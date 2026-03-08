from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from models.book import Book


class BookListPanel(ttk.LabelFrame):
    """Kuvab raamatute nimekirja tabeli kujul."""

    def __init__(self, master: tk.Misc) -> None:
        """Loob tabeli, kerimisriba ja veerud."""
        super().__init__(master, text="Raamatute nimekiri")

        self.tree = ttk.Treeview(
            self,
            columns=("id", "title", "author", "year", "genre", "status"),
            show="headings",
            height=15,
        )
        self._build_widgets()

    def populate(self, books: list[Book]) -> None:
        """Asendab tabeli sisu etteantud raamatute andmetega."""
        for item_id in self.tree.get_children():
            self.tree.delete(item_id)

        for book in books:
            self.tree.insert(
                "",
                "end",
                values=(book.id, book.title, book.author, book.year, book.genre, book.status_label),
            )

    def get_selected_book_id(self) -> int | None:
        """Tagastab valitud tabelirea raamatu ID."""
        selected = self.tree.selection()
        if not selected:
            return None

        values = self.tree.item(selected[0], "values")
        if not values:
            return None

        return int(values[0])

    def _build_widgets(self) -> None:
        """Paigutab tabeli veerud ja kerimisriba."""
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        headings = {
            "id": "ID",
            "title": "Pealkiri",
            "author": "Autor",
            "year": "Aasta",
            "genre": "Žanr",
            "status": "Staatus",
        }

        widths = {
            "id": 60,
            "title": 240,
            "author": 170,
            "year": 80,
            "genre": 120,
            "status": 100,
        }

        for column_name, heading_text in headings.items():
            self.tree.heading(column_name, text=heading_text)
            self.tree.column(column_name, width=widths[column_name], anchor="center")

        self.tree.grid(row=0, column=0, sticky="nsew", padx=(8, 0), pady=8)
        scrollbar.grid(row=0, column=1, sticky="ns", padx=(0, 8), pady=8)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
