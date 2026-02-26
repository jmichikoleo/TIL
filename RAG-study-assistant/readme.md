# RAG STUDY ASSISTANT 

---

A local **Flask + OpenAI** study assistant for generating flashcards and Q&A from text or PDF documents. 
Built to run locally or inside Docker, with offline-friendly features and easy deployment.

---

## Features

- Generate flashcards from uploaded `.txt` or `.pdf` files.  
- Generate question & answer pairs from custom text input.  
- Three-step chaining agents for high-quality flashcards and Q&A.  
- Interactive flashcard UI with front/back flipping.  
- Docker-ready for easy deployment.  

---

## Project Structure

RAG-study-assistant/
- app.py 
- Dockerfile 
- requirements.txt 
- .gitignore
- .env.example 
- data/ 
- static/ 
- templates/ 
- utils/ 

--- 
## Getting Started (Local Python)

1. Clone the repository

```bash
git clone https://github.com/your-username/RAG-study-assistant.git
cd RAG-study-assistant

2. Create the environment

```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows

3. Install dependencies

```
pip install -r requirements.txt

4. Run the app

python app.py

5. Open your browser

http://localhost:5000

---

## Usage 

### Flashcards

- Upload a .txt or .pdf file.

- Click Generate Flashcards.

- Flip cards to see answers.

### Q&A

- Enter a custom question in the Q&A section.

- Click Ask

- View generated answers
