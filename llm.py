from dotenv import load_dotenv
import os 
import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
from prompts import (
    STUDY_PROMPT,
    INTERVIEW_PROMPT,
    QUIZ_PROMPT,
    CODING_PROMPT
)

load_dotenv()

api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# 🟢 Caches the heavy API connection setup
@st.cache_resource
def get_llm_model():
    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
        task="text-generation",
        huggingfacehub_api_token=api_key
    )
    return ChatHuggingFace(llm=llm)

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=api_key
)

model = ChatHuggingFace(llm=llm)

def ask_ai(choice, messages):
    
    if choice == "study":
        system_prompt = STUDY_PROMPT
    elif choice == "coding":
        system_prompt = CODING_PROMPT
    elif choice == "interview":
        system_prompt = INTERVIEW_PROMPT
    elif choice == "quiz":
        system_prompt = QUIZ_PROMPT
        
    final_messages = [SystemMessage(content = system_prompt)] + messages
    response = model.invoke(final_messages) #ai answer is stored in response
    return response.content #returns AI text back to streamlit_app.py

#Imp working

#st.session_state.messages → remembers what to display in the Streamlit interface.
#conversation → remembers what to send to the AI model so it has conversational context.
