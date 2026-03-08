from __future__ import annotations

import json
from pathlib import Path

from models.book import Book, BookData


type BookListData = list[BookData]


class JsonStorage:
    """Loeb ja salvestab raamatute andmeid JSON-faili."""

    def __init__(self, file_path: Path) -> None:
        """Seob salvestuskihi konkreetse failiteega."""
        self.file_path = file_path

    def load_books(self) -> list[Book]:
        """Tagastab failist loetud raamatute nimekirja."""
        if not self.file_path.exists():
            return []

        with self.file_path.open("r", encoding="utf-8") as file:
            raw_data: BookListData = json.load(file)

        return [Book.from_dict(item) for item in raw_data]

    def save_books(self, books: list[Book]) -> None:
        """Salvestab kõik raamatud JSON-faili."""
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        data = [book.to_dict() for book in books]
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
