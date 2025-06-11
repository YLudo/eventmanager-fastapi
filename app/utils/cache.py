from datetime import datetime, timedelta
from typing import Any, Dict, Tuple

class SimpleCache:
    def __init__(self, ttl_seconds: int = 60) -> None:
        self.ttl = timedelta(seconds=ttl_seconds)
        self._store: Dict[str, Tuple[Any, datetime]] = {}

    def get(self, key: str) -> Any | None:
        item = self._store.get(key)
        if not item:
            return None
        value, timestamp = item
        if datetime.utcnow() - timestamp > self.ttl:
            self._store.pop(key, None)
            return None
        return value

    def set(self, key: str, value: Any) -> None:
        self._store[key] = (value, datetime.utcnow())

    def invalidate(self, key: str) -> None:
        self._store.pop(key, None)

cache = SimpleCache(ttl_seconds=60)