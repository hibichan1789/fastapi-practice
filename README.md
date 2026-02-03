#python fastAPI練習

数値をクエリパラメータで送れるようにした
リストでも送れることを今日初めて知った
numpy配列のままではJSONを返せない、→.tolist()でリストに直す
ENV PYTHONUNBUFFERED=1 ←バッファを溜めずに出力するために使う

#コンテナの起動
docker compose up -d --build

#fastAPIのd動作をターミナルで確認
docker compose logs -f web

#swaggerの起動
http://localhost:8000/docs