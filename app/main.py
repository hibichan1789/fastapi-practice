from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
def home():
    return {"message": "DockerとGitHubの連携に成功"}

@app.get("/hello/{name}")
def say_hello(name:str):
    return {"message": f"こんにちは{name}さん"}

@app.get("/add", description="クエリパラメータの二つの整数値を四則演算する")
def calc_numbers(a:int = Query(..., description="整数値"), b:int = Query(..., description="整数値")):
    add_value = a + b
    sub_value = a - b
    mul_value = a * b
    div_value = a / b if b != 0 else None
    return {
        f"{a} + {b}": add_value,
        f"{a} - {b}": sub_value,
        f"{a} * {b}": mul_value,
        f"{a} / {b}": div_value
        }