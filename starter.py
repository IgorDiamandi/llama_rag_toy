import openai
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_response(question):
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()

    response = query_engine.query(question)
    #print(response)
    return response
