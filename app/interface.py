import streamlit as st
from ingestion.pdf_ingest import extract_text_from_pdf
from ingestion.image_ingest import extract_text_from_image
from ingestion.audio_ingest import transcribe_audio
from generator.rag_engine import generate_answer
from graph.create_graph import create_graph_from_text
from retriever.orchestrator import hybrid_retrieve
from vector_db.store import store_embedding

SUPPORTED_TYPES = {
    "pdf": extract_text_from_pdf,
    "png": extract_text_from_image,
    "jpg": extract_text_from_image,
    "jpeg": extract_text_from_image,
    "mp3": transcribe_audio
}

UNUSABLE_RESPONSES = {
    "[transcription unavailable: whisper not loaded]",
    "[no audio content detected]",
    "[transcription failed]",
    "[tesseract is not installed. ocr failed.]",
    "[image ocr failed]",
    "[no text found in image]",
    "[no text found in pdf]",
    "[no content extracted]",
    "",
    None
}

def launch_ui():
    st.title("Multimodal Graph RAG Assistant")
    uploaded_file = st.file_uploader("Upload your file (.pdf/.jpg/.png/.mp3)", type=["pdf", "jpg", "png", "mp3", "jpeg"])

    if uploaded_file:
        file_type = uploaded_file.name.split('.')[-1].lower()
        extractor = SUPPORTED_TYPES.get(file_type)

        if extractor:
            content = extractor(uploaded_file)
            st.session_state["doc"] = content

            if (
                isinstance(content, str)
                and content.strip().lower() not in UNUSABLE_RESPONSES
            ):
                clean_text = content.strip()
                store_embedding(clean_text, {"source": uploaded_file.name, "page_content": clean_text})
                create_graph_from_text(clean_text)
            else:
                st.warning("No usable content could be extracted from the file.")
        else:
            st.error("Unsupported file type")

    query = st.text_input("Ask a question:")
    if query and "doc" in st.session_state:
        result = hybrid_retrieve(query)
        st.markdown(f"### Answer:\n{result}")
