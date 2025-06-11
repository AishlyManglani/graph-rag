from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from generator.rag_engine import generate_answer

# Placeholder: you can integrate Cypher query + keyword match here in future

def classify_query_type(query):
    if any(q in query.lower() for q in ["who", "when", "where"]):
        return "lookup"
    elif any(q in query.lower() for q in ["summarize", "overview"]):
        return "summarization"
    else:
        return "semantic"

def hybrid_retrieve(query):
    query_type = classify_query_type(query)
    # Logic to adjust retrieval mode can go here
    return generate_answer(query)
