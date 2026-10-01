"""Esporta le voci Pianificata di un catalogo locale, senza sovrascritture."""
import argparse
import csv
import re
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='Esporta procedure pianificate in CSV UTF-8.')
    parser.add_argument('--catalogo', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        text = args.catalogo.read_text(encoding='utf-8-sig')
        rows = re.findall(r'^- (ARI-\d{4}) — (.+?) — Pianificata\s*$', text, re.MULTILINE)
        if not rows or len({code for code, _ in rows}) != len(rows):
            raise ValueError('Voci pianificate assenti o codici duplicati')
        with args.output.open('x', encoding='utf-8', newline='') as stream:
            writer = csv.writer(stream)
            writer.writerow(['codice', 'titolo', 'stato'])
            writer.writerows((code, title, 'Pianificata') for code, title in rows)
    except (OSError, UnicodeError, ValueError) as exc:
        parser.exit(1, f'Errore: {exc}\n')
    print(f'Esportate {len(rows)} procedure pianificate in {args.output}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
