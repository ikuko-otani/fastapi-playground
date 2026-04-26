# F-08: Dependencies — First Steps

## What you learn / 学習内容

**EN:** How to use FastAPI's Dependency Injection system with `Depends()`.

**JA:** FastAPI の依存性注入（DI）システムを `Depends()` で使う方法を学ぶ。

## Key concepts / キーコンセプト

- `Depends()` — declare a dependency (do NOT call it, just pass it)
- `Annotated[T, Depends(...)]` — modern recommended pattern
- Type alias (`CommonsDep`) — reuse the same dependency cleanly
- DI works with both `async def` and `def`

## Interview focus / 面接頻出ポイント

- Why DI? → separation of concerns, testability, reusability
- `Depends()` vs calling the function directly
- How FastAPI integrates dependencies into OpenAPI `/docs`

## Reference / 参照

- Tutorial: https://fastapi.tiangolo.com/tutorial/dependencies/
- Advanced — Sub-dependencies: https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/
- Advanced — Dependencies with yield: https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/
