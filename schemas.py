from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(min_length=3, max_length=200)


class ChatResponse(BaseModel):
    reply: str