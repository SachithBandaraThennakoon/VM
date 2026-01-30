import faiss
import numpy as np
from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()


client = OpenAI()

def embed_text(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return np.array(response.data[0].embedding)

index = faiss.IndexFlatL2(1536)
documents = []

def add_document(text):
    vector = embed_text(text)
    index.add(np.array([vector]))
    documents.append(text)

def search(query, k=3):
    if len(documents) == 0:
        return ["No prior knowledge available. Focus on fundamentals."]

    q_vec = embed_text(query)
    D, I = index.search(np.array([q_vec]), k)

    results = []
    for i in I[0]:
        if i < len(documents):
            results.append(documents[i])

    return results
