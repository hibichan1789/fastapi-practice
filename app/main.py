from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "DockerとGitHubの連携に成功"}

@app.get("/hello/{name}")
def say_hello(name:str):
    return {"message": f"こんにちは{name}さん"}