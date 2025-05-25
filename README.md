
```markdown
# 📈 Exotic Finance Assistant

An intelligent Q&A assistant built using **RAG (Retrieval-Augmented Generation)** to answer complex questions related to **exotic options in finance**. This system combines PDF content extraction, vector-based document indexing using ChromaDB, and LLM-powered responses using **Gemini 1.5 Flash**.

---

## 🚀 Features

- 📄 Automatic PDF text extraction
- 🔍 Smart chunking of content for better retrieval
- 💾 Vector database integration with [ChromaDB](https://docs.trychroma.com/)
- 🧠 Gemini-powered LLM for answer generation
- 🌐 REST API with [FastAPI](https://fastapi.tiangolo.com/)
- 🌍 Automatic translation of user queries to English
- 🔗 Easily connectable with a front-end via HTTP

---

## 🛠️ Project Structure

```

📁 Exotic-Finance-Assistant
│
├── data/                  # Contains the input PDF file
├── chroma\_db/             # Vector database files (ChromaDB)
├── src/                   # Core logic modules
│   ├── pdf\_utils.py       # PDF text extraction
│   ├── chunking.py        # Text segmentation
│   ├── db.py              # ChromaDB setup and interaction
│   ├── rag\_pipeline.py    # RAG pipeline logic
│   └── llm\_utils.py       # Translation + Gemini API calls
├── main.py                # FastAPI server entrypoint
├── prompt.py              # System prompt for Gemini
├── requirements.txt       # Python dependencies
├── .env                   # Configuration file (API keys, etc.)
└── README.md              # This file

````

---

## ⚙️ Installation

### 1. Clone the project

```bash
git clone https://github.com/fofanaibrahimseloh/Exotic-Finance-Assistant.git
cd Exotic-Finance-Assistant
````

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file at the root:

```
GEMINI_API_KEY=your_google_api_key
DB_PATH=chroma_db
COLLECTION_NAME=exotic_option
PDF_PATH=data/exotic_option.pdf
```

---

## ▶️ Run the API locally

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### ✨ Available Endpoints

* `GET /query?query=...` → Ask a question about exotic finance
* `POST /init` → Initializes the PDF indexing (run once)

---

## ☁️ Deployment

### Backend (FastAPI)

* Deploy via [Railway](https://railway.app/)
* Add `.env` variables in Railway's dashboard

### Frontend (Optional)

* Connect via `fetch("/query?query=...")`
* Deploy your front-end using [Cloudflare Pages](https://pages.cloudflare.com/)

---

## 💬 Sample Question

```bash
GET /query?query=What are the characteristics of an Asian option?
```

---

## 📚 References

* [ChromaDB Docs](https://docs.trychroma.com/)
* [Gemini API by Google](https://ai.google.dev/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Exotic Options - Investopedia](https://www.investopedia.com/terms/e/exoticoption.asp)

---

## 👨‍💻 Author

**Fofana Ibrahim Seloh**
Engineering student passionate about market finance, AI, and data science.
📫 [LinkedIn](https://www.linkedin.com/in/fofanaibrahimseloh) • ✉️ [Email](mailto:fofanaibseloh@gmail.com)

---

## 🛡️ License

This project is licensed under the MIT License.

```

---

Let me know if you'd like me to push it directly to your GitHub repo or prepare it in a file you can download.
```
