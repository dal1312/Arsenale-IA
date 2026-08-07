# ARI-0701 — Revisione Docker

- **Categoria:** Sistemi e sviluppo
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.2.0
- **Utilizzo offline:** Sì

## Scopo

Valutare correttezza, sicurezza, riproducibilità e manutenibilità di immagini e configurazioni Docker.

## Campo di applicazione

Dockerfile, Compose, immagini, reti, volumi, health check, build context e configurazioni di runtime container.

## Quando usarla

- si prepara una release containerizzata
- build o avvio Docker sono fragili
- si vuole ridurre privilegi, dimensioni o rischi di configurazione

## Quando non usarla

- il problema principale è nel codice applicativo non containerizzato
- manca accesso a Dockerfile/Compose e si pretendono conclusioni definitive
- si vuole aggiornare tutte le immagini senza verificarne compatibilità

## Prerequisiti

- Dockerfile o configurazioni disponibili
- versioni delle immagini di base identificabili
- Docker disponibile quando è necessario provare build e avvio
- scopo dei servizi e dati persistenti compreso

## Materiale necessario

- Dockerfile e compose
- file .dockerignore
- configurazioni ambiente e segreti senza esporli
- log build/runtime
- inventario immagini, volumi, reti e porte

## Procedura operativa

1. Identificare Dockerfile, Compose, immagini, servizi e volumi.
2. Verificare versioni fissate, multi-stage, build context e .dockerignore.
3. Controllare utente non privilegiato, segreti e permessi.
4. Verificare health check, dipendenze, reti, porte e persistenza.
5. Analizzare dimensione immagini, cache, layer e pacchetti superflui.
6. Eseguire build e avvio quando possibile e registrare errori e tempi.
7. Verificare logging, arresto pulito, riavvio e perdita di un servizio.

## Controlli

- build riproducibile
- immagini base esplicite
- segreti non incorporati
- privilegi minimi
- volumi e reti documentati
- health check presenti dove utili
- avvio e arresto verificabili

## Errori frequenti

- usare latest senza motivazione
- incorporare segreti in ARG/ENV o layer
- eseguire come root senza necessità
- ottimizzare solo la dimensione ignorando sicurezza
- dichiarare pronta un'immagine mai avviata

## Rapporto finale

Riportare immagini di base, esito build/avvio, privilegi, segreti, reti, volumi, health check, dimensioni, rischi di sicurezza e piano di correzione.

## Condizioni di uscita

- configurazioni comprese
- build verificata o impedimento motivato
- runtime essenziale provato quando possibile
- rischi prioritizzati
- piano operativo prodotto

## Cronologia delle versioni

- **0.2.0** — Struttura uniformata a `STANDARD.md`; requisiti, controlli, rapporto e condizioni di uscita resi espliciti.
- **0.1.0** — Prima versione operativa.
