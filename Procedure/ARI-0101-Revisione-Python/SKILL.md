---
name: revisione-python
description: Revisiona un progetto Python per correttezza, manutenibilità, dipendenze, packaging e compatibilità. Usa prima di migrazioni, distribuzioni o modifiche importanti senza intervenire subito sul codice.
---

# Revisione Python

Segui integralmente la procedura descritta in `PROCEDURA.md` nella stessa cartella.

## Comportamento obbligatorio

- Identifica versione Python, struttura dei pacchetti, punto di ingresso e gestione dipendenze.
- Verifica ambiente, test, tipi, analisi statica e build quando disponibili.
- Controlla packaging, import, eccezioni, risorse e side effect all'importazione.
- Verifica portabilità Windows/Linux, percorsi ed encoding quando pertinenti.
- Cita evidenze e classifica i problemi da P0 a P4.
- Produci il piano senza modificare il codice durante la revisione.
