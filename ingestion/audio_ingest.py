import whisper

try:
    model = whisper.load_model("base")
except Exception as e:
    model = None
    print("⚠️ Whisper model failed to load:", e)

def transcribe_audio(file):
    if not model:
        return "[Transcription unavailable: Whisper not loaded]"
    try:
        result = model.transcribe(file.name)
        transcript = result.get("text", "").strip()
        return transcript if transcript else "[No audio content detected]"
    except Exception as e:
        print(f"[ERROR] Transcription failed: {e}")
        return "[Transcription failed]"