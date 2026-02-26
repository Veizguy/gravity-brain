import os
import time
import json
import logging
import asyncio
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Load environment variables
load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ALLOWED_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
VAULT_PATH = os.getenv("VAULT_PATH", "/Users/mikkelfeld/obsidian/brain")

# Paths (Relative to Vault or Absolute)
INBOX_DIR = Path(VAULT_PATH) / "1 - Inbox"
OUTBOX_RAW = Path(VAULT_PATH) / "outbox" / "chat-out" / "raw"
OUTBOX_PROCESSED = Path(VAULT_PATH) / "outbox" / "chat-out" / "processed"

# Ensure directories exist
INBOX_DIR.mkdir(parents=True, exist_ok=True)
OUTBOX_RAW.mkdir(parents=True, exist_ok=True)
OUTBOX_PROCESSED.mkdir(parents=True, exist_ok=True)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle incoming messages and save to inbox/chat-in/"""
    chat_id = str(update.effective_chat.id)
    
    # Simple security: Only respond to the configured chat ID
    if ALLOWED_CHAT_ID and chat_id != ALLOWED_CHAT_ID:
        logging.warning(f"Unauthorized access from chat_id: {chat_id}")
        return

    timestamp = int(time.time())
    payload = {
        "timestamp": timestamp,
        "chat_id": chat_id,
        "username": update.effective_user.username,
        "type": "text",
        "text": update.message.text
    }

    # Handle Voice/Audio
    if update.message.voice or update.message.audio:
        file = await update.message.voice.get_file() if update.message.voice else await update.message.audio.get_file()
        file_ext = "ogg" if update.message.voice else "mp3"
        file_name = f"{timestamp}_telegram_voice.{file_ext}"
        file_path = INBOX_DIR / "audio" / file_name
        await file.download_to_drive(file_path)
        payload["type"] = "audio"
        payload["file_path"] = str(file_path)
        payload["text"] = update.message.caption or "[Audio Message]"

    # Save JSON to inbox
    json_path = INBOX_DIR / f"{timestamp}_telegram_chat.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    
    logging.info(f"Saved message to {json_path}")

async def monitor_outbox(application):
    """Monitor outbox/chat-out/raw/ for files and send them to Telegram"""
    logging.info("Starting outbox monitor...")
    while True:
        try:
            for file_path in OUTBOX_RAW.iterdir():
                if file_path.is_file() and not file_path.name.startswith('.'):
                    logging.info(f"Found outgoing message: {file_path.name}")
                    
                    # Read content
                    content = ""
                    try:
                        if file_path.suffix == '.json':
                            with open(file_path, 'r', encoding='utf-8') as f:
                                data = json.load(f)
                                content = data.get("text", "")
                        else:
                            with open(file_path, 'r', encoding='utf-8') as f:
                                content = f.read()

                        if content:
                            await application.bot.send_message(
                                chat_id=ALLOWED_CHAT_ID, 
                                text=content
                            )
                            # Move to processed
                            target_path = OUTBOX_PROCESSED / file_path.name
                            file_path.rename(target_path)
                            logging.info(f"Sent message and moved to {target_path}")
                        
                    except Exception as e:
                        logging.error(f"Error processing {file_path}: {e}")
            
        except Exception as e:
            logging.error(f"Outbox monitor error: {e}")
            
        await asyncio.sleep(5)  # Poll every 5 seconds

def main():
    if not TOKEN:
        logging.error("TELEGRAM_BOT_TOKEN not found!")
        return

    application = ApplicationBuilder().token(TOKEN).build()
    
    # Handle text and voice
    message_handler = MessageHandler(filters.TEXT | filters.VOICE | filters.AUDIO, handle_message)
    application.add_handler(message_handler)

    # Start polling
    logging.info("Telegram Bot started. Polling for messages...")
    
    # We need to run the monitor_outbox loop alongside polling
    loop = asyncio.get_event_loop()
    loop.create_task(monitor_outbox(application))
    
    application.run_polling()

if __name__ == '__main__':
    main()
