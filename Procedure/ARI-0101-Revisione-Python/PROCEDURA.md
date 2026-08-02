# ARI-0101 — Revisione Python

## Scopo
Valutare qualità, correttezza, manutenibilità e compatibilità di un progetto Python esistente.

## Quando usarla
- prima di una nuova funzionalità importante;
- durante una migrazione di versione Python;
- quando test, dipendenze o packaging risultano fragili;
- prima di distribuire un'applicazione o una libreria.

## Procedura
1. Identificare versione Python, punto di ingresso, struttura dei pacchetti e strumenti di gestione dipendenze.
2. Verificare `pyproject.toml`, `requirements*.txt`, file ambiente e blocco delle versioni.
3. Eseguire, quando disponibili, test, controllo tipi, analisi statica e build del pacchetto.
4. Controllare import circolari, gestione eccezioni, uso di risorse, concorrenza e side effect all'importazione.
5. Verificare portabilità Windows/Linux, encoding, percorsi, file temporanei e gestione configurazione.
6. Analizzare sicurezza delle dipendenze, segreti, deserializzazione, comandi di sistema e input esterni.
7. Produrre un piano prioritizzato senza modificare il codice durante la revisione.

## Controlli minimi
- struttura dei moduli coerente;
- ambienti riproducibili;
- dipendenze dichiarate e necessarie;
- test eseguibili;
- errori gestiti in modo esplicito;
- nessun segreto nel repository;
- compatibilità dichiarata verificabile.

## Output
Rapporto con evidenze, priorità P0-P4, test mancanti, rischi di migrazione e ordine di intervento.

## Condizione di uscita
La procedura termina solo quando ambiente, test, dipendenze, packaging e principali rischi sono stati verificati o marcati come non verificabili con motivazione.