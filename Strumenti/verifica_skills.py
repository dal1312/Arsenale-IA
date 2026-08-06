from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROCEDURE_ROOT = ROOT / "Procedure"

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ALLOWED_TOP_LEVEL = {
    "name",
    "description",
    "license",
    "compatibility",
    "metadata",
    "allowed-tools",
}


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if not lines or lines[0].strip() != "---":
        raise ValueError("front matter YAML iniziale assente")

    try:
        end = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration as exc:
        raise ValueError("chiusura del front matter YAML assente") from exc

    metadata: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.startswith((" ", "\t")):
            continue
        if ":" not in line:
            raise ValueError(f"riga front matter non valida: {line!r}")
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()

    body = "\n".join(lines[end + 1 :])
    return metadata, body


def main() -> int:
    errors: list[str] = []
    names: dict[str, Path] = {}
    procedure_count = 0
    skill_count = 0

    for directory in sorted(p for p in PROCEDURE_ROOT.iterdir() if p.is_dir()):
        procedure = directory / "PROCEDURA.md"
        if not procedure.exists():
            continue

        procedure_count += 1
        skill = directory / "SKILL.md"

        if not skill.exists():
            errors.append(f"{directory.name}: manca SKILL.md")
            continue

        skill_count += 1

        try:
            metadata, body = parse_frontmatter(skill)
        except (OSError, ValueError) as exc:
            errors.append(f"{directory.name}: {exc}")
            continue

        unexpected = set(metadata) - ALLOWED_TOP_LEVEL
        if unexpected:
            fields = ", ".join(sorted(unexpected))
            errors.append(
                f"{directory.name}: campi top-level non portabili nel front matter: {fields}"
            )

        name = metadata.get("name", "")
        description = metadata.get("description", "")

        if not NAME_RE.fullmatch(name):
            errors.append(
                f"{directory.name}: name non valido {name!r}; usare minuscole, numeri e trattini"
            )

        if not description:
            errors.append(f"{directory.name}: description assente o vuota")

        if len(description) > 1024:
            errors.append(f"{directory.name}: description supera 1024 caratteri")

        if "PROCEDURA.md" not in body:
            errors.append(f"{directory.name}: il corpo non rinvia a PROCEDURA.md")

        if name:
            previous = names.get(name)
            if previous is not None:
                errors.append(
                    f"{directory.name}: name duplicato {name!r}, già usato da {previous.name}"
                )
            else:
                names[name] = directory

    if errors:
        print("VERIFICA FALLITA")
        for error in errors:
            print(f"- {error}")
        print(
            f"\nProcedure rilevate: {procedure_count}; "
            f"SKILL.md rilevati: {skill_count}; errori: {len(errors)}"
        )
        return 1

    print(
        f"OK: {procedure_count} procedure, "
        f"{skill_count} adattatori SKILL.md validi e nomi runtime univoci."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
