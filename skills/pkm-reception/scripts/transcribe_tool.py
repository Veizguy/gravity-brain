import os
import sys
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def transcribe_audio(file_path):
    """
    Transcribes audio file using OpenAI Whisper API.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment.")
        sys.exit(1)

    client = openai.OpenAI(api_key=api_key)

    try:
        with open(file_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                language="da" # Danish
            )
        return transcript.text
    except Exception as e:
        print(f"Error during transcription: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transcribe_tool.py <path_to_audio_file>")
        sys.exit(1)

    audio_path = sys.argv[1]
    if not os.path.exists(audio_path):
        print(f"Error: File not found at {audio_path}")
        sys.exit(1)

    text = transcribe_audio(audio_path)
    print(text)
