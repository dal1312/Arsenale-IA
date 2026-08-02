# ARI-0001 — Revisione repository

- **Categoria:** Nucleo
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.1.0
- **Utilizzo offline:** Sì

## Scopo

Analizzare un repository software esistente, comprenderne struttura e stato reale, individuare problemi verificabili e produrre un piano di miglioramento prioritizzato senza modificare subito il codice.

## Quando usarla

Usare questa procedura quando:

- si eredita un progetto;
- si prepara una modifica importante;
- si deve valutare la qualità del codice;
- si vuole conoscere lo stato reale prima di una release;
- documentazione e implementazione potrebbero non essere allineate.

## Quando non usarla

Non usarla come sostituto della diagnosi di un singolo errore già riproducibile o quando esiste già un piano approvato e occorre soltanto implementarlo.

## Prerequisiti

- accesso ai file del progetto;
- indicazioni sullo scopo del software;
- strumenti necessari per build e test, quando disponibili;
- permesso esplicito prima di applicare modifiche.

## Regole operative

1. Non modificare il codice durante la fase di analisi.
2. Non inventare problemi.
3. Distinguere bug confermati, rischi, debito tecnico e preferenze stilistiche.
4. Citare file, funzioni e prove.
5. Registrare i comandi eseguiti e il loro esito.
6. Non dichiarare il progetto pronto per produzione senza prove sufficienti.

## Procedura

### 1. Identificazione

Raccogliere:

- scopo del progetto;
- linguaggi e framework;
- punto di ingresso;
- sistemi supportati;
- dipendenze principali;
- servizi esterni;
- modalità di distribuzione.

### 2. Mappa del repository

Individuare:

- codice sorgente;
- test;
- configurazioni;
- documentazione;
- script;
- pipeline CI/CD;
- file Docker;
- artefatti generati;
- aree critiche.

### 3. Verifica dello stato reale

Quando possibile eseguire:

- installazione dipendenze;
- lint;
- controllo tipi;
- test unitari;
- test di integrazione;
- build;
- avvio locale.

Per ogni comando annotare comando, esito, durata, avvisi ed errore principale.

### 4. Analisi del codice

Controllare:

- responsabilità dei moduli;
- accoppiamento;
- duplicazioni;
- funzioni e classi troppo complesse;
- gestione errori;
- configurazioni replicate;
- side effect nascosti;
- codice morto;
- dipendenze circolari.

### 5. Analisi dei test

Verificare:

- copertura delle funzioni critiche;
- qualità delle asserzioni;
- casi limite;
- test intermittenti;
- dipendenze da rete o ordine di esecuzione;
- test di regressione mancanti.

### 6. Sicurezza

Controllare, quando pertinenti:

- segreti nel codice;
- autenticazione e autorizzazione;
- validazione input;
- gestione file;
- injection;
- replay;
- esposizione dati sensibili;
- dipendenze vulnerabili.

### 7. Prestazioni

Segnalare solo problemi osservati o punti che richiedono misurazione. Evitare ottimizzazioni premature.

### 8. Documentazione e rilascio

Verificare README, installazione, configurazione, comandi di test, versionamento, CI/CD, pacchettizzazione e procedura di rilascio.

## Classificazione delle priorità

- **P0:** bloccante
- **P1:** critica
- **P2:** alta
- **P3:** media
- **P4:** bassa

## Scheda obbligatoria del problema

Per ogni problema indicare:

- identificativo;
- titolo;
- priorità;
- categoria;
- file e funzione;
- evidenza;
- impatto;
- correzione consigliata;
- test richiesti;
- stima;
- rischio della modifica;
- dipendenze.

## Rapporto finale

Il rapporto deve contenere:

1. sintesi esecutiva;
2. mappa del repository;
3. esito di build e test;
4. problemi trovati;
5. punti di forza;
6. piano di miglioramento;
7. ticket proposti;
8. ordine consigliato;
9. componenti da non modificare;
10. verdetto finale.

## Verdetti consentiti

- NON AVVIABILE
- INSTABILE
- FUNZIONANTE CON PROBLEMI CRITICI
- FUNZIONANTE MA DA CONSOLIDARE
- BUONO
- PRONTO PER HARDENING
- PRONTO PER PRODUZIONE

## Condizioni di uscita

La procedura è conclusa solo quando:

- il repository è stato mappato;
- build e test sono stati eseguiti oppure ne è stata spiegata l'impossibilità;
- ogni problema importante dispone di evidenza;
- è stato prodotto un piano prioritizzato;
- nessuna modifica è stata applicata senza approvazione.

## Errori frequenti dell'IA

- iniziare subito il refactoring;
- criticare lo stile senza dimostrare un impatto;
- dichiarare test superati senza numeri;
- ignorare parti stabili del progetto;
- confondere documentazione obsoleta con codice errato;
- presentare supposizioni come vulnerabilità confermate.

## Cronologia

- 0.1.0 — Prima versione operativa.
