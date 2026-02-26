from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def answer_query(prompt, chunks=None):
    """
    Send a prompt to OpenAI. Optionally provide chunks as context.
    """
    context_text = "\n\n".join(c["text"] for c in chunks) if chunks else ""
    full_prompt = f"{prompt}\n\nContext:\n{context_text}" if context_text else prompt

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": full_prompt}],
        temperature=0
    )
    return response.choices[0].message.content.strip()


# === Flashcard Steps ===
def generate_flashcards_step1(text, chunk_size=300, overlap=50):
    from utils.chunker import chunk_text
    chunks = chunk_text(text, chunk_size=chunk_size, overlap=overlap)
    return chunks  # Step 1 output

def generate_flashcards_step2(chunks, cards_per_chunk=2):
    raw_flashcards = []
    for chunk in chunks:
        prompt = f"""
You are a study assistant.
Create {cards_per_chunk} flashcards from the text below.

Format EXACTLY like this:
Q: question
A: answer

Text:
{chunk['text']}
"""
        resp = answer_query(prompt)
        blocks = resp.split("Q:")
        for block in blocks[1:]:
            if "A:" in block:
                q, a = block.split("A:", 1)
                raw_flashcards.append({"question": q.strip(), "answer": a.strip()})
    return raw_flashcards

def generate_flashcards_step3(raw_flashcards):
    # Step 3: simple aggregator, can deduplicate or sort
    seen = set()
    final_cards = []
    for card in raw_flashcards:
        key = (card['question'], card['answer'])
        if key not in seen:
            seen.add(key)
            final_cards.append(card)
    return final_cards


# === Q&A Steps ===
def generate_qa_step1(text, chunk_size=300, overlap=50):
    from utils.chunker import chunk_text
    chunks = chunk_text(text, chunk_size=chunk_size, overlap=overlap)
    return chunks

def generate_qa_step2(chunks, num_pairs=2):
    raw_pairs = []
    for chunk in chunks:
        prompt = f"""
You are a helpful study assistant.
From the text below, create {num_pairs} useful Q&A pairs.

Format EXACTLY like this:
Q: question
A: answer

Text:
{chunk['text']}
"""
        resp = answer_query(prompt)
        blocks = resp.split("Q:")
        for block in blocks[1:]:
            if "A:" in block:
                q, a = block.split("A:", 1)
                raw_pairs.append({"question": q.strip(), "answer": a.strip()})
    return raw_pairs

def generate_qa_step3(raw_pairs):
    # Step 3: aggregator / deduplicate
    seen = set()
    final_pairs = []
    for pair in raw_pairs:
        key = (pair['question'], pair['answer'])
        if key not in seen:
            seen.add(key)
            final_pairs.append(pair)
    return final_pairs