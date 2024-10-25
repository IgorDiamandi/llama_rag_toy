import openai
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

openai.api_key = "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"


def get_response(question):
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()

    response = query_engine.query(question)
    #print(response)
    return response
