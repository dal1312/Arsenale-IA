from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROCEDURE_ROOT = ROOT / "Procedure"
EVIDENCE_ROOT = ROOT / "Verifiche"

META_RE_TEMPLATE = r"^- \*\*{key}:\*\*\s*(.+?)\s*$"
DIR_RE = re.compile(r"^(ARI-\d{4})-")


def metadata(text: str, key: str) -> str | None:
    match = re.search(
        META_RE_TEMPLATE.format(key=re.escape(key)),
        text,
        re.MULTILINE,
    )
    return match.group(1).strip() if match else None


def promotion_errors(procedure_state: str, reports: list[dict[str, str]]) -> list[str]:
    if procedure_state != "Verificata":
        return []

    valid = [report for report in reports if report.get("Stato evidenza") == "Valida"]
    errors: list[str] = []

    if len(valid) < 2:
        errors.append("richieste almeno 2 evidenze valide")

    projects = {report.get("Progetto", "").strip() for report in valid}
    projects.discard("")
    if len(projects) < 2:
        errors.append("richiesti almeno 2 progetti distinti")

    if not any(report.get("Tipo prova") == "Indipendente" for report in valid):
        errors.append("richiesta almeno 1 prova indipendente")

    return errors


def reports_for(code: str) -> list[dict[str, str]]:
    directory = EVIDENCE_ROOT / code
    if not directory.is_dir():
        return []

    reports: list[dict[str, str]] = []
    for path in sorted(directory.glob("VER-*.md")):
        text = path.read_text(encoding="utf-8")
        reports.append(
            {
                "Progetto": metadata(text, "Progetto") or "",
                "Tipo prova": metadata(text, "Tipo prova") or "",
                "Stato evidenza": metadata(text, "Stato evidenza") or "",
            }
        )
    return reports


def main() -> int:
    errors: list[str] = []
    verified_count = 0

    for directory in sorted(PROCEDURE_ROOT.iterdir()):
        if not directory.is_dir():
            continue
        match = DIR_RE.match(directory.name)
        if not match:
            continue

        code = match.group(1)
        procedure_path = directory / "PROCEDURA.md"
        if not procedure_path.is_file():
            continue

        text = procedure_path.read_text(encoding="utf-8")
        state = metadata(text, "Stato") or ""
        if state == "Verificata":
            verified_count += 1

        for error in promotion_errors(state, reports_for(code)):
            errors.append(f"{code}: {error}")

    if errors:
        print("VERIFICA PROMOZIONI FALLITA")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "VERIFICA PROMOZIONI SUPERATA: "
        f"{verified_count} procedure Verificate rispettano la soglia automatizzabile"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
