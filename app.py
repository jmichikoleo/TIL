from flask import Flask, render_template, request
from utils.text_loader import load_text
from utils.llm import (
    generate_flashcards_step1, generate_flashcards_step2, generate_flashcards_step3,
    generate_qa_step1, generate_qa_step2, generate_qa_step3
)
import os
import hashlib

app = Flask(__name__)

UPLOAD_FOLDER = "data/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
DECK_CACHE = {}

def hash_file(file_bytes):
    return hashlib.md5(file_bytes).hexdigest()

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in {"txt", "pdf"}

@app.route("/", methods=["GET", "POST"])
def index():
    flashcards = None
    qa_pairs = None
    error = None

    if request.method == "POST":
        action = request.form.get("action")

        # === Flashcards ===
        if action == "flashcards":
            file = request.files.get("file")
            if not file or file.filename == "":
                error = "❌ Please upload a file first."
            elif not allowed_file(file.filename):
                error = "❌ Only .txt or .pdf allowed."
            else:
                file_bytes = file.read()
                file_hash = hash_file(file_bytes)
                file_path = os.path.join(UPLOAD_FOLDER, file.filename)
                with open(file_path, "wb") as f:
                    f.write(file_bytes)

                if file_hash not in DECK_CACHE:
                    text = load_text(file_path)
                    chunks = generate_flashcards_step1(text)
                    raw_cards = generate_flashcards_step2(chunks)
                    flashcards = generate_flashcards_step3(raw_cards)
                    DECK_CACHE[file_hash] = {"filename": file.filename, "flashcards": flashcards}
                else:
                    flashcards = DECK_CACHE[file_hash]["flashcards"]

        # === Q&A ===
        elif action == "qa":
            context_text = request.form.get("question_context")
            if not context_text:
                error = "❌ Please provide text for Q&A."
            else:
                chunks = generate_qa_step1(context_text)
                raw_pairs = generate_qa_step2(chunks)
                qa_pairs = generate_qa_step3(raw_pairs)

    return render_template("index.html", flashcards=flashcards, qa_pairs=qa_pairs, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)