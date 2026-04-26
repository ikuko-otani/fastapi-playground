# F-09: Security — OAuth2 with Password Bearer (First Steps Only)

> **Scope**: Intro-level only (触りのみ). Full JWT implementation is out of scope for this sprint.

## What You Learn / 学習内容

### English
- How `OAuth2PasswordBearer` works as a callable dependency
- How FastAPI automatically adds an **Authorize** button in Swagger UI (`/docs`)
- The OAuth2 Password Flow: client POSTs credentials → receives bearer token → sends `Authorization: Bearer <token>` header
- How `Depends(oauth2_scheme)` extracts the token string from the `Authorization` header
- Why `tokenUrl` is a **relative URL** (important for reverse-proxy deployments)
- How FastAPI inherits from `SecurityBase` to integrate with OpenAPI schema

### 日本語
- `OAuth2PasswordBearer` が呼び出し可能な依存関係としてどう機能するか
- FastAPI が Swagger UI（`/docs`）に **Authorize ボタン**を自動追加する仕組み
- OAuth2 パスワードフロー：クライアントが資格情報を POST → Bearer トークンを受け取る → `Authorization: Bearer <token>` ヘッダーを送信
- `Depends(oauth2_scheme)` が `Authorization` ヘッダーからトークン文字列を取り出す仕組み
- `tokenUrl` が**相対 URL**である理由（リバースプロキシ環境で重要）
- FastAPI が `SecurityBase` を継承して OpenAPI スキーマと統合する仕組み

## Key Files / 主要ファイル

| File | Description |
|------|-------------|
| `main.py` | Main FastAPI app with OAuth2 bearer scheme |

## Flagship Relevance / Flagshipとの関連

`payment-ledger-api` では、将来的に JWT Bearer 認証を使って API エンドポイントを保護します。
この単元で学ぶ `OAuth2PasswordBearer` + `Depends()` のパターンは、その基盤となります。

## Related Advanced Guide / 関連上級ガイド

- [OAuth2 with Password, Bearer and JWT tokens](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)
- [Advanced Security](https://fastapi.tiangolo.com/advanced/security/)
- [HTTP Basic Auth](https://fastapi.tiangolo.com/advanced/security/http-basic-auth/)
