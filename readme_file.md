                   Enterprise AI Knowledge Assistant (AWS + RAG + LLM)

Problem Statement - Companies have thousands of documents and cannot search them efficiently.
Solution - An AI system where users upload documents and ask questions to get instant answers.

An end-to-end AI-powered Retrieval-Augmented Generation (RAG) system built with FastAPI, FAISS, and LLM integration.
This system allows users to upload documents (PDF, TXT, JSON, etc.) and interact with them using natural language queries.


Architecture
 - AWS EC2 Deployment
 - S3 for Document Storage
 - FastAPI Backend
 - Vector Search (FAISS)
 - LLM via OpenRouter
 - Gradio UI for interaction

Features
 - Upload files & folders (PDF, TXT, JSON, CSV, MD)
 - Intelligent document chunking with overlap
 - Embedding-based semantic search
 -  Fast retrieval using FAISS
 - Top-K retrieval + reranking
 - Cleaned and structured answers
 - Deployed on AWS (public access)
 - Chat interface for document Q&A

How It Works
 Document Upload
  - Files uploaded via UI → stored in AWS S3
 Chunking
  - Text split into overlapping chunks
 Embedding
  - Each chunk converted into vector embeddings
 Vector Storage
  - Stored in FAISS index
 Query Processing
  - User query → converted to embedding
 Retrieval
  - Top-K relevant chunks fetched
 LLM Generation
  - Context + query → passed to LLM
  - Final answer generated

Tech Stack
 - Backend: FastAPI
 - Frontend: Gradio
 - Vector DB: FAISS
 - Cloud: AWS EC2 + S3
 - LLM: OpenRouter (LLaMA 3)
 - Embeddings: Sentence Transformers

Setup Instructions
1 Clone Repo
 - git clone https://github.com/arun184527/enterprise-ai-system.git
cd enterprise-ai-system
2️ Create Virtual Environment
 - python -m venv venv
 - source venv/bin/activate   # Linux
 - venv\Scripts\activate      # Windows
3️ Install Dependencies
 - pip install -r requirements.txt
4️ Set API Key
 - export OPENROUTER_API_KEY="your_api_key"
5️ Run Backend
 - uvicorn app.main:app --host 0.0.0.0 --port 8000
6️ Run UI
 - python ui.py

Deployment (AWS)
 - EC2 instance used for hosting backend & UI
 - Security group ports opened:
 - 8000 → FastAPI
 - 7860 → UI
 - S3 used for document storage

Limitations
 - t3.micro (1GB RAM) may crash under load
 - Recommended: t3.small or higher

Future Improvements
 - Persistent vector DB (ChromaDB / Pinecone)
 - Authentication system
 - Multi-user support
 - Streaming responses
 - Docker + CI/CD pipeline
 - Domain + HTTPS

Key Learnings
 - Real-world RAG pipeline design
 - AWS deployment & debugging
 - Memory optimization challenges
 - LLM integration via APIs
 - End-to-end system architecture

 Author
 Arun Ghatage
     Aspiring AI/ML Engineer