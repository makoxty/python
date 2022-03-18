from fastapi import FastAPI
from blog_code.schemas import Blog
from blog_code.models import Base
from blog_code.database import engine

# テーブルを作成
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/blog")
def create(blog: Blog):
    return {"data": blog}
