from __future__ import annotations


class InMemoryStore:
    def __init__(self) -> None:
        self._items: dict[str, list[str]] = {}

    def get_recent(self, user_id: str, limit: int = 5) -> list[str]:
        return self._items.get(user_id, [])[-limit:]

    def append(self, user_id: str, message: str) -> None:
        if user_id not in self._items:
            self._items[user_id] = []
        self._items[user_id].append(message)
