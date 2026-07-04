import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from langchain_core.messages import HumanMessage

from llm import ask_ai

# 🟢 Caches the embedding model in memory
@st.cache_resource
def get_embedding_model():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


def create_vector_db(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load() #Read and parse the file into a list of document pages
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100 #using overlap to prevent senetence breaking 
)
    chunks = text_splitter.split_documents(documents) #splits documents good for larger pdf's

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    ) #it calls the embedding models 

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="db"
    )
    return vector_db

def ask_pdf(question,vector_db,choice):
    retriever = vector_db.as_retriever(
        search_kwargs = {"k":3} #retriever helps chroma_db to search and retrieve info
    )
    results = retriever.invoke(question) #results contains the 3 most relevant Document chunks
    context = "\n\n".join(
    doc.page_content for doc in results)
    prompt = f"""
    Answer the question ONLY using the context below.
    If the answer is not found in the context,
    say:"I could not find this information in the uploaded PDF."
    Context:{context}
    Question:{question}
    """
    
    answer = ask_ai(
        choice,
        [HumanMessage(content=prompt)]
    )

    return answer
    #coverts chunks/documents into plain text understood by AI
#join is used to combine the 3 seperate chunks into one large context now llma can read it 
