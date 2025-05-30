import streamlit as st
from summarizer import summarize_text
from utils import extract_pdf_text, extract_docx_text, extract_txt_text

st.set_page_config(page_title="Text Summarizer", page_icon="📄")

st.title("📄 Multi-Page Text Summarizer")
st.write("Upload a text, PDF, or DOCX file and get a concise AI-generated summary.")

uploaded_file = st.file_uploader("Upload your file (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    if uploaded_file.name.endswith(".pdf"):
        raw_text = extract_pdf_text(uploaded_file)
    elif uploaded_file.name.endswith(".docx"):
        raw_text = extract_docx_text(uploaded_file)
    elif uploaded_file.name.endswith(".txt"):
        raw_text = extract_txt_text(uploaded_file)
    else:
        st.error("Unsupported file format")

    st.subheader("📖 Original Text:")
    st.write(raw_text)

    if st.button("✨ Generate Summary"):
        with st.spinner("Generating summary..."):
            summary = summarize_text(raw_text)
        st.subheader("📝 AI-generated Summary:")
        st.write(summary)
