def chunk_text(text, chunk_size=300, overlap=50, source="sample.txt"):
    chunks = []
    start = 0
    chunk_id = 0

    while start < len(text):
        end = start + chunk_size
        chunk_text = text[start:end]

        chunks.append({
            "id": chunk_id,
            "text": chunk_text,
            "source": source
        })

        chunk_id += 1
        start = end - overlap

    return chunks