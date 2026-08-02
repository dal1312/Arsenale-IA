# ARI-0601 — Revisione Git

## Scopo
Valutare lo stato del repository Git, la chiarezza della cronologia, la strategia dei rami e i rischi operativi.

## Procedura
1. Verificare ramo predefinito, stato del working tree e file ignorati.
2. Analizzare cronologia, messaggi di commit e dimensione delle modifiche.
3. Controllare presenza di file binari pesanti, segreti, artefatti e file generati.
4. Valutare strategia di branch, tag, release e pull request.
5. Verificare conflitti ricorrenti, merge non lineari e commit di correzione ripetitivi.
6. Controllare protezioni del ramo principale e verifiche obbligatorie.
7. Produrre un piano con interventi ordinati per rischio.

## Controlli minimi
- repository pulito;
- `.gitignore` coerente;
- nessun segreto nella cronologia recente;
- commit leggibili e verificabili;
- tag e versioni coerenti;
- strategia dei rami documentata.

## Output
Rapporto con rischi, anomalie della cronologia, interventi consigliati e regole operative future.