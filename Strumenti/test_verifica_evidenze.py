import unittest

from Strumenti.verifica_evidenze import declared_versions_from_text, procedure_versions


class EvidenceVersionValidationTests(unittest.TestCase):
    def test_extracts_current_and_historical_versions(self) -> None:
        text = """# ARI-9999 — Demo

## Cronologia delle versioni

- **1.2.1** — Stato aggiornato.
- **1.2.0** — Metodo iniziale.
"""
        self.assertEqual(declared_versions_from_text(text), {"1.2.1", "1.2.0"})

    def test_real_procedure_accepts_declared_history_only(self) -> None:
        versions = procedure_versions("ARI-0001")
        self.assertIsNotNone(versions)
        assert versions is not None
        self.assertIn("0.2.0", versions)
        self.assertIn("0.2.1", versions)
        self.assertNotIn("9.9.9", versions)

    def test_unknown_procedure_returns_none(self) -> None:
        self.assertIsNone(procedure_versions("ARI-9999"))


if __name__ == "__main__":
    unittest.main()
