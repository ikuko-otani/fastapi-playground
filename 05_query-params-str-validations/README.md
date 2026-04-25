# F-05: Query Params & String Validations

## What you will learn / 学習内容

**English:**
This exercise covers how FastAPI handles query parameters with additional validation using `Query()` and `Annotated` from the `typing` module. You will learn how type hints directly drive both runtime validation and OpenAPI schema generation — a key concept for backend interviews.

**日本語：**
この演習では、FastAPI が `Query()` と `typing.Annotated` を使ってクエリパラメーターに追加バリデーションを付与する方法を学びます。型ヒントがランタイムバリデーションと OpenAPI スキーマ生成の両方を駆動するという、バックエンド面接で頻出の重要概念です。

---

## Topics covered / カバーするトピック

| # | Topic (EN) | トピック（日本語） |
|---|-----------|------------------|
| 1 | Optional query param with `str \| None` | `str \| None` によるオプショナルクエリ |
| 2 | `Query(min_length, max_length, pattern)` | 文字列長・正規表現バリデーション |
| 3 | Required query params (no default) | デフォルト値なし → 必須パラメーター |
| 4 | `list[str]` query param (multi-value) | 複数値クエリパラメーター |
| 5 | `title`, `description` metadata | OpenAPI ドキュメント用メタデータ |
| 6 | `alias` for non-Python-valid names | Python 変数名に使えない URL キー名への対応 |
| 7 | `deprecated=True` | 非推奨パラメーターの OpenAPI 表示 |
| 8 | `include_in_schema=False` | OpenAPI スキーマから隠す |
| 9 | `AfterValidator` (Pydantic v2) | カスタムバリデーション関数 |

---

## Flagship connection / payment-ledger-api との接続

- `GET /transactions?status=pending&limit=50` → `Query(min_length, max_length)` で入力サニタイズ
- `GET /transactions?tag=food&tag=travel` → `list[str]` multi-value query
- `AfterValidator` → カスタム検証（例：`txn-` プレフィックス付き取引ID検証）
- `include_in_schema=False` → 内部デバッグパラメーターを公開APIから隠す

---

## References / 参考リンク

- [Official Tutorial](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/)
- [Pydantic AfterValidator docs](https://docs.pydantic.dev/latest/concepts/validators/#annotated-validators)
- [FastAPI Advanced: Query Params](https://fastapi.tiangolo.com/advanced/additional-responses/)
