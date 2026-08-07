from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROCEDURE_ROOT = ROOT / "Procedure"
CATALOGO = ROOT / "CATALOGO.md"

REQUIRED_METADATA = (
    "Categoria",
    "Livello",
    "Stato",
    "Versione",
    "Utilizzo offline",
)

REQUIRED_HEADINGS = (
    "## Scopo",
    "## Campo di applicazione",
    "## Quando usarla",
    "## Quando non usarla",
    "## Prerequisiti",
    "## Materiale necessario",
    "## Procedura operativa",
    "## Controlli",
    "## Errori frequenti",
    "## Rapporto finale",
    "## Condizioni di uscita",
    "## Cronologia delle versioni",
)

DIR_RE = re.compile(r"^(ARI-\d{4})-")
TITLE_RE = re.compile(r"^# (ARI-\d{4}) — .+", re.MULTILINE)
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
AVAILABLE_RE = re.compile(r"\*\*(ARI-\d{4}) — [^\n]+?\*\* — Disponibile")


def metadata_value(text: str, key: str) -> str | None:
    match = re.search(rf"^- \*\*{re.escape(key)}:\*\*\s*(.+?)\s*$", text, re.MULTILINE)
    return match.group(1).strip() if match else None


def section_body(text: str, heading: str) -> str:
    start = text.find(heading)
    if start < 0:
        return ""
    start += len(heading)
    rest = text[start:]
    next_heading = re.search(r"^##\s+", rest, re.MULTILINE)
    end = next_heading.start() if next_heading else len(rest)
    return rest[:end].strip()


def main() -> int:
    errors: list[str] = []
    codes: set[str] = set()

    if not PROCEDURE_ROOT.is_dir():
        print("ERRORE: cartella Procedure non trovata")
        return 1

    procedure_dirs = sorted(path for path in PROCEDURE_ROOT.iterdir() if path.is_dir())

    for directory in procedure_dirs:
        dir_match = DIR_RE.match(directory.name)
        if not dir_match:
            errors.append(f"{directory.name}: nome cartella non conforme ARI-xxxx-...")
            continue

        expected_code = dir_match.group(1)
        procedure_file = directory / "PROCEDURA.md"
        skill_file = directory / "SKILL.md"

        if not procedure_file.is_file():
            errors.append(f"{directory.name}: PROCEDURA.md mancante")
            continue
        if not skill_file.is_file():
            errors.append(f"{directory.name}: SKILL.md mancante")

        text = procedure_file.read_text(encoding="utf-8")
        title = TITLE_RE.search(text)
        if not title:
            errors.append(f"{directory.name}: titolo H1 non conforme")
        elif title.group(1) != expected_code:
            errors.append(
                f"{directory.name}: codice titolo {title.group(1)} diverso da {expected_code}"
            )

        if expected_code in codes:
            errors.append(f"{directory.name}: codice duplicato {expected_code}")
        codes.add(expected_code)

        for key in REQUIRED_METADATA:
            value = metadata_value(text, key)
            if not value:
                errors.append(f"{directory.name}: metadato {key} mancante o vuoto")

        version = metadata_value(text, "Versione")
        if version and not VERSION_RE.fullmatch(version):
            errors.append(f"{directory.name}: versione non semantica: {version}")
        if version and f"**{version}**" not in section_body(text, "## Cronologia delle versioni"):
            errors.append(f"{directory.name}: versione {version} assente dalla cronologia")

        positions: list[int] = []
        for heading in REQUIRED_HEADINGS:
            count = text.count(heading)
            if count != 1:
                errors.append(f"{directory.name}: {heading} presente {count} volte")
                continue
            pos = text.find(heading)
            positions.append(pos)
            if not section_body(text, heading):
                errors.append(f"{directory.name}: sezione vuota {heading}")

        if len(positions) == len(REQUIRED_HEADINGS) and positions != sorted(positions):
            errors.append(f"{directory.name}: sezioni canoniche fuori ordine")

    if CATALOGO.is_file():
        catalog_text = CATALOGO.read_text(encoding="utf-8")
        available = set(AVAILABLE_RE.findall(catalog_text))
        missing = sorted(available - codes)
        extra = sorted(codes - available)
        if missing:
            errors.append("Procedure disponibili senza cartella: " + ", ".join(missing))
        if extra:
            errors.append("Cartelle procedura non marcate Disponibile: " + ", ".join(extra))
    else:
        errors.append("CATALOGO.md mancante")

    if errors:
        print("VERIFICA PROCEDURE FALLITA")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"VERIFICA PROCEDURE SUPERATA: {len(procedure_dirs)} procedure conformi a STANDARD.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
