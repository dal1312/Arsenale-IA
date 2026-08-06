---
name: revisione-docker
description: Revisiona Dockerfile e configurazioni Docker per correttezza, sicurezza, riproducibilità e manutenibilità. Usa su immagini, Compose, servizi, reti e volumi prima della distribuzione.
---

# Revisione Docker

Segui integralmente la procedura descritta in `PROCEDURA.md` nella stessa cartella.

## Comportamento obbligatorio

- Identifica Dockerfile, Compose, immagini, servizi, reti e volumi.
- Verifica versioni, contesto di build, `.dockerignore` e riproducibilità.
- Controlla privilegi, segreti, permessi, porte e persistenza.
- Esegui build e avvio quando possibile registrando esito e tempi.
- Verifica health check, arresto pulito e comportamento ai guasti pertinenti.
- Produci un piano di correzione prioritizzato.
