#python fastAPI練習

#コンテナの起動
docker compose up -d --build

#fastAPIのd動作をターミナルで確認
docker compose logs -f web

#swaggerの起動
http://localhost:8000/docs

#学習メモ
・ENV PYTHONUNBUFFERED=1 ←バッファを溜めずに出力するために使う
・リクエストボディの"text"をtextに格納してJSONとして外部のファイル(app/data/message.json)に保存した
・ログを定義してみてコンソール出力できるようにした
・asynccontextmanagerをつかって起動時の処理を行うようにした、起動時に保存用のディレクトリの作成を行った
・HTTPExceptionやstatus_codeでエラーハンドリング、ステータスコードを管理した