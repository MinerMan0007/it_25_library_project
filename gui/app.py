from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk

from gui.form_panel import BookFormPanel
from gui.list_panel import BookListPanel
from services.library_service import LibraryService


class LibraryApp:
    """Seob kasutajaliidese komponendid ja rakenduse tegevused."""

    def __init__(self, service: LibraryService) -> None:
        """Valmistab peaakna ja kõik alamkomponendid ette."""
        self.service = service
        self.root = tk.Tk()
        self.root.title("Raamatukogu haldur")
        self.root.geometry("1100x650")  # Veidi kõrgem, et loendur mahuks mugavalt
        self.root.minsize(980, 560)

        self.form_panel = BookFormPanel(self.root)
        self.list_panel = BookListPanel(self.root)

        self._build_layout()
        self._build_button_row()
        self.refresh_list()

    def run(self) -> None:
        """Käivitab Tkinteri põhisilmuse."""
        self.root.mainloop()

    def add_book(self) -> None:
        """Lisab vormilt saadud andmete põhjal uue raamatu."""
        title, author, year_text, genre = self.form_panel.get_book_form_data()
        success, message = self.service.add_book(title, author, year_text, genre)

        if success:
            self.form_panel.clear_form()
            self.refresh_list()
            messagebox.showinfo("Info", message)
        else:
            messagebox.showwarning("Hoiatus", message)

    def update_book(self) -> None:
        """Muudab valitud raamatu andmeid vormi sisendi põhjal."""
        book_id = self.list_panel.get_selected_book_id()
        if book_id is None:
            messagebox.showwarning("Hoiatus", "Palun vali tabelist raamat, mida soovid muuta.")
            return

        title, author, year_text, genre = self.form_panel.get_book_form_data()
        success, message = self.service.update_book(book_id, title, author, year_text, genre)

        if success:
            self.refresh_list()
            messagebox.showinfo("Info", message)
        else:
            messagebox.showwarning("Hoiatus", message)

    def delete_book(self) -> None:
        """Kustutab valitud raamatu pärast kinnitust."""
        book_id = self.list_panel.get_selected_book_id()
        if book_id is None:
            messagebox.showwarning("Hoiatus", "Palun vali tabelist raamat.")
            return

        if messagebox.askyesno("Kinnitus", "Kas oled kindel, et soovid selle raamatu kustutada?"):
            if self.service.delete_book(book_id):
                self.refresh_list()
                messagebox.showinfo("Info", "Raamat on kustutatud.")

    def toggle_selected_status(self) -> None:
        """Muudab valitud raamatu staatust."""
        book_id = self.list_panel.get_selected_book_id()
        if book_id is None:
            messagebox.showwarning("Hoiatus", "Palun vali tabelist raamat.")
            return

        if self.service.toggle_borrow_status(book_id):
            self.refresh_list()

    def refresh_list(self) -> None:
        """Värskendab tabelit vastavalt otsingule ja filtrile."""
        query = self.form_panel.get_search_query()
        status_filter = self.form_panel.get_status_filter()
        books = self.service.search_books(query, status_filter)
        self.list_panel.populate(books)

    def _build_layout(self) -> None:
        """Seadistab põhiakna paigutuse."""
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.form_panel.grid(row=0, column=0, sticky="ns", padx=12, pady=12)
        self.list_panel.grid(row=0, column=1, sticky="nsew", padx=(0, 12), pady=12)

    def _build_button_row(self) -> None:
        """Loob tegevusnupud ja seob need käskudega."""
        button_frame = ttk.Frame(self.form_panel)
        button_frame.grid(row=7, column=0, columnspan=2, sticky="ew", padx=8, pady=(10, 8))
        button_frame.columnconfigure((0, 1), weight=1)

        ttk.Button(button_frame, text="Lisa raamat", command=self.add_book).grid(
            row=0, column=0, sticky="ew", padx=(0, 4), pady=4
        )
        ttk.Button(button_frame, text="Värskenda vaadet", command=self.refresh_list).grid(
            row=0, column=1, sticky="ew", padx=(4, 0), pady=4
        )

        # Uus nupp andmete muutmiseks
        ttk.Button(button_frame, text="Muuda andmeid", command=self.update_book).grid(
            row=1, column=0, sticky="ew", padx=(0, 4), pady=4
        )

        ttk.Button(button_frame, text="Muuda staatust", command=self.toggle_selected_status).grid(
            row=1, column=1, sticky="ew", padx=(4, 0), pady=4
        )
        ttk.Button(button_frame, text="Kustuta raamat", command=self.delete_book).grid(
            row=2, column=0, columnspan=2, sticky="ew", pady=(4, 0)
        )