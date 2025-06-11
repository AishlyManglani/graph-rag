import os
import re
import asyncio
import ast
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage

load_dotenv()

prompt = PromptTemplate(
    input_variables=["text"],
    template="""
Extract meaningful triples (subject, relation, object) from the text:

Example:
"Elon Musk founded SpaceX." -> ["Elon Musk", "founded", "SpaceX"]

Text:
{text}
Return a Python list of triples.
"""
)

def extract_triples(text):
    asyncio.set_event_loop(asyncio.new_event_loop())  # for Gemini gRPC client

    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
    formatted_prompt = prompt.format(text=text)
    response = llm([HumanMessage(content=formatted_prompt)])

    # Remove ``` blocks and whitespace
    cleaned = re.sub(r"```[a-zA-Z]*", "", response.content or "").strip("`\n ")

    try:
        return ast.literal_eval(cleaned)
    except Exception as e:
        print("⚠️ Failed to parse Gemini response:", e)
        return []
