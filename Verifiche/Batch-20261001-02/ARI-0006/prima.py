import re
META_RE_TEMPLATE = r"^- \*\*{key}:\*\*\s*(.+?)\s*$"

def metadata(text: str, key: str) -> str | None:
    match = re.search(
        META_RE_TEMPLATE.format(key=re.escape(key)),
        text,
        re.MULTILINE,
    )
    return match.group(1).strip() if match else None
