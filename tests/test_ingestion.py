def test_pdf_extraction():
    from ingestion.pdf_ingest import extract_text_from_pdf
    with open("tests/sample.pdf", "rb") as f:
        text = extract_text_from_pdf(f)
        assert len(text) > 10

def test_image_extraction():
    from ingestion.image_ingest import extract_text_from_image
    with open("tests/sample.jpg", "rb") as f:
        text = extract_text_from_image(f)
        assert len(text) > 5

def test_audio_transcription():
    from ingestion.audio_ingest import transcribe_audio
    class File: name = "tests/sample.mp3"
    text = transcribe_audio(File())
    assert len(text) > 5
