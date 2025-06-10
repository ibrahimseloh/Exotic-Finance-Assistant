Here's the English version of the `README.md` file:

````markdown
# Praxis - Q/A Assistant for Exotic Options

**Praxis** is an intelligent assistant for exotic options finance, utilizing large language models (LLM) to answer questions related to exotic options and structured finance products. The system is based on the **RAG (Retrieval-Augmented Generation)** architecture, extracting and indexing information from PDF files while generating precise and detailed answers.

## Key Features

- **PDF Data Extraction**: The application extracts data from a PDF file regarding exotic options and indexes it into a ChromaDB database.
- **Natural Language Answers**: The tool generates detailed, quantitative, and rigorous responses using Google's **Gemini 1.5 Flash** model.
- **User Interface with Streamlit**: An interactive interface allowing users to ask questions and view answers, along with the sources used to generate those answers.

## Prerequisites

Before running the application, you need to install the following dependencies:

### Dependencies

- **FastAPI**: Framework for building the RESTful API.
- **uvicorn**: ASGI server for running the FastAPI application.
- **chromadb**: Used for managing the Chroma database.
- **pydantic**: Data validation for input and output.
- **PyPDF2**: Library to extract text from PDF files.
- **google-generativeai**: For integration with Google's **Gemini 1.5 Flash** model.
- **python-dotenv**: For managing environment variables.
- **streamlit**: Library for creating the user interface.
- **streamlit-pdf-viewer**: For displaying PDF files in Streamlit.

You can install these libraries by running:

```bash
pip install -r requirements.txt
```

## Configuration

1. **Gemini API Key**: Before using the application, you need to configure the Gemini API key. Use the sidebar interface in Streamlit to enter your API key. This key is required to interact with the **Gemini 1.5 Flash** model.

2. **File Paths**:
   - **PDF_PATH**: The path to the PDF file containing information about exotic options.
   - **DB_PATH**: The path where the Chroma database will be stored.
   - **COLLECTION_NAME**: The name of the Chroma collection where the extracted data will be stored.

## Running the Application

1. Ensure **FastAPI** and **Uvicorn** are installed.
2. Run the API using Uvicorn:

```bash
uvicorn app:app --reload
```

This will start the API on `http://localhost:8000`.

3. To start the Streamlit interface, use the following command:

```bash
streamlit run app.py
```

This will open the application in your browser at `http://localhost:8501`.

## API Endpoints

### `GET /set_gemini_key/`

This endpoint allows you to set the Gemini API key required to interact with the model. You must send the key via a GET request with the `api_key` parameter.

**Example:**

```bash
GET http://localhost:8000/set_gemini_key/?api_key=your_api_key
```

### `GET /query`

This endpoint allows you to ask questions and get answers about exotic options from the extracted and indexed data in ChromaDB. You must send a GET request with the `query` parameter.

**Example:**

```bash
GET http://localhost:8000/query?query=What is the difference between an Asian option and a barrier option?
```

Response: A structured response containing the answer and the sources used.

## Project Structure

Here is the project structure:

```
├── app.py                    # FastAPI application
├── requirements.txt           # List of dependencies
├── src/
│   ├── db.py                 # Code for managing the ChromaDB database
│   ├── rag_pipeline.py       # RAG pipeline for generating answers
│   └── llm_utils.py          # Utilities for interacting with the Gemini model
├── data/
│   └── exotic_option.pdf     # PDF file containing financial information
├── .env                       # Environment variables (optional)
└── README.md                 # This file
```

## Contribution

Contributions are welcome! If you want to improve this project, feel free to open an *issue* or a *pull request*.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

---

Developed by **Fofana Ibrahim Seloh** – [LinkedIn](https://www.linkedin.com/in/ibrahim-seloh-fofana-6073b4291/)
```

Make sure this file is placed in the root of your project to properly document the setup and usage steps.
````
