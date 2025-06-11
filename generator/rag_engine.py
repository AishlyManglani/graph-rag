import os
import asyncio
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from vector_db.store import get_vectorstore
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

load_dotenv()

asyncio.set_event_loop(asyncio.new_event_loop())

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
retriever = get_vectorstore().as_retriever()

qa_prompt = PromptTemplate.from_template(
    "Use the following context to answer the question:\n\nContext: {context}\n\nQuestion: {question}\n\nAnswer:"
)
qa_chain = LLMChain(llm=llm, prompt=qa_prompt)

def generate_answer(query, content=None):
    docs = retriever.get_relevant_documents(query)
    context = "\n".join([doc.page_content for doc in docs])
    return qa_chain.run({"context": context, "question": query})