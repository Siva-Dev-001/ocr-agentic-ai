from fastapi import APIRouter

from agents.rag_agent import RAGAgent

router = APIRouter()


@router.post("/ask")
def ask(question: str):

    response = RAGAgent().run(
        question
    )

    return {
        "answer": response
    }