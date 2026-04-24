# Chapter F-01: First Steps
# Ref: https://fastapi.tiangolo.com/tutorial/first-steps/
#
# Run: uvicorn main:app --reload
# Docs: http://localhost:8000/docs

# TODO: Step 1 — Import FastAPI and create app instance
# FastAPI をインポートし、app インスタンスを作成する
from fastapi import FastAPI

# Create the FastAPI application instance
# FastAPI アプリケーションのインスタンスを作成する
app = FastAPI()

# TODO: Step 2 — Define root endpoint GET /
# ルートエンドポイント GET / を定義する
@app.get("/")
async def root():
    return {"message": "Hello World"}

# TODO: Step 3 — Add GET /health endpoint
# ヘルスチェック用エンドポイント GET /health を追加する
# Health check endpoint — used in Docker / K8s liveness probes
# ヘルスチェック用エンドポイント — Docker/K8s の liveness probe で使う
@app.get("/health")
async def health_check():
    return {"status": "OK"}

# TODO: Step 4 — Add async GET /items/{item_id} endpoint
# 非同期版エンドポイント GET /items/{item_id} を追加する
# Path parameter with type hint — FastAPI validates and converts types automatically
# 型ヒント付きパスパラメータ — FastAPI が自動でバリデーション・型変換する
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "description": f"Item number {item_id}"}

# TODO: Step 5 — Add sync def GET /ping endpoint (compare with async)
# 同期版エンドポイント GET /ping を追加して async def と比較する
# Sync version for comparison — use when calling blocking (non-async) code
# 同期版（比較用）— ブロッキングコードを呼ぶときに使う
@app.get("/ping")
def ping():
    return {"pong": True}
