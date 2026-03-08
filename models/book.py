from __future__ import annotations

from dataclasses import dataclass


type BookData = dict[str, int | str | bool]


@dataclass(slots=True)
class Book:
    """Hoiab ühe raamatu põhiandmeid."""

    id: int
    title: str
    author: str
    year: int
    genre: str
    is_borrowed: bool = False

    @property
    def status_label(self) -> str:
        """Tagastab raamatu staatuse eestikeelse tekstina."""
        return "Väljas" if self.is_borrowed else "Kohal"

    def to_dict(self) -> BookData:
        """Teisendab raamatu JSON-i jaoks sõnastikuks."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "genre": self.genre,
            "is_borrowed": self.is_borrowed,
        }

    @classmethod
    def from_dict(cls, data: BookData) -> "Book":
        """Loob raamatu objekti sõnastiku põhjal."""
        return cls(
            id=int(data["id"]),
            title=str(data["title"]),
            author=str(data["author"]),
            year=int(data["year"]),
            genre=str(data["genre"]),
            is_borrowed=bool(data.get("is_borrowed", False)),
        )
