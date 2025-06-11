# Praxis - Q/A Assistant for Exotic Options

**Praxis** is an intelligent assistant designed for exotic options finance, using large language models (LLMs) to answer questions related to exotic options and structured finance products. The system is based on the **RAG (Retrieval-Augmented Generation)** architecture, extracting and indexing information from PDF files and generating precise answers.

## Key Features

* **PDF Data Extraction**: Extracts data from a PDF containing exotic options and indexes it into a **ChromaDB** database.
* **Natural Language Answers**: Generates detailed, rigorous, and quantitative responses using **Gemini 1.5 Flash** (Google AI).
* **User Interface with Streamlit**: Allows users to ask questions and view answers along with the sources used to generate them.

## Prerequisites

Before running the application, install the following dependencies:

### Dependencies

* **FastAPI**: Framework for building the RESTful API.
* **uvicorn**: ASGI server for running the FastAPI application.
* **chromadb**: Manages the Chroma database.
* **pydantic**: Data validation for input and output.
* **PyPDF2**: Extracts text from PDF files.
* **google-generativeai**: For integration with Google's **Gemini 1.5 Flash** model.
* **python-dotenv**: For managing environment variables.
* **streamlit**: For the user interface.
* **streamlit-pdf-viewer**: For displaying PDF files within Streamlit.

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

1. **Gemini API Key**: You must configure your Gemini API key to interact with the **Gemini 1.5 Flash** model. Enter the API key in the sidebar interface provided by Streamlit.

2. **File Paths**:

   * **PDF\_PATH**: Path to the PDF containing information on exotic options.
   * **DB\_PATH**: Path where the Chroma database will be stored.
   * **COLLECTION\_NAME**: Name of the Chroma collection for storing the extracted data.

## Running the Application

### 1. **Start the API**

Ensure **FastAPI** and **Uvicorn** are installed. Then run the API:

```bash
uvicorn app:app --reload
```

This will start the API at `http://localhost:8000`.

### 2. **Start Streamlit Interface**

To start the Streamlit interface:

```bash
streamlit run app.py
```

This will open the application in your browser at `http://localhost:8501`.


## API Endpoints

### `GET /set_gemini_key/`

This endpoint allows you to set the Gemini API key to interact with the model. Send the key via a GET request with the `api_key` parameter.

**Example:**

```bash
GET http://localhost:8000/set_gemini_key/?api_key=your_api_key
```

### `GET /query`

This endpoint allows you to ask questions about exotic options from the extracted data in ChromaDB. Send a GET request with the `query` parameter.

**Example:**

```bash
GET http://localhost:8000/query?query=What is the difference between an Asian option and a barrier option?
```

Response: A structured answer with sources used.

## Project Structure

Here’s the updated project structure:

```
├── app.py                    # FastAPI application
├── requirements.txt           # List of dependencies
├── start.sh                  # Script to run FastAPI and Streamlit
├── railway.json              # Railway deployment configuration
├── Dockerfile                # Dockerfile for containerization
├── src/
│   ├── db.py                 # Code for managing the ChromaDB database
│   ├── rag_pipeline.py       # RAG pipeline for generating answers
│   ├── llm_utils.py          # Utilities for interacting with the Gemini model
│   └── pdf_utils.py          # Utilities for PDF extraction
├── data/
│   └── exotic_option.pdf     # PDF file containing financial information
├── .env                       # Environment variables (optional)
└── README.md                 # This file
```

## Contribution

Contributions are welcome! If you want to improve the project, feel free to open an **issue** or submit a **pull request**.

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

---

Developed by **Fofana Ibrahim Seloh** – [LinkedIn](https://www.linkedin.com/in/ibrahim-seloh-fofana-6073b4291/)

---

This updated README reflects the added files (`start.sh`, `railway.json`, `Dockerfile`, and `src/pdf_utils.py`), and ensures that everything is clearly explained for setting up and running the project.
