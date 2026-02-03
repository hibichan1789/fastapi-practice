from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "DockerとGitHubの連携に成功"}