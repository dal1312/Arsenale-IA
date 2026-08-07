# ARI-0101 — Revisione Python

- **Categoria:** Sistemi e sviluppo
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.2.0
- **Utilizzo offline:** Sì

## Scopo

Valutare qualità, correttezza, manutenibilità, packaging e compatibilità di un progetto Python esistente.

## Campo di applicazione

Applicazioni, librerie, servizi, script, CLI e progetti Python multipiattaforma.

## Quando usarla

- prima di una funzionalità importante o rilascio
- durante una migrazione di versione Python
- quando test, dipendenze o packaging risultano fragili

## Quando non usarla

- serve diagnosticare un singolo errore riproducibile
- l'ambito è una sola patch e basta ARI-0002
- si vuole modificare subito il codice senza revisione

## Prerequisiti

- accesso al progetto
- versioni Python dichiarate o deducibili
- strumento di gestione dipendenze identificabile
- ambiente sufficiente per eseguire almeno parte delle verifiche

## Materiale necessario

- pyproject.toml e/o requirements
- file di lock e configurazioni ambiente
- suite di test
- configurazioni lint/type check/build
- documentazione di installazione e packaging

## Procedura operativa

1. Identificare versione Python, entry point, struttura pacchetti e gestione dipendenze.
2. Verificare pyproject.toml, requirements, file ambiente e blocco versioni.
3. Eseguire quando disponibili test, type check, analisi statica e build.
4. Controllare import circolari, eccezioni, risorse, concorrenza e side effect all'import.
5. Verificare portabilità Windows/Linux, encoding, percorsi, temporanei e configurazione.
6. Analizzare dipendenze, segreti, deserializzazione, comandi di sistema e input esterni.
7. Produrre piano prioritizzato senza modificare il codice durante la revisione.

## Controlli

- struttura moduli coerente
- ambiente riproducibile
- dipendenze dichiarate e necessarie
- test eseguibili
- errori gestiti esplicitamente
- nessun segreto nel repository
- compatibilità dichiarata verificabile

## Errori frequenti

- confondere problemi di ambiente con difetti del codice
- ignorare file di lock o packaging
- forzare aggiornamenti di tutte le dipendenze insieme
- trascurare differenze Windows/Linux
- modificare codice durante la fase di revisione

## Rapporto finale

Indicare versione Python, strumenti dipendenze, esito installazione, test, lint/type check/build, problemi con priorità P0-P4, test mancanti, rischi di migrazione e ordine di intervento.

## Condizioni di uscita

- ambiente e versioni compresi
- test e dipendenze verificati o marcati non verificabili
- packaging analizzato
- rischi principali prioritizzati
- piano operativo prodotto

## Cronologia delle versioni

- **0.2.0** — Struttura uniformata a `STANDARD.md`; requisiti, controlli, rapporto e condizioni di uscita resi espliciti.
- **0.1.0** — Prima versione operativa.
