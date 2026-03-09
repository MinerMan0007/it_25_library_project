from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from models.book import Book


class BookListPanel(ttk.LabelFrame):
    """Kuvab raamatute nimekirja tabeli kujul ja raamatute arvu."""

    def __init__(self, master: tk.Misc) -> None:
        """Loob tabeli, kerimisriba, veerud ja loenduri."""
        super().__init__(master, text="Raamatute nimekiri")

        self.tree = ttk.Treeview(
            self,
            columns=("id", "title", "author", "year", "genre", "status"),
            show="headings",
            height=15,
        )

        # Raamatute arvu silt (Rasmuse lisaülesanne)
        self.count_var = tk.StringVar(value="Raamatuid kokku: 0")
        self.count_label = ttk.Label(self, textvariable=self.count_var, font=("TkDefaultFont", 9, "bold"))

        self._build_widgets()

    def populate(self, books: list[Book]) -> None:
        """Asendab tabeli sisu etteantud raamatute andmetega ja uuendab loendurit."""
        for item_id in self.tree.get_children():
            self.tree.delete(item_id)

        for book in books:
            self.tree.insert(
                "",
                "end",
                values=(book.id, book.title, book.author, book.year, book.genre, book.status_label),
            )

        # Uuenda raamatute arvu
        self.count_var.set(f"Raamatuid tabelis: {len(books)}")

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
        """Paigutab tabeli veerud, kerimisriba ja loenduri."""
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

        # Paigutus
        self.tree.grid(row=0, column=0, sticky="nsew", padx=(8, 0), pady=(8, 0))
        scrollbar.grid(row=0, column=1, sticky="ns", pady=(8, 0))

        # Loenduri paigutus tabeli alla
        self.count_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=8, pady=8)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)