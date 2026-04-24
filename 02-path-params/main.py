# Chapter F-02: Path Parameters
# Ref: https://fastapi.tiangolo.com/tutorial/path-params/
#
# Run: uvicorn main:app --reload
# Docs: http://localhost:8000/docs

# TODO: Implement the following steps
# 日本語訳：以下のステップを順番に実装してください
#
# Step 1: Basic path parameter (no type hint)
# Step 2: Path parameter with int type hint -> auto parsing & validation
# Step 3: Order matters -> /users/me before /users/{user_id}
# Step 4: Enum-based predefined values (str, Enum)
# Step 5: Path containing path -> /files/{file_path:path}
