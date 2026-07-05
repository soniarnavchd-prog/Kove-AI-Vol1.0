import streamlit as st
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.messages import HumanMessage
from llm import ask_ai

@st.cache_resource
def get_embedding_model():
    api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    return HuggingFaceInferenceAPIEmbeddings(
        api_key=api_key,
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

def create_vector_db(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load() 
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100 
    )
    chunks = text_splitter.split_documents(documents)
    embedding_model = get_embedding_model()

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model
    )
    return vector_db

def ask_pdf(question, vector_db, choice):
    retriever = vector_db.as_retriever(search_kwargs={"k": 3})
    results = retriever.invoke(question) 
    context = "\n\n".join(doc.page_content for doc in results)
    
    prompt = f"""
    Answer the question ONLY using the context below.
    If the answer is not found in the context,
    say:"I could not find this information in the uploaded PDF."
    Context:{context}
    Question:{question}
    """
    return ask_ai(choice, prompt)