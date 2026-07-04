# Kove-AI-Vol1.0
🤖 Kove AI: A multi-mode personal learning mentor built with Streamlit and LangChain, featuring personalized study roadmaps, interactive coding challenges, mock interviews, quizzes, and PDF RAG capabilities.
# 🤖 KOVE AI | Your Professional AI Learning Tutor

Kove AI is an intelligent, multi-mode learning assistant designed to guide students and professionals through customized educational roadmaps, mock interview training, dynamic quiz sessions, and code mentoring. It features an integrated RAG (Retrieval-Augmented Generation) pipeline allowing users to upload custom PDFs and query them seamlessly using specific mentor personas.

---

## ✨ Features

* **📚 Study Mentor:** Adapts explanations to your level (School, College, Professional) and auto-generates personalized learning roadmaps.
* **💻 Coding Mentor:** Provides conceptual deep-dives, code walk-throughs, dry runs, and interactive challenges.
* **🎤 Interview Coach:** Conducts realistic, conversational technical mock interviews, providing custom feedback and scoring out of 10.
* **📝 Quiz Generator:** Generates custom multi-format quizzes (MCQs, T/F, Fill-in-the-blanks) based on your selected topic.
* **📄 PDF Retrieval-Augmented Generation (RAG):** Upload any PDF document to chat directly with your selected AI mentor mode using your document's contexts.

---

## 🛠️ Tech Stack

* **Frontend UI:** Streamlit
* **LLM Orchestration:** LangChain (LangChain Core & Community)
* **Inference Model:** Meta-Llama-3-8B-Instruct (via Hugging Face Endpoint)
* **Embeddings:** `sentence-transformers/all-MiniLM-L6-v2`
* **Vector Database:** ChromaDB
* **PDF Parsing:** PyPDF

---

## 🚀 Local Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
   cd YOUR_REPO_NAME
