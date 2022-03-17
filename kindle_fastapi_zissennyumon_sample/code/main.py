from turtle import title
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel):
    title: str
    description: str
    published_at: Optional[bool]

@app.get('/')
def index():
    return {'data': {'name': 'Test'}}

@app.get('/about')
def about():
    return {'data': {'about page'}}

# 以下のURLでアクセスできる
# http://localhost:8081/test?limit=100?published=false
@app.get('/test')
def item(limit=10, published: bool=True):
    if published:
        return {'data': f'{limit}件'}
    else:
        return {'data': '非公開'}
    
@app.post('/blog')
def creata_blog(blog: Blog):
    return {'data': blog}