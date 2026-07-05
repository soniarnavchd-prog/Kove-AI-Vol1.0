"""
Kove AI Vol-1
Copyright (c) 2026 Arnav Soni

This source code is provided for viewing only.
Copying, redistribution, or commercial use without permission is prohibited.
"""
import streamlit as st
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.messages import HumanMessage
from llm import ask_ai

@st.cache_resource
def get_embedding_model():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
def create_vector_db(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load() 
    
    text_splitter = RecursiveCharacterTextSplitter(   #used to split long pages into small chunks.
        chunk_size=500,
        chunk_overlap=100  #keeps 100 char from previous chunks 
    )
    chunks = text_splitter.split_documents(documents)
    embedding_model = get_embedding_model()

    vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="db")
    return vector_db

def ask_pdf(question, vector_db, choice):
    retriever = vector_db.as_retriever(search_kwargs={"k": 3}) #converts db into search engine and k= 3 means takes only 3 relevant tokens 
    results = retriever.invoke(question) 
    context = "\n\n".join(doc.page_content for doc in results) #Combines all retrieved chunks into one long string.
    
    prompt = f"""
    Answer the question ONLY using the context below.
    If the answer is not found in the context,
    say:"I could not find this information in the uploaded PDF." 
    Context:{context}
    Question:{question} 
    """
    return ask_ai(choice, [HumanMessage(content=prompt)]) #sends context and question to llama
