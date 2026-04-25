# Chapter F-06: Response Model
# Ref: https://fastapi.tiangolo.com/tutorial/response-model/
#
# Run: uvicorn main:app --reload
# Docs: http://localhost:8000/docs
#
# Topics covered in this chapter:
#   1. Return type annotation as response model
#   2. response_model parameter in path operation decorator
#   3. Input/Output model separation (security: password filtering)
#   4. Model inheritance for data filtering
#   5. response_model_exclude_unset / _exclude_defaults / _exclude_none
#   6. response_model_include / response_model_exclude
#   7. Returning Response directly (JSONResponse, RedirectResponse)
#   8. response_model=None to disable validation

# TODO: Fill in the implementation following the study guide (Step 1 ~ Step 4)
# 日本語訳：以下に学習ガイド（Step 1〜4）に従って実装を追加してください

from fastapi import FastAPI

# Type hints are mandatory in FastAPI — they drive validation, serialization, and OpenAPI docs
# 日本語訳：型ヒントはFastAPIの必須要件 — バリデーション・シリアライズ・OpenAPI生成に直結します

app = FastAPI()
