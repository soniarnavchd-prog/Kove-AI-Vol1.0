import streamlit as st
from llm import ask_ai
from langchain_core.messages import HumanMessage, AIMessage
import time
from rag import create_vector_db, ask_pdf

def stream_response(text): # creates streaming animation 
    for word in text.split():
        yield word + " "
        time.sleep(0.05)

st.set_page_config(
    page_title = "Kove AI", # changes the chrome tab to kove Ai displayed on top
    page_icon = "🤖",
    layout = "wide"
)

if "messages" not in st.session_state:
    st.session_state.messages = []
    
if "roadmap_progress" not in st.session_state:
    st.session_state.roadmap_progress = []
    
if "vector_db" not in st.session_state:
    st.session_state.vector_db = None
#we added because st.session_state remenbers it so no db rebuilding 
if "current_pdf" not in st.session_state:
    st.session_state.current_pdf = None
    
st.title("🤖 Kove AI")

# -------------------------
# Show Previous Messages
# -------------------------
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"): 
            st.write(message.content)

# -------------------------
# Sidebar Layout
# -------------------------
with st.sidebar:
    st.title("✨ Kove Ai")
    st.caption("Your Personal AI Mentor for Python, ML & GenAI 🚀")
    st.markdown("---------")
    st.subheader("⚙️ Settings")
    st.success("🟢 Connected")
    st.info("🦙 Model: Llama 3")
    st.caption("Version 1.0")
    
    uploaded_file = st.file_uploader(
        "📄 Upload PDF",
        type = ["pdf"]
    )
    
if st.session_state.vector_db:
    st.success("📄 Using uploaded PDF")
    
if st.button("❌ Remove PDF"):
    st.session_state.vector_db = None
    st.session_state.current_pdf = None
    st.success("PDF Removed!")

    st.rerun()
    
if uploaded_file:
    if st.session_state.current_pdf != uploaded_file.name:
        with open("uploaded.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner("📚 Reading PDF..."):
            st.session_state.vector_db = create_vector_db("uploaded.pdf")

        st.session_state.current_pdf = uploaded_file.name

        st.success("✅ PDF Loaded Successfully!")

# -------------------------
# Mode Selection & Main Chat
# -------------------------
mode = st.selectbox(
    "Choose Mode",
    [
        "📚 Study Mentor",
        "💻 Coding Mentor",
        "🎤 Interview Coach",
        "📝 Quiz Generator"
    ]
)

# 🟢 4. Fixed map keys to perfectly match the selectbox strings exactly
mode_map = {
    "📚 Study Mentor": "study",
    "💻 Coding Mentor": "coding",
    "🎤 Interview Coach": "interview",
    "📝 Quiz Generator": "quiz"
}

choice = mode_map[mode]

question = st.chat_input("Ask me anything...")

if question:
    with st.chat_message("user"):
        st.write(question)

    st.session_state.messages.append(HumanMessage(content = question))

    if st.session_state.vector_db:
        answer = ask_pdf(
        question,
        st.session_state.vector_db,
        choice
        )
    else:
        answer = ask_ai(
        choice,
        st.session_state.messages
        )
    
    with st.chat_message("assistant"):
        full_reponse = st.write_stream(stream_response(answer))
        
    st.session_state.messages.append(AIMessage(content = full_reponse))
    
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun() # it tells streamlit to run the whole app again like refresh in google 
