import re
from typing import List
from fastapi import FastAPI, Depends
from .routes import blog, user, auth

# Docker用
from .blog_code.schemas import Blog, ShowBlog, User, ShowUser
from .blog_code.models import Base
from .blog_code.hashing import Hash
from .blog_code import models
from .blog_code.database import engine, SessionLocal, get_db

# python3コマンド実行用
# from blog_code.schemas import Blog, ShowBlog, User, ShowUser
# from blog_code.models import Base
# from blog_code import models
# from blog_code.hashing import Hash
# from blog_code.database import engine, SessionLocal

app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)
