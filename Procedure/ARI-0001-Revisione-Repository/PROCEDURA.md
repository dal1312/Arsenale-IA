# ARI-0001 — Revisione repository

- **Categoria:** Nucleo
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.2.0
- **Utilizzo offline:** Sì

## Scopo

Analizzare un repository software esistente, comprenderne struttura e stato reale, individuare problemi verificabili e produrre un piano di miglioramento prioritizzato senza modificare subito il codice.

## Campo di applicazione

Repository applicativi, librerie, servizi, strumenti CLI, progetti multipiattaforma e monorepo. La procedura copre struttura, build, test, qualità del codice, sicurezza, prestazioni, documentazione e rilascio.

## Quando usarla

- si eredita un progetto o si entra in una base di codice poco conosciuta
- si prepara una modifica importante o un hardening
- documentazione e implementazione potrebbero non essere allineate
- serve una fotografia tecnica prima di pianificare interventi

## Quando non usarla

- la causa di un singolo errore è già il problema principale: usare ARI-0003
- esiste già un piano approvato e occorre solo implementarlo: usare ARI-0005
- si vuole modificare il codice durante la stessa fase di revisione

## Prerequisiti

- accesso ai file del progetto
- indicazioni sullo scopo del software e sui sistemi supportati
- strumenti necessari per build e test, quando disponibili
- permesso esplicito prima di applicare modifiche

## Materiale necessario

- repository o copia di lavoro
- README, specifiche, ticket e documentazione disponibile
- comandi di installazione, build, test e avvio
- log e output prodotti durante le verifiche

## Procedura operativa

1. Identificare scopo, linguaggi, framework, entry point, piattaforme, dipendenze e servizi esterni.
2. Mappare sorgenti, test, configurazioni, documentazione, script, CI/CD, Docker e artefatti generati.
3. Eseguire quando possibile installazione dipendenze, lint, controllo tipi, test, build e avvio locale; registrare comando ed esito.
4. Analizzare responsabilità dei moduli, accoppiamento, duplicazioni, complessità, gestione errori, side effect, codice morto e dipendenze circolari.
5. Valutare test, casi limite, instabilità e dipendenze da rete, tempo o ordine di esecuzione.
6. Controllare sicurezza, configurazioni, segreti, validazione input e dipendenze vulnerabili quando pertinenti.
7. Segnalare prestazioni solo sulla base di evidenze o necessità di misurazione.
8. Verificare README, installazione, versionamento, CI/CD, pacchettizzazione e rilascio.
9. Classificare i rilievi da P0 a P4 e costruire il piano di miglioramento senza applicarlo.

## Controlli

- ogni problema importante dispone di file, simbolo o prova osservabile
- bug confermati, rischi, debito tecnico e preferenze stilistiche sono distinti
- build e test sono eseguiti oppure l'impossibilità è motivata
- nessuna modifica è applicata nella fase di revisione
- i componenti stabili e da non toccare sono esplicitati

## Errori frequenti

- iniziare subito il refactoring
- criticare lo stile senza dimostrare un impatto
- dichiarare test superati senza dati
- ignorare parti stabili del progetto
- presentare supposizioni come vulnerabilità confermate

## Rapporto finale

Produrre: sintesi esecutiva; mappa del repository; esito di build e test; problemi con priorità P0-P4 ed evidenze; punti di forza; piano di miglioramento; ticket proposti; ordine consigliato; componenti da non modificare; verdetto finale. Verdetti ammessi: NON AVVIABILE, INSTABILE, FUNZIONANTE CON PROBLEMI CRITICI, FUNZIONANTE MA DA CONSOLIDARE, BUONO, PRONTO PER HARDENING, PRONTO PER PRODUZIONE.

## Condizioni di uscita

- repository mappato
- build e test eseguiti o impedimenti documentati
- rilievi importanti supportati da evidenza
- piano prioritizzato prodotto
- nessuna modifica applicata senza approvazione

## Cronologia delle versioni

- **0.2.0** — Struttura uniformata a `STANDARD.md`; requisiti, controlli, rapporto e condizioni di uscita resi espliciti.
- **0.1.0** — Prima versione operativa.
