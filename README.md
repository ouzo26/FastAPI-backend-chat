A small backend chat application built with FastAPI, SQLite, and the OpenAI API.

This project accepts user messages through an API, generates AI responses, 
stores the user message and assistant reply in SQLite, and returns the reply as JSON.


- FastAPI backend
- Request and response validation with Pydantic
- SQLite database for storing messages
- OpenAI API integration for AI-generated replies
- Environment variable setup using `.env`
- Interactive API testing with FastAPI Swagger UI


API Endpoints

- `POST /chat` — send a message and receive an AI-generated reply
- `GET /messages` — retrieve saved messages from the database


things used so far : 

- Python
- FastAPI
- SQLite
- Pydantic
- OpenAI API
- python-dotenv
