# graph-rag

# 🧠 Enterprise Multimodal Graph RAG System

A modular prototype RAG system that ingests text, images, and audio, builds a knowledge graph and vector database, and answers natural language queries via hybrid search.

---

## Demo Video:
https://drive.google.com/file/d/1KpIAw14Djjxp_ffA5OTCxzDSPJ_l7u2A/view?usp=sharing

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


## 🛠️ Local Setup Instructions

### ✅ 1. Clone the Repository
```bash
git clone https://github.com/AishlyManglani/graph-rag.git
cd graph-rag
```

---

### ✅ 2. Create and Activate a Virtual Environment
#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### ✅ 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> ⚠️ Ensure you have `ffmpeg` and `tesseract` installed and in your system PATH:
> - **Tesseract**: https://github.com/tesseract-ocr/tesseract
> - **FFmpeg**: https://ffmpeg.org/download.html

---

### ✅ 4. Set Up Environment Variables
Create a `.env` file in the project root:
```env
GOOGLE_API_KEY=your-gemini-api-key
```

---

### ✅ 5. Start Neo4j and Qdrant
Ensure Docker is installed and running, then:
```bash
docker compose up -d
```
This will start:
- `neo4j` on ports `7474` (UI) and `7687` (Bolt)
- `qdrant` on port `6333` (Vector DB)

---

### ✅ 6. Launch the App
```bash
streamlit run run.py
```
Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

### ✅ 7. Run Evaluation Suite (Optional)
```bash
python -m evals.evaluate
```
This runs a minimal set of test queries and logs accuracy + latency.

---

## ✅ File Types Supported
- PDF (.pdf)
- Image (.jpg, .png, .jpeg)
- Audio (.mp3)





