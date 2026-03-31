from fastapi import APIRouter
from database import get_db_connection
from schemas import ChatRequest, ChatResponse
from services.openai_service import ask_model

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    reply_text = ask_model(request.message)

    conn = get_db_connection()    ## opens database connection
    cursor = conn.cursor()        ## sends database commands

    cursor.execute(
        "INSERT INTO messages (message, reply) VALUES (?, ?)",
        (request.message, reply_text)
    )

    conn.commit()
    conn.close()

    return {"reply": reply_text}


@router.get("/messages")
def get_messages():
    conn = get_db_connection()   
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM messages")    ## running SQL query
    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]   ##turns each SQLite row into a python dictionary