"""
Kove AI Vol-1
Copyright (c) 2026 Arnav Soni

This source code is provided for viewing only.
Copying, redistribution, or commercial use without permission is prohibited.
"""
from dotenv import load_dotenv
import os 
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
from prompts import (
    COMMON_RULES,
    STUDY_PROMPT,
    INTERVIEW_PROMPT,
    QUIZ_PROMPT,
    CODING_PROMPT
)

load_dotenv()

api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=api_key
)  #creates connection with llama

model = ChatHuggingFace(llm=llm) #converts endpoint into chatmodel

def ask_ai(choice, messages):
    
    if choice == "study":
        system_prompt = STUDY_PROMPT
    elif choice == "coding":
        system_prompt = CODING_PROMPT
    elif choice == "interview":
        system_prompt = INTERVIEW_PROMPT
    elif choice == "quiz":
        system_prompt = QUIZ_PROMPT
        
    
    system_prompt = COMMON_RULES + "\n\n" + system_prompt    
    final_messages = [SystemMessage(content = system_prompt)] + messages
    response = model.invoke(final_messages) #ai answer is stored in response
    return response.content #returns AI text back to streamlit_app.py

#Imp working

#st.session_state.messages → remembers what to display in the Streamlit interface.
#conversation → remembers what to send to the AI model so it has conversational context.
