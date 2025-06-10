import streamlit as st
import requests
import fitz  # PyMuPDF
from PIL import Image
import os
from markdown import markdown

# ─── CONFIG ───
API_GEMINI_KEY = "http://localhost:8000/set_gemini_key"
API_URL = "http://localhost:8000/query"
PDF_PATH = "data/exotic_option.pdf"

st.set_page_config(layout="wide")
st.title("🤖 Praxis – Assistant Q/A pour les Options Exotiques")

# ─── SIDEBAR POUR CLÉ API GEMINI ───
with st.sidebar:
    st.header("⚙️ Configuration")
    gemini_key = st.text_input("Entrez votre clé API Gemini", type="password")
    if st.button("Envoyer la clé API"):
        if gemini_key.strip():
            response = requests.get(API_GEMINI_KEY, params={"api_key": gemini_key})
            if response.status_code == 200:
                st.success("Clé API Gemini envoyée avec succès !")
            else:
                st.error(f"Erreur lors de l'envoi de la clé API : {response.status_code}")
        else:
            st.warning("Veuillez entrer une clé API valide.")

# ─── INTRO ───
st.markdown(
    """
    <div style="background-color: #0d1b2a; padding: 1.2rem 1rem;
                border-radius: 6px; margin-bottom: 1.5rem; color: #e0e1dd;">
        <h4 style="margin-bottom: 0.5em;">📘 <strong>Praxis – Assistant Q/R pour les Options Exotiques</strong></h4>
        <p style="font-size: 1.5em; line-height: 1.6;">
            Basé sur l’architecture <strong>RAG (Retrieval-Augmented Generation)</strong>, Praxis répond à vos questions sur les options exotiques en finance.
            Il extrait le contenu d’un PDF, l’indexe avec <em>ChromaDB</em>, et génère des réponses précises grâce au LLM <strong>Gemini 1.5 Flash</strong>.
        </p>
        <p style="font-size: 0.85em; margin-top: 1em;">
            🛠️ Conçu et développé par <strong>Fofana Ibrahim Seloh</strong> • <a href='https://www.linkedin.com/in/ibrahim-seloh-fofana-6073b4291/' target='_blank' style='color: #91e0ff;'>LinkedIn</a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ─── ZONE DE RECHERCHE ───
st.markdown("#### 🔍 Posez votre question :")
search_col, _ = st.columns([6, 4])  # pour aligner à gauche
with search_col:
    question = st.text_input(
        label="",
        placeholder="Ex : Quelle est la différence entre une option asiatique et une barrière ?",
        label_visibility="collapsed"
    )
    if st.button("🚀 Envoyer"):
        if question.strip():
            with st.spinner("⏳ Génération en cours..."):
                res = requests.get(API_URL, params={"query": question})
                if res.status_code == 200:
                    data = res.json()
                    st.session_state.bot_response = data["bot_response"]
                    st.session_state.sources = data["sources"]
                else:
                    st.error(f"❌ Erreur API {res.status_code}")

# ─── LAYOUT PRINCIPAL ───
col_left, col_right = st.columns([3, 2], gap="large")

# ─── GAUCHE : réponse + sources ───
with col_left:
    if "bot_response" in st.session_state:
        st.markdown("#### 💬 Réponse")
        html_response = markdown(st.session_state.bot_response)
        st.markdown(
            f"""
            <div style="height: 700px; overflow-y: auto; margin-top: 20px;
                        background-color: #0d1b2a; color: #e0e1dd;
                        padding: 1.5em; font-size: 0.85em; line-height: 1.6;
                        border-radius: 6px; box-shadow: 0 0 10px rgba(0,0,0,0.2);">
                {html_response}
            </div>
            """,
            unsafe_allow_html=True
        )

    if "sources" in st.session_state:
        st.markdown("#### 📎 Sources utilisées")
        st.markdown('<div style="font-size: 0.85em; margin-top: 1em;">', unsafe_allow_html=True)
        for i, src in enumerate(st.session_state.sources, 1):
            page = int(src["page"])
            text = src["text"].replace("\n", " ").strip()[:90] + "..."
            label = f"[{i}] : {text} (page {page})"
            if st.button(label, key=f"src_{i}"):
                st.session_state.current_page = page - 1
        st.markdown("</div>", unsafe_allow_html=True)

# ─── DROITE : visionneur PDF (inchangé) ───
with col_right:
    def display_pdf_page(doc, page_num):
        page = doc.load_page(page_num)
        zoom = 2.0
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        st.image(img, use_column_width=True)

    if not os.path.exists(PDF_PATH):
        st.error(f"📁 Fichier introuvable : {PDF_PATH}")
    else:
        doc = fitz.open(PDF_PATH)
        total_pages = len(doc)
        if 'current_page' not in st.session_state:
            st.session_state.current_page = 0

        c1, c2, c3 = st.columns([1, 2, 1])
        with c1:
            if st.button("◀", key="prev") and st.session_state.current_page > 0:
                st.session_state.current_page -= 1
        with c2:
            pg_num = st.number_input("Page", 1, total_pages,
                                     st.session_state.current_page + 1,
                                     key="page_input")
            st.session_state.current_page = pg_num - 1
        with c3:
            if st.button("▶", key="next") and st.session_state.current_page < total_pages - 1:
                st.session_state.current_page += 1

        st.caption(f"📄 Page {st.session_state.current_page + 1} / {total_pages}")
        display_pdf_page(doc, st.session_state.current_page)
        doc.close()
