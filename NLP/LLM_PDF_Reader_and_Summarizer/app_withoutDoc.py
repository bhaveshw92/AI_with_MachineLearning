import streamlit as st
import PyPDF2
from transformers import pipeline
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
import base64

# Define the function to extract text from PDF


def extract_text_from_pdf(pdf_file_path):
    with open(pdf_file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text_list = []
        for page_number in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]
            text = page.extract_text()
            text_list.append(text)
        full_text = '\n'.join(text_list)
        return full_text


# model and tokenizer loading
checkpoint = "LaMini-Flan-T5-248M"
tokenizer = T5Tokenizer.from_pretrained(checkpoint)
base_model = T5ForConditionalGeneration.from_pretrained(
    checkpoint, device_map='auto', torch_dtype=torch.float32)

# file loader and preprocessing


def file_preprocessing(file):
    loader = PyPDFLoader(file)
    pages = loader.load_and_split()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200, chunk_overlap=50)
    texts = text_splitter.split_documents(pages)
    final_texts = ""
    for text in texts:
        print(text)
        final_texts = final_texts + text.page_content
    return final_texts

# LLM pipeline


def llm_pipeline(filepath):
    pipe_sum = pipeline(
        'summarization',
        model=base_model,
        tokenizer=tokenizer,
        max_length=500,
        min_length=150)
    input_text = file_preprocessing(filepath)
    result = pipe_sum(input_text)
    result = result[0]['summary_text']
    return result


@st.cache_data
# function to display the PDF of a given file
def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)


# streamlit code
st.set_page_config(layout="wide")


summarizer = pipeline(
    'summarization',
    model=base_model,
    tokenizer=tokenizer,
    max_length=500,
    min_length=150)


# Streamlit app
def main():
    st.title("📄Document Summarization App using LaMini-Flan-T5-248M Langauge Model with PDF, TXT File and Textfield!")

    # Initialize text as an empty string
    text = ""

    # Radio buttons for input selection
    choice = st.radio("Select Input Method:",
                      ("PDF", "Text File", "Write Text"))

    if choice == "PDF":
        # File uploader for PDF files
        uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

        if uploaded_file:
            if st.button("Summarize"):
                col1, col2 = st.columns(2)
                filepath = "data/"+uploaded_file.name
                # Save the uploaded file to a temporary location
                with open("temp_file.pdf", "wb") as f:
                    f.write(uploaded_file.read())  # .get_value()

                with col1:
                    st.info("Uploaded File")
                    pdf_view = displayPDF(filepath)

                with col2:
                    summary = llm_pipeline(filepath)
                    st.info("Summarization Complete")
                    st.success(summary)

    elif choice == "Text File":
        uploaded_file = st.file_uploader("Choose a text file", type="txt")
        if uploaded_file is not None:
            if st.button("Summarize"):
                col1, col2 = st.columns(2)
                text = uploaded_file.read().decode("utf-8")
                # Display the original text (optional)
                with col1:
                    st.header("Original Text")
                    st.write(text)
                with col2:
                    # Summarize the text
                    summary = summarizer(
                        text, max_length=500, min_length=50, do_sample=False)
                    final_summary = summary[0]['summary_text']

                    st.info("Summarization Complete")
                    st.success(final_summary)

    elif choice == "Write Text":
        text = st.text_area("Enter your text here:")
        if st.button("Summarize"):
            col1, col2 = st.columns(2)
            # Display the original text
            with col1:
                st.header("Original Text")
                st.write(text)
            with col2:
                # Summarize the text
                summary = summarizer(text, max_length=500,
                                     min_length=50, do_sample=False)
                final_summary = summary[0]['summary_text']

                st.info("Summarization Complete")
                st.success(final_summary)


# Run the Streamlit app
if __name__ == "__main__":
    main()
