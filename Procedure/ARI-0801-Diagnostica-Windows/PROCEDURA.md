# ARI-0801 — Diagnostica Windows

- **Categoria:** Sistemi e sviluppo
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.2.0
- **Utilizzo offline:** Sì

## Scopo

Diagnosticare problemi di avvio, prestazioni, compatibilità e configurazione su Windows senza applicare modifiche indiscriminate.

## Campo di applicazione

Windows desktop/server, applicazioni, servizi, driver, risorse di sistema, eventi e dipendenze con sintomi osservabili.

## Quando usarla

- un'applicazione o servizio non parte o si comporta in modo anomalo
- esistono problemi di prestazioni o compatibilità
- serve isolare una causa legata a configurazione, driver o risorse

## Quando non usarla

- non esiste un sintomo concreto
- si vuole applicare pulizia o tweak generici senza diagnosi
- il problema è chiaramente interno al codice e riproducibile fuori da Windows

## Prerequisiti

- versione Windows e hardware identificabili
- sintomo e comportamento atteso descritti
- accesso ai log o agli strumenti di sistema pertinenti
- possibilità di applicare solo modifiche autorizzate e reversibili

## Materiale necessario

- Visualizzatore eventi e Cronologia affidabilità
- Gestione attività/Monitoraggio risorse
- log applicativi
- informazioni driver e aggiornamenti
- configurazioni e dipendenze dell'applicazione

## Procedura operativa

1. Raccogliere versione Windows, hardware, driver, aggiornamenti e sintomo.
2. Riprodurre il problema annotando orario, messaggi, processi e condizioni.
3. Consultare eventi, affidabilità, attività e log pertinenti.
4. Verificare servizi, avvio, disco, memoria, CPU, GPU e rete.
5. Controllare integrità dei file applicativi e dipendenze.
6. Isolare con configurazione minima o avvio pulito quando appropriato.
7. Formulare ipotesi ordinate e testarle una alla volta.
8. Applicare una correzione reversibile e verificare la regressione.

## Controlli

- ogni modifica registrata
- registro di sistema modificato solo con backup e motivo
- servizi non disattivati casualmente
- driver aggiornati solo se correlati
- procedura di ripristino disponibile

## Errori frequenti

- eseguire tweak generici
- modificare più servizi insieme
- aggiornare driver senza relazione col sintomo
- cancellare log o evidenze
- dichiarare risolto senza riprodurre il flusso

## Rapporto finale

Indicare ambiente Windows, sintomo, riproduzione, evidenze, ipotesi testate, causa confermata o probabile, modifica applicata, verifica e procedura di ripristino.

## Condizioni di uscita

- sintomo riprodotto o impedimento spiegato
- causa confermata o probabilità motivata
- correzione reversibile verificata quando applicata
- ripristino documentato
- evidenze conservate

## Cronologia delle versioni

- **0.2.0** — Struttura uniformata a `STANDARD.md`; requisiti, controlli, rapporto e condizioni di uscita resi espliciti.
- **0.1.0** — Prima versione operativa.
