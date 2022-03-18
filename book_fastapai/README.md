# 環境構築コマンド
python3 -m venv fastapi-env
source fastapi-env/bin/activate
  deactivate
pip install fastapi uvicorn

# Swagger
http://localhost:8081
http://localhost:8081/redoc

# docker起動
docker-compose up -d
docker-compose down

# DBeaver
以下のサイトよりダウンロードし、blog.dbを指定する
https://dbeaver.io/download/

# docker立ち上げから停止まで
source fastapi-env/bin/activate
docker-compose up -d
make dev
http://localhost:8081
deactivate
docker-compose down

pipコマンドはpip3

参考書
45