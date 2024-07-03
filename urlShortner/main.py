import shortlink
from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class short(BaseModel):
    link:str
@app.post("/")
def root(link:short):
    URL=shortlink.short(link.link)
    return {"result":URL}