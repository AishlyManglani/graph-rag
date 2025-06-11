# graph-rag

# 🧠 Enterprise Multimodal Graph RAG System

A modular prototype RAG system that ingests text, images, and audio, builds a knowledge graph and vector database, and answers natural language queries via hybrid search.

---

## 🚀 Features
- ✅ Multimodal ingestion: `.pdf`, `.jpg/.png`, `.mp3`
- ✅ Entity and relation extraction via LLM
- ✅ Graph database with Neo4j
- ✅ Vector database with Qdrant
- ✅ Hybrid search: keyword, vector, graph traversal
- ✅ UI via Streamlit
- ✅ Evaluation suite and tests included

---

## 🧱 Architecture
- **Ingestion**: PyMuPDF, Tesseract, Whisper
- **Graph DB**: Neo4j (via Py2Neo)
- **Vector Store**: Qdrant + SentenceTransformers
- **Answer Generation**: LangChain + OpenAI
- **Evaluation**: Latency, hallucination, accuracy
- **UI**: Streamlit

---

## 🧪 Evaluation

Run:
```bash
python evals/evaluate.py
