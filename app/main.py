from fastapi import FastAPI, Body, HTTPException, Path
from contextlib import asynccontextmanager
import os
import logging
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATADIRNAME = "app/data"
DATAFILENAME = "messages.json"
DATAFILEPATH = os.path.join(DATADIRNAME, DATAFILENAME)
@asynccontextmanager
async def lifespan(app:FastAPI):
    logger.info("アプリを起動中")
    os.makedirs(DATADIRNAME, exist_ok=True)
    yield


app = FastAPI(lifespan=lifespan)

@app.post("/messages", description="メッセージを保存する", status_code=201)
def save_messages(text: str = Body(..., embed=True)):
    logger.info("/messages POSTが呼ばれました")
    logger.info(f"text: {text}")
    messages = []
    logger.info(f"{DATAFILEPATH}が存在するか確認します")
    if os.path.exists(DATAFILEPATH):
        logger.info(f"{DATAFILEPATH}が存在したため読み込みます")
        with open(DATAFILEPATH, "r") as f:
            messages = json.load(f)
    messages.append(text)
    logger.info(f"messages: {messages}")
    logger.info(f"{DATAFILEPATH}に書き込みをします")
    with open(DATAFILEPATH, "w") as f:
        json.dump(messages, f, indent=4)
    logger.info("書き込みが完了しました")
    return {
        "message": "saved",
        "total_messages": len(messages)
        }

@app.get("/messages", description="保存されたメッセージを取得する")
def get_messages():
    logger.info("/messages GETが呼ばれました")
    if not os.path.exists(DATAFILEPATH):
        raise HTTPException(status_code=400, detail="メッセージは保存されてません")
    logger.info(f"{DATAFILEPATH}の読み込みを開始します")
    with open(DATAFILEPATH, "r") as f:
        messages = json.load(f)
    logger.info("読み込みが完了しました")
    return {"messages": messages}

@app.get("/messages/{text}", description="文字列が保存されているか")
def exists_text(text:str = Path(..., description="文字列")):
    logger.info(f"/messages/{text} GETが呼ばれました")
    if not os.path.exists(DATAFILEPATH):
        raise HTTPException(status_code=400, detail="メッセージは保存されていません")
    logger.info(f"{DATAFILEPATH}の読み込みを開始します")
    with open(DATAFILEPATH, "r") as f:
        messages = json.load(f)
    if not text in messages:
        raise HTTPException(status_code=404, detail=f"{text}は保存されていません")
    return {"message": True}