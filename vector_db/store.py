from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from langchain.vectorstores import Qdrant
from langchain.embeddings import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer

COLLECTION_NAME = "rag_docs"
model = SentenceTransformer("all-MiniLM-L6-v2")
client = QdrantClient("localhost", port=6333)

def ensure_collection():
    if COLLECTION_NAME not in [c.name for c in client.get_collections().collections]:
        client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE),
        )

def store_embedding(text, metadata):
    ensure_collection()
    vector = model.encode(text).tolist()
    payload = {"page_content": text, **metadata}  # Ensure page_content is available in payload
    client.upload_collection(
        collection_name=COLLECTION_NAME,
        vectors=[vector],
        payload=[payload]
    )

def get_vectorstore():
    ensure_collection()
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return Qdrant(
        client=client,
        collection_name=COLLECTION_NAME,
        embeddings=embedding,
    )