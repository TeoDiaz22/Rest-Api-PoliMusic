from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
import dataAccess
import json

app = FastAPI()

class Song(BaseModel):
    id: int = 0
    name: str
    path: str
    plays: int = 0

@app.get("/song/get")
def get_songs():
    songs = dataAccess.get_songs()
    return songs

@app.post("/song/add")
def add_song(song: Song):
    dataAccess.add_song(song)
    return {"result": "Song added successfully."}

@app.patch("/song/update")
def update_song(song: Song):
    dataAccess.update_song(song)
    return {"result": "Song updated successfully."}

@app.delete("/song/delete")
def delete_song(song_id: int):
    dataAccess.delete_song(song_id)
    return {"result": "Song deleted successfully."}