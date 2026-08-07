import unittest

from Strumenti.verifica_promozioni import promotion_errors


def report(project: str, evidence_type: str = "Interna", state: str = "Valida") -> dict[str, str]:
    return {
        "Progetto": project,
        "Tipo prova": evidence_type,
        "Stato evidenza": state,
    }


class PromotionThresholdTests(unittest.TestCase):
    def test_verified_accepts_two_distinct_projects_with_independent_proof(self) -> None:
        errors = promotion_errors(
            "Verificata",
            [report("org/internal"), report("org/external", "Indipendente")],
        )
        self.assertEqual(errors, [])

    def test_verified_rejects_less_than_two_valid_reports(self) -> None:
        errors = promotion_errors("Verificata", [report("org/internal")])
        self.assertTrue(any("almeno 2 evidenze valide" in error for error in errors))

    def test_verified_rejects_same_project_twice(self) -> None:
        errors = promotion_errors(
            "Verificata",
            [report("org/same"), report("org/same", "Indipendente")],
        )
        self.assertTrue(any("almeno 2 progetti distinti" in error for error in errors))

    def test_verified_rejects_missing_independent_proof(self) -> None:
        errors = promotion_errors(
            "Verificata",
            [report("org/one"), report("org/two")],
        )
        self.assertTrue(any("almeno 1 prova indipendente" in error for error in errors))

    def test_non_verified_does_not_require_promotion_threshold(self) -> None:
        self.assertEqual(promotion_errors("Bozza verificabile", []), [])

    def test_non_valid_reports_do_not_count(self) -> None:
        errors = promotion_errors(
            "Verificata",
            [
                report("org/one"),
                report("org/two", "Indipendente", "Inconcludente"),
            ],
        )
        self.assertTrue(any("almeno 2 evidenze valide" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
