from blog_code.models import Base
from blog_code.database import engine, SessionLocal

# テーブルを作成
Base.metadata.create_all(bind=engine)
# checkfirst=False とするとテーブルを再作成してくれる
# Base.metadata.create_all(bind=engine, checkfirst=False)
