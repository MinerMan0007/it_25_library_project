from __future__ import annotations

import os
import sys


type VersionTuple = tuple[int, int]

REQUIRED_VERSION: VersionTuple = (3, 12)
BYPASS_ENV_VAR = "LIBRARY_APP_ALLOW_OLD_PYTHON"


def enforce_python_version() -> None:
    """Kontrollib, kas rakendus käivitatakse toetatud Pythoni versiooniga."""
    if os.getenv(BYPASS_ENV_VAR) == "1":
        return

    current_version = sys.version_info[:2]
    if current_version < REQUIRED_VERSION:
        required = f"{REQUIRED_VERSION[0]}.{REQUIRED_VERSION[1]}"
        current = f"{current_version[0]}.{current_version[1]}"
        raise RuntimeError(
            "See projekt vajab Python 3.12 või uuemat versiooni. "
            f"Praegune versioon on {current}. "
            f"Erandkorras saab kontrolli vahele jätta keskkonnamuutujaga {BYPASS_ENV_VAR}=1."
        )
