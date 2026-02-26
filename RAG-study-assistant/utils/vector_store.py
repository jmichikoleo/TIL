import os
import numpy as np
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def embed_texts(texts, model="text-embedding-3-small"):
    response = client.embeddings.create(
        model=model,
        input=texts
    )
    return [e.embedding for e in response.data]


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def build_vector_store(chunks):
    texts = [c["text"] for c in chunks]
    embeddings = embed_texts(texts)
    return embeddings, chunks


def search(query, embeddings, chunks, top_k=3):
    query_emb = embed_texts([query])[0]

    scores = [
        cosine_similarity(query_emb, emb)
        for emb in embeddings
    ]

    top_indices = np.argsort(scores)[::-1][:top_k]
    return [chunks[i] for i in top_indices]