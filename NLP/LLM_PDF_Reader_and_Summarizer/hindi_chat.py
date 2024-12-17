import streamlit as st
import PyPDF2
from transformers import pipeline, DistilBertTokenizer, DistilBertForQuestionAnswering
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
import torch
import base64
from docx import Document
import os

# Constants
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# Load QA model and tokenizer
qa_model = pipeline("question-answering",
                    model="distilbert-base-uncased-distilled-squad")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Function to extract text from PDF


def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfFileReader(file)
    text = ""
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extract_text()
    return text

# Function to extract text from Word document


def extract_text_from_word(filepath):
    doc = Document(filepath)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

# Function to split text into chunks


def split_text(text, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = text_splitter.split_text(text)
    return chunks

# Function to extract key points and structure slides


def generate_slides_content(text):
    chunks = split_text(text)
    slides_content = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=150,
                             min_length=30, do_sample=False)
        slides_content.append(summary[0]['summary_text'])
    return slides_content


# Streamlit chat interface
st.title("Hindi Document Chat Interface")

uploaded_file = st.file_uploader(
    "Upload a PDF or DOCX file", type=["pdf", "docx"])

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        text = extract_text_from_pdf(uploaded_file)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        filepath = os.path.join("data", uploaded_file.name)
        with open(filepath, "wb") as f:
            f.write(uploaded_file.read())
        text = extract_text_from_word(filepath)

    st.text_area("Extracted Text", text, height=300)

    st.header("Generate Slides Content")
    if st.button("Generate Slides"):
        slides_content = generate_slides_content(text)
        for i, slide in enumerate(slides_content):
            st.markdown(f"### Slide {i+1}")
            st.write(slide)
