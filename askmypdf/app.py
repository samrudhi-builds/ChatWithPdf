import streamlit as st
from pdf_utils import extract_text_from_pdf
from rag_utils import split_text, add_chunks_to_chroma, query_gpt

st.set_page_config(page_title="AskMyPDF", layout="centered")
st.title("📄 AskMyPDF – Chat with your PDF!")

# Initialize session state
if 'pdf_processed' not in st.session_state:
    st.session_state['pdf_processed'] = False
if 'current_filename' not in st.session_state:
    st.session_state['current_filename'] = None

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    # Check if this is a new file or if we need to reprocess
    if (not st.session_state['pdf_processed'] or 
        st.session_state['current_filename'] != uploaded_file.name):
        
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())
        
        with st.spinner("Extracting text and processing PDF..."):
            text = extract_text_from_pdf("temp.pdf")
            chunks = split_text(text)
            add_chunks_to_chroma(chunks)
        
        st.session_state['pdf_processed'] = True
        st.session_state['current_filename'] = uploaded_file.name
        st.success("PDF uploaded and processed!")
    else:
        st.info(f"PDF '{uploaded_file.name}' is already processed. You can ask questions below.")

    question = st.text_input("❓ Ask a question about your PDF")
    if question:
        with st.spinner("Searching..."):
            answer = query_gpt(question)
        st.markdown("### 🧠 Answer:")
        st.write(answer)

# Reset button to allow reprocessing
if st.session_state['pdf_processed']:
    if st.button("🔄 Reset (Upload New PDF)"):
        st.session_state['pdf_processed'] = False
        st.session_state['current_filename'] = None
        st.rerun()
