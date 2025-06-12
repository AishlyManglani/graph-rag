import os
from PIL import Image
from google.generativeai import GenerativeModel
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def extract_text_from_image(file):
    try:
        image = Image.open(file)
        model = genai.GenerativeModel("gemini-pro-vision")
        response = model.generate_content([image, "Describe this image."])
        text = response.text.strip()
        return text if text else "[No description returned by Gemini]"
    except Exception as e:
        return f"[Image analysis failed: {e}]"
