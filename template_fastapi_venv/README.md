# 環境構築コマンド
python3 -m venv fastapi-env
source fastapi-env/bin/activate
  deactivate
pip install fastapi uvicorn


Makefileを作ったので、以下のコマンドでサーバーを起動できる
make start

# Swagger
http://localhost:8081
http://localhost:8081/redoc

# FastAPIについて
## パスパラメータの型を指定して受け取る
- 例：数値型で受け取る場合
@app.get('/blog/{id}')
def show(id:int):
  return {'data': id}

# docker起動
docker-compose up -d
docker-compose down


# 参考サイト
https://qiita.com/satto_sann/items/4fbc1a4e2b33fa2237d2

# 一番最初の環境構築時だけ実施
docker-compose exec db /bin/bash
mysql -u root -p
⇨ password
これでmysqlにアクセスできる

# MySQLにアクセス
docker-compose exec db /bin/bash
mysql -u user -h 127.0.0.1 -D sample_db -p

# docker立ち上げから停止まで
source fastapi-env/bin/activate
docker-compose up -d
http://localhost:8081
docker-compose down
deactivate