# 🚀 Enterprise Multi-Agent Document Intelligence Platform

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-Production-green.svg)]()
[![LangGraph](https://img.shields.io/badge/LangGraph-Agentic_AI-orange.svg)]()
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue.svg)]()
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-success.svg)]()
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)]()

## 📖 Overview

Enterprise Multi-Agent Document Intelligence Platform is a production-oriented Agentic AI solution designed to process, understand, and reason over enterprise documents using Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), OCR, Vector Search, and Multi-Agent orchestration.

The platform automates document ingestion, OCR extraction, semantic indexing, knowledge retrieval, summarization, validation, and question answering through autonomous AI agents coordinated using LangGraph workflows.

This project demonstrates modern AI engineering practices including:

* Multi-Agent Systems
* Agentic AI Workflows
* Retrieval-Augmented Generation (RAG)
* Document Intelligence
* OCR Pipelines
* FastAPI Microservices
* Vector Databases
* Cloud-Ready Deployment
* CI/CD Automation

---

## 🎯 Key Features

### 🤖 Multi-Agent Architecture

Specialized agents collaborate to complete document processing tasks:

| Agent             | Responsibility                      |
| ----------------- | ----------------------------------- |
| OCR Agent         | Extract text from scanned documents |
| Extraction Agent  | Extract structured information      |
| Validation Agent  | Verify extracted content            |
| Summary Agent     | Generate executive summaries        |
| RAG Agent         | Retrieve contextual knowledge       |
| Coordinator Agent | Manage agent orchestration          |

---

### 📄 Intelligent Document Processing

Supported document types:

* Invoices
* Contracts
* Purchase Orders
* Legal Documents
* Resumes
* Research Papers
* Financial Reports
* Scanned PDFs

---

### 🔍 Retrieval-Augmented Generation (RAG)

Capabilities:

* Semantic Search
* Knowledge Retrieval
* Context-Aware Question Answering
* Enterprise Knowledge Base
* Vector Similarity Search
* Embedding Management

---

### 🧠 Agentic Workflow with LangGraph

Workflow Pipeline:

```text
Document Upload
        │
        ▼
 OCR Agent
        │
        ▼
 Extraction Agent
        │
        ▼
 Validation Agent
        │
        ▼
 Embedding Agent
        │
        ▼
 Vector Storage
        │
        ▼
 Summary Agent
        │
        ▼
 Query & RAG Agent
        │
        ▼
 Final Response
```

---

## 🏗️ Architecture

```text
                    ┌─────────────────┐
                    │   User Upload   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    FastAPI      │
                    └────────┬────────┘
                             │
               ┌─────────────┴─────────────┐
               ▼                           ▼

      ┌────────────────┐        ┌─────────────────┐
      │ OCR Processing │        │ Document Parser │
      └────────────────┘        └─────────────────┘
               │                           │
               └─────────────┬─────────────┘
                             ▼

                  ┌────────────────────┐
                  │ Multi-Agent Layer  │
                  └────────────────────┘
                             │
                             ▼

                 ┌─────────────────────┐
                 │ LangGraph Workflow  │
                 └─────────────────────┘
                             │
                             ▼

                 ┌─────────────────────┐
                 │ Embeddings Engine   │
                 └─────────────────────┘
                             │
                             ▼

                 ┌─────────────────────┐
                 │     ChromaDB        │
                 └─────────────────────┘
                             │
                             ▼

                 ┌─────────────────────┐
                 │   RAG Questioning   │
                 └─────────────────────┘
```

---

## 🛠️ Technology Stack

### Backend

* Python 3.12+
* FastAPI
* SQLAlchemy
* Pydantic

### AI / LLM

* OpenAI
* Azure OpenAI
* LangChain
* LangGraph

### RAG & Vector Search

* ChromaDB
* OpenAI Embeddings

### OCR

* Tesseract OCR
* PyMuPDF

### Database

* PostgreSQL

### DevOps

* Docker
* Docker Compose
* GitHub Actions

### Testing

* Pytest

---

## 📂 Project Structure

```text
ocr-agentic-ai/

├── api/
├── agents/
├── graph/
├── rag/
├── services/
├── db/
├── models/
├── schemas/
├── prompts/
├── utils/
├── uploads/
├── tests/
│
├── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Siva-Dev-001/ocr-agentic-ai.git

cd ocr-agentic-ai
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create `.env`

```env
OPENAI_API_KEY=

AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_KEY=
AZURE_DEPLOYMENT_NAME=

DATABASE_URL=postgresql://postgres:postgres@localhost/agentic_ai
```

---

## ▶️ Run Application

```bash
uvicorn main:app --reload
```

Access API:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

Redoc:

```text
http://localhost:8000/redoc
```

---

## 🐳 Docker Deployment

Build:

```bash
docker build -t ocr-agentic-ai .
```

Run:

```bash
docker-compose up --build
```

---

## 📡 API Endpoints

### Upload Document

```http
POST /upload
```

Upload PDF documents for processing.

---

### Ask Questions

```http
POST /ask
```

Example:

```json
{
  "question": "What is the invoice total amount?"
}
```

---

### Health Check

```http
GET /health
```

---

## 📈 Future Enhancements

* Azure AI Document Intelligence Integration
* Multi-Modal Agents
* MongoDB Vector Search
* Semantic Caching
* Agent Memory
* Autonomous Tool Calling
* Human-in-the-Loop Validation
* Kubernetes Deployment
* Observability with OpenTelemetry
* Agent Evaluation Framework

---

## 💼 Skills Demonstrated

### Artificial Intelligence

* Agentic AI
* Multi-Agent Systems
* LLM Orchestration
* Prompt Engineering
* RAG

### Backend Engineering

* Python
* FastAPI
* REST APIs
* SQLAlchemy

### Data Engineering

* PostgreSQL
* Vector Databases
* Embeddings

### Cloud & DevOps

* Docker
* CI/CD
* GitHub Actions
* Azure OpenAI

### Enterprise Architecture

* Service Layer Design
* Agent Coordination
* Workflow Orchestration
* Scalable API Development

---

## 📊 Business Value

This platform reduces manual document processing effort by automating:

* Data Extraction
* Information Validation
* Knowledge Retrieval
* Document Summarization
* Question Answering
* Enterprise Search

Organizations can leverage this solution to accelerate document workflows, improve accuracy, and unlock insights from unstructured data.

---

## 👨‍💻 Author

**Python Full Stack & AI Developer**

Specializations:

* Django & FastAPI
* Agentic AI
* LangGraph
* LangChain
* Azure OpenAI
* RAG Systems
* Vector Databases
* Cloud Deployments
* Enterprise Automation

---

## ⭐ Support

If you find this project useful:

* Star the repository
* Fork the project
* Create issues for improvements
* Submit pull requests

Contributions are welcome.
