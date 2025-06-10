from fastapi import FastAPI, Request
from pydantic import BaseModel
import httpx
import os
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # sau ["http://localhost:8081"] dacă vrei să limitezi
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Note(BaseModel):
    title: str
    content: str
    user_id: str

# Baze URL pentru microservicii


USER_SERVICE_URL = os.getenv("USER_SERVICE_URL")
NOTE_SERVICE_URL = os.getenv("NOTE_SERVICE_URL")
TAG_SERVICE_URL = os.getenv("TAG_SERVICE_URL")
print("USER_SERVICE_URL =", USER_SERVICE_URL)
class User(BaseModel):
    username: str
    password: str

@app.post("/api/register")
async def register(user: User):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{USER_SERVICE_URL}/register", json=user.model_dump())
    return response.json()

class User(BaseModel):
    username: str
    password: str

@app.post("/api/login")
async def login(user: User):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{USER_SERVICE_URL}/login", json=user.dict())
    return response.json()


@app.post("/api/note")
async def create_note(note: Note):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{NOTE_SERVICE_URL}/note", json=note.dict())
    return response.json()

@app.get("/api/notes/{user_id}")
async def get_notes(user_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{NOTE_SERVICE_URL}/notes/{user_id}")
    return response.json()

@app.delete("/api/note/{note_id}")
async def delete_note(note_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{NOTE_SERVICE_URL}/note/{note_id}")
    return response.json()

class Tag(BaseModel):
    note_id: str
    tag: str

@app.post("/api/tag")
async def add_tag(tag: Tag):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{TAG_SERVICE_URL}/tag", json=tag.dict())
    return response.json()

@app.get("/api/tags/{note_id}")
async def get_tags(note_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{TAG_SERVICE_URL}/tags/{note_id}")
    return response.json()
