from typing import Any

def new(*args: Any, **kwargs: Any): ...
def atfork() -> None: ...
def get_random_bytes(n: int) -> bytes: ...
