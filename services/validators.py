def validate_book_input(title: str, author: str, year_text: str, genre: str) -> tuple[bool, str]:
    """Kontrollib, kas raamatu sisestusväljad sisaldavad sobivaid väärtusi."""

    title = title.strip()
    author = author.strip()
    year_text = year_text.strip()
    genre = genre.strip()

    if not title:
        return False, "Pealkiri on kohustuslik."
    if not author:
        return False, "Autor on kohustuslik."
    if not year_text:
        return False, "Aasta on kohustuslik."
    if not genre:
        return False, "Žanr on kohustuslik."
    if not year_text.isdigit():
        return False, "Aasta peab olema täisarv."

    year = int(year_text)
    if year < 1450 or year > 2100:
        return False, "Aasta peab jääma vahemikku 1450 kuni 2100."

    if len(title) > 120:
        return False, "Pealkiri on liiga pikk."
    if len(author) > 80:
        return False, "Autori nimi on liiga pikk."
    if len(genre) > 40:
        return False, "Žanri väärtus on liiga pikk."

    return True, ""
