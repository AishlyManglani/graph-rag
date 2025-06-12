import whisper
import os
import google.generativeai as genai

try:
    model = whisper.load_model("base")
except Exception:
    model = None

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def transcribe_audio(file):
    try:
        if model:
            result = model.transcribe(file.name)
            text = result.get("text", "").strip()
            if text: return text
    except Exception:
        pass

    # Fallback: use Gemini for captioning
    try:
        audio_path = file.name
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(f"Summarize this audio file: {audio_path}")
        return response.text.strip() or "[No transcription from Gemini]"
    except Exception as e:
        return f"[Audio analysis failed: {e}]"
