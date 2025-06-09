from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from bson import ObjectId

app = FastAPI()

# Conectare la MongoDB pentru taguri (port 27019)
client = MongoClient("mongodb://mongo-tags:27017/")
db = client["tags_db"]
tags_collection = db["tags"]

class Tag(BaseModel):
    note_id: str
    tag: str

@app.post("/tag")
def add_tag(tag_data: Tag):
    tags_collection.insert_one(tag_data.dict())
    return {"message": "Tag added"}

@app.get("/tags/{note_id}")
def get_tags(note_id: str):
    tags = list(tags_collection.find({"note_id": note_id}))
    for tag in tags:
        tag["_id"] = str(tag["_id"])
    return tags
