# ARI-0701 — Revisione Docker

## Scopo
Valutare correttezza, sicurezza, riproducibilità e manutenibilità di immagini e configurazioni Docker.

## Procedura
1. Identificare Dockerfile, file Compose, immagini di base, servizi e volumi.
2. Verificare versioni fissate, multi-stage build, contesto di build e `.dockerignore`.
3. Controllare esecuzione come utente non privilegiato, gestione segreti e permessi.
4. Verificare health check, dipendenze tra servizi, reti, porte e persistenza.
5. Analizzare dimensione immagini, cache, layer inutili e pacchetti superflui.
6. Eseguire build e avvio quando possibile; registrare errori e tempi.
7. Verificare logging, arresto pulito, riavvio e comportamento dopo perdita di un servizio.

## Controlli minimi
- build riproducibile;
- immagini di base esplicite;
- segreti non incorporati;
- privilegi minimi;
- volumi e reti documentati;
- health check presenti dove utili;
- procedure di avvio e arresto verificabili.

## Output
Rapporto con rischi di sicurezza, problemi di build, sprechi di risorse e piano di correzione prioritizzato.