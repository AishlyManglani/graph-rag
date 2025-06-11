from PIL import Image
import pytesseract

def extract_text_from_image(file):
    try:
        image = Image.open(file)
        text = pytesseract.image_to_string(image)
        return text.strip() if text else "[No text found in image]"
    except pytesseract.TesseractNotFoundError:
        return "[Tesseract is not installed. OCR failed.]"
    except Exception as e:
        return f"[Image OCR failed: {str(e)}]"