---
name: refactoring-controllato
description: Migliora la struttura interna del software preservando il comportamento osservabile. Usa quando esistono evidenze di un problema strutturale e verifiche sufficienti contro le regressioni.
---

# Refactoring controllato

Segui integralmente la procedura descritta in `PROCEDURA.md` nella stessa cartella.

## Comportamento obbligatorio

- Definisci il comportamento esterno da preservare.
- Rafforza i test di caratterizzazione prima delle trasformazioni.
- Applica una trasformazione significativa alla volta.
- Esegui test, controlli statici e build dopo ogni passaggio.
- Non introdurre nuove funzionalità durante il refactoring.
- Documenta benefici verificabili e rischi residui.
