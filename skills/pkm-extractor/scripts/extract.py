import argparse
import sys
import os
import shutil
import tempfile
from pathlib import Path

def extract_pdf(filepath):
    """Robust PDF extraction: Try text first, then fallback to OCR if needed."""
    try:
        from pypdf import PdfReader
    except ImportError:
        # If pypdf is not available, we skip straight to OCR
        return extract_pdf_ocr(filepath)
    
    try:
        reader = PdfReader(filepath)
        text = []
        for i, page in enumerate(reader.pages):
            page_text = page.extract_text()
            if page_text and len(page_text.strip()) > 50: # Simple heuristic for "real" text
                text.append(f"--- Page {i+1} (Text) ---\n{page_text}")
            else:
                # Text is too sparse, try OCR on this page
                page_ocr = extract_pdf_page_ocr(filepath, i)
                text.append(f"--- Page {i+1} (OCR) ---\n{page_ocr}")
                
        return "\n\n".join(text)
    except Exception:
        return extract_pdf_ocr(filepath)

def extract_pdf_page_ocr(filepath, page_index):
    """OCR a specific page of a PDF."""
    try:
        from pdf2image import convert_from_path
        import pytesseract
        
        # Only convert the specific page to save memory
        images = convert_from_path(filepath, first_page=page_index+1, last_page=page_index+1)
        if images:
            return pytesseract.image_to_string(images[0], lang='dan+eng')
    except Exception as e:
        return f"[OCR Error on page {page_index+1}: {e}]"
    return ""

def extract_pdf_ocr(filepath):
    """Full OCR of a PDF file using pdf2image."""
    try:
        from pdf2image import convert_from_path
        import pytesseract
        
        images = convert_from_path(filepath)
        text = []
        for i, img in enumerate(images):
            page_text = pytesseract.image_to_string(img, lang='dan+eng')
            text.append(f"--- Page {i+1} (Full OCR) ---\n{page_text}")
        return "\n\n".join(text)
    except Exception as e:
        print(f"Failed to OCR PDF: {e}", file=sys.stderr)
        sys.exit(1)

def extract_image(filepath):
    """OCR an image file."""
    try:
        from PIL import Image
        import pytesseract
    except ImportError:
        print("Error: Pillow or pytesseract not installed.", file=sys.stderr)
        sys.exit(1)
        
    try:
        img = Image.open(filepath)
        text = pytesseract.image_to_string(img, lang='dan+eng')
        return text
    except Exception as e:
        print(f"Failed to read Image. Error: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Extract text from PDF or Image files via OCR.")
    parser.add_argument("file", help="Path to the PDF or Image file")
    
    args = parser.parse_args()
    filepath = args.file
    
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' does not exist.", file=sys.stderr)
        sys.exit(1)
        
    ext = os.path.splitext(filepath)[1].lower()
    
    if ext == '.pdf':
        text = extract_pdf(filepath)
    elif ext in ['.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif']:
        text = extract_image(filepath)
    else:
        print(f"Error: Unsupported extension '{ext}'.", file=sys.stderr)
        sys.exit(1)
        
    print(text)

if __name__ == "__main__":
    main()
