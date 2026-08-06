---
name: diagnosi-errori
description: Diagnostica malfunzionamenti riproducibili individuando la causa radice prima di correggere. Usa quando esiste un errore concreto, un comportamento inatteso o una regressione da isolare.
---

# Diagnosi errori

Segui integralmente la procedura descritta in `PROCEDURA.md` nella stessa cartella.

## Comportamento obbligatorio

- Raccogli comportamento atteso, comportamento reale, ambiente e versione.
- Riproduci e riduci il problema prima di modificare il codice.
- Separa fatti, ipotesi e informazioni mancanti.
- Verifica una sola ipotesi alla volta.
- Applica la correzione minima coerente con la causa confermata.
- Aggiungi un test di regressione e registra l'esito finale.
