from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_ROOT = ROOT / "Verifiche"
PROCEDURE_ROOT = ROOT / "Procedure"

REQUIRED_METADATA = (
    "Identificativo",
    "Procedura",
    "Versione procedura",
    "Data",
    "Progetto",
    "Revisione",
    "Tipo prova",
    "Stato evidenza",
)

REQUIRED_HEADINGS = (
    "## Ambito",
    "## Ambiente e accesso",
    "## Passi esercitati",
    "## Verifiche osservabili",
    "## Rilievi prodotti",
    "## Limiti",
    "## Esito sul progetto",
    "## Esito sulla procedura",
)

ID_RE = re.compile(r"^VER-(ARI-\d{4})-(\d{8})-(\d{2})$")
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
VALID_TYPES = {"Interna", "Indipendente"}
VALID_STATES = {"Eseguita", "Valida", "Inconcludente", "Respinta"}


def metadata(text: str, key: str) -> str | None:
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


def current_procedure_version(code: str) -> str | None:
    matches = list(PROCEDURE_ROOT.glob(f"{code}-*/PROCEDURA.md"))
    if len(matches) != 1:
        return None
    return metadata(matches[0].read_text(encoding="utf-8"), "Versione")


def main() -> int:
    errors: list[str] = []
    reports = sorted(EVIDENCE_ROOT.glob("ARI-*/VER-*.md")) if EVIDENCE_ROOT.is_dir() else []
    seen_ids: set[str] = set()

    for report in reports:
        text = report.read_text(encoding="utf-8")
        values = {key: metadata(text, key) for key in REQUIRED_METADATA}

        for key, value in values.items():
            if not value:
                errors.append(f"{report}: metadato {key} mancante o vuoto")

        evidence_id = values.get("Identificativo")
        code = values.get("Procedura")
        version = values.get("Versione procedura")
        date = values.get("Data")
        evidence_type = values.get("Tipo prova")
        state = values.get("Stato evidenza")

        if evidence_id:
            match = ID_RE.fullmatch(evidence_id)
            if not match:
                errors.append(f"{report}: identificativo non conforme: {evidence_id}")
            else:
                if code and match.group(1) != code:
                    errors.append(f"{report}: codice in Identificativo diverso da Procedura")
                if date and match.group(2) != date.replace("-", ""):
                    errors.append(f"{report}: data in Identificativo diversa da Data")
            if evidence_id in seen_ids:
                errors.append(f"{report}: identificativo duplicato {evidence_id}")
            seen_ids.add(evidence_id)
            if report.stem != evidence_id:
                errors.append(f"{report}: nome file diverso dall'Identificativo")

        if code and report.parent.name != code:
            errors.append(f"{report}: cartella diversa dal codice procedura {code}")
        if code and not current_procedure_version(code):
            errors.append(f"{report}: procedura {code} non trovata")
        if version and not VERSION_RE.fullmatch(version):
            errors.append(f"{report}: versione procedura non semantica: {version}")
        if date and not DATE_RE.fullmatch(date):
            errors.append(f"{report}: data non conforme: {date}")
        if evidence_type and evidence_type not in VALID_TYPES:
            errors.append(f"{report}: tipo prova non ammesso: {evidence_type}")
        if state and state not in VALID_STATES:
            errors.append(f"{report}: stato evidenza non ammesso: {state}")

        positions: list[int] = []
        for heading in REQUIRED_HEADINGS:
            count = text.count(heading)
            if count != 1:
                errors.append(f"{report}: {heading} presente {count} volte")
                continue
            positions.append(text.find(heading))
            if not section_body(text, heading):
                errors.append(f"{report}: sezione vuota {heading}")

        if len(positions) == len(REQUIRED_HEADINGS) and positions != sorted(positions):
            errors.append(f"{report}: sezioni obbligatorie fuori ordine")

    if errors:
        print("VERIFICA EVIDENZE FALLITA")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"VERIFICA EVIDENZE SUPERATA: {len(reports)} rapporti strutturalmente validi")
    return 0


if __name__ == "__main__":
    sys.exit(main())
