https://zenn.dev/sh0nk/books/537bb028709ab9/viewer/281ee0
# 環境構築
- docker-compose build
- docker-compose run --entrypoint "poetry init --name demo-app --dependency fastapi --dependency uvicorn[standard]" demo-app
※ Authorのパートのみnを入力
他はEnter
- docker-compose run --entrypoint "poetry install" demo-app

- Swagger
http://localhost:8000/docs

- MySQLへの接続コマンド
  - docker-compose upしてれば接続できる
docker-compose exec db mysql demo

- dockerを立ち上げた状態で以下のコマンドを実施
docker-compose exec demo-app poetry add sqlalchemy aiomysql

- api モジュールの migrate_db スクリプトを実行する
docker-compose exec demo-app poetry run python -m api.migrate_db

docker-compose exec db mysql demo
SHOW TABLES;
DESCRIBE tasks;
DESCRIBE dones;

docker-compose ps
docker-compose up -d
docker-compose down