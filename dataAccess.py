import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import select
from sqlalchemy import MetaData
from sqlalchemy import insert

load_dotenv()

engine = create_engine("mssql+pyodbc://"+os.getenv('USER_DB')+":"+os.getenv('PASS_DB')+"@"+os.getenv('HOST_DB')+":"+os.getenv('PORT_DB')+"/"+os.getenv('DB_NAME')+"?driver=ODBC+Driver+17+for+SQL+Server")
metadata_obj = MetaData()

song_table = Table(
    "TBL_SONG",
    metadata_obj,
    Column("ID_SONG", Integer, primary_key=True),
    Column("SONG_NAME",String),
    Column("SONG_PATH",String),
    Column("PLAYS",Integer),
)
  
def get_songs():
    stmt = select(song_table)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        return result.fetchall()
    return [] 

def add_song(song):
    with engine.connect() as conn:
        conn.execute(song_table.insert().values(
            SONG_NAME=song.name,
            SONG_PATH=song.path,
            PLAYS=song.plays
        ))
        
def update_song(song):
    with engine.connect() as conn:
        conn.execute(song_table.update().where(song_table.c.ID_SONG == song.id).values(
            SONG_NAME=song.name,
            SONG_PATH=song.path,
            PLAYS=song.plays
        ))

def delete_song(song_id):
    with engine.connect() as conn:
        conn.execute(song_table.delete().where(song_table.c.ID_SONG == song_id))
        