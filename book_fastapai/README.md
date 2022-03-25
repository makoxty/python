# 環境構築コマンド
python3 -m venv fastapi-env
source fastapi-env/bin/activate
  deactivate
pip3 install fastapi uvicorn
pip3 install passlib bcrypt

# Table作成
python3 code/blog/createdb.py


# docker立ち上げから停止まで
source fastapi-env/bin/activate
docker-compose up
make start
http://localhost:8081
docker-compose down
deactivate

# Swagger
http://localhost:8081
http://localhost:8081/redoc

# docker起動
docker-compose up -d
docker-compose down

# DBeaver
以下のサイトよりダウンロードし、blog.dbを指定する
https://dbeaver.io/download/

pipコマンドはpip3

89