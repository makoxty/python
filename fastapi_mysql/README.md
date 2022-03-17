# これは何のプロジェクト？
.venvを使わないテンプレート

# 参考サイト
https://qiita.com/satto_sann/items/4fbc1a4e2b33fa2237d2

# SWAGGER
http://localhost:8001/docs

# docker起動
docker-compose up -d
docker-compose down

# MySQLにアクセス
docker-compose exec db /bin/bash
mysql -u user -h 127.0.0.1 -D sample_db -p

# 一番最初の環境構築時だけ実施
docker-compose build
docker-compose exec db /bin/bash
mysql -u root -p
⇨ password
これでmysqlにアクセスできる

curl -X GET "http://localhost:8001/users" -H "accept: application/json"

# M1MacのDocker×MySQLの環境構築ではまるところ
https://qiita.com/yamagen0915/items/e84ae95066add052d15b