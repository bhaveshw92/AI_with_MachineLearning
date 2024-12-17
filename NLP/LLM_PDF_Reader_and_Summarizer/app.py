import streamlit as st
import PyPDF2
from transformers import pipeline, T5Tokenizer, T5ForConditionalGeneration
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
import torch
import base64
from docx import Document
import os

# Constants
CHECKPOINT = "LaMini-Flan-T5-248M"
CHUNK_SIZE = 200
CHUNK_OVERLAP = 50
MAX_SUMMARY_LENGTH = 500
MIN_SUMMARY_LENGTH = 150

# Load model and tokenizer
tokenizer = T5Tokenizer.from_pretrained(CHECKPOINT)
base_model = T5ForConditionalGeneration.from_pretrained(
    CHECKPOINT, device_map='auto', torch_dtype=torch.float32)

# Summarizer pipeline
summarizer = pipeline(
    'summarization',
    model=base_model,
    tokenizer=tokenizer,
    max_length=MAX_SUMMARY_LENGTH,
    min_length=MIN_SUMMARY_LENGTH
)

# Define the function to extract text from PDF


def extract_text_from_pdf(pdf_file_path):
    with open(pdf_file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text_list = [page.extract_text() for page in pdf_reader.pages]
    return '\n'.join(text_list)

# File loader and preprocessing


def file_preprocessing(file):
    loader = PyPDFLoader(file)
    pages = loader.load_and_split()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    texts = text_splitter.split_documents(pages)
    return "".join(text.page_content for text in texts)

# LLM pipeline


def llm_pipeline(filepath):
    input_text = file_preprocessing(filepath)
    result = summarizer(input_text)
    return result[0]['summary_text']


@st.cache_data
def displayPDF(file):
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# Define the function to extract text from Word files


def extract_text_from_word(word_file_path):
    doc = Document(word_file_path)
    return "\n".join(paragraph.text for paragraph in doc.paragraphs)

# Streamlit app


def main():
    st.set_page_config(layout="wide")
    st.title("📄Document Summarization App using LaMini-Flan-T5-248M Language Model with PDF, Word Doc, TXT File and Textfield!")

    choice = st.radio("Select Input Method:",
                      ("PDF", "Word File", "Text File", "Write Text"))

    if choice == "PDF":
        uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
        if uploaded_file and st.button("Summarize"):
            col1, col2 = st.columns(2)
            filepath = os.path.join("data", uploaded_file.name)
            with open(filepath, "wb") as f:
                f.write(uploaded_file.read())
            with col1:
                st.info("Uploaded File")
                displayPDF(filepath)
            with col2:
                summary = llm_pipeline(filepath)
                st.info("Summarization Complete")
                st.success(summary)

    elif choice == "Text File":
        uploaded_file = st.file_uploader("Choose a text file", type="txt")
        if uploaded_file and st.button("Summarize"):
            col1, col2 = st.columns(2)
            text = uploaded_file.read().decode("utf-8")
            with col1:
                st.header("Original Text")
                st.write(text)
            with col2:
                summary = summarizer(
                    text, max_length=MAX_SUMMARY_LENGTH, min_length=MIN_SUMMARY_LENGTH, do_sample=False)
                st.info("Summarization Complete")
                st.success(summary[0]['summary_text'])

    elif choice == "Write Text":
        text = st.text_area("Enter your text here:")
        if st.button("Summarize"):
            col1, col2 = st.columns(2)
            with col1:
                st.header("Original Text")
                st.write(text)
            with col2:
                summary = summarizer(
                    text, max_length=MAX_SUMMARY_LENGTH, min_length=MIN_SUMMARY_LENGTH, do_sample=False)
                st.info("Summarization Complete")
                st.success(summary[0]['summary_text'])

    elif choice == "Word File":
        uploaded_file = st.file_uploader("Choose a Word file", type="docx")
        if uploaded_file and st.button("Summarize"):
            col1, col2 = st.columns(2)
            filepath = os.path.join("data", uploaded_file.name)
            with open(filepath, "wb") as f:
                f.write(uploaded_file.read())
            text = extract_text_from_word(filepath)
            with col1:
                st.header("Original Text")
                st.write(text)
            with col2:
                summary = summarizer(
                    text, max_length=MAX_SUMMARY_LENGTH, min_length=MIN_SUMMARY_LENGTH, do_sample=False)
                st.info("Summarization Complete")
                st.success(summary[0]['summary_text'])


if __name__ == "__main__":
    main()
