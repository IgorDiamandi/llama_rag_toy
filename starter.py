from transformers import pipeline
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
import os

generator = pipeline('text-generation', model='gpt2')


def get_response(question):
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()

    response = query_engine.query(question)
    response_text = str(response)
    extended_response = generator(response_text, max_length=10000, num_return_sequences=1, truncation=True)[0]["generated_text"]
    return extended_response


# Test it
if __name__ == "__main__":
    question = "What is the main idea of the book Good Omens?"
    print(get_response(question))
