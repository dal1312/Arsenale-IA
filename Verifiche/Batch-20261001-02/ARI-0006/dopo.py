import re

def metadata(text: str, key: str) -> str | None:
    pattern = rf"^- \*\*{re.escape(key)}:\*\*\s*(.+?)\s*$"
    match = re.search(pattern, text, re.MULTILINE)
    return match.group(1).strip() if match else None
