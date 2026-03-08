from pathlib import Path

from gui.app import LibraryApp
from services.library_service import LibraryService
from storage.json_storage import JsonStorage
from utils.runtime import enforce_python_version


def main() -> None:
    """Käivitab rakenduse ja valmistab vajalikud teenused ette."""
    enforce_python_version()

    data_path = Path(__file__).parent / "data" / "books.json"
    storage = JsonStorage(data_path)
    service = LibraryService(storage)

    app = LibraryApp(service)
    app.run()


if __name__ == "__main__":
    main()
