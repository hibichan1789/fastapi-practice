from fastapi import FastAPI, Query
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/stats", description="数値リストの統計値を返す")
def get_stats(numbers:list[float] = Query(..., description="計算したい数値のリスト")):
    array = np.array(numbers)
    logger.info(array)
    return {
        "array":array.tolist(),
        "mean": np.mean(array),
        "max": np.max(array),
        "min": np.min(array)
    }