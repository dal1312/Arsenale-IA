# ARI-0010 — Preparazione al rilascio

- **Categoria:** Nucleo
- **Livello:** L5 Audit
- **Stato:** Bozza verificabile
- **Versione:** 0.2.0
- **Utilizzo offline:** Sì

## Scopo

Verificare che una versione sia tecnicamente pronta per la distribuzione e disponga di controlli, artefatti, istruzioni operative e recupero adeguati.

## Campo di applicazione

Release candidate di applicazioni, servizi, librerie, immagini, pacchetti e distribuzioni con artefatti identificabili.

## Quando usarla

- esiste una versione candidata
- si sta per pubblicare o distribuire un artefatto
- sono necessarie decisione go/no-go, note e rollback

## Quando non usarla

- la funzionalità non ha ancora superato implementazione e test
- non esiste un artefatto o commit candidato identificato
- manca ancora una decisione architetturale fondamentale

## Prerequisiti

- versione candidata e commit o tag identificabili
- criteri di accettazione
- pipeline di build disponibile
- configurazioni e dipendenze note

## Materiale necessario

- codice sorgente e artefatto candidato
- note di rilascio
- pipeline di build e test
- configurazioni e migrazioni
- procedure di installazione, aggiornamento, backup e ripristino

## Procedura operativa

1. Definire versione, contenuto e ambiente destinatario.
2. Verificare stato del repository e modifiche incluse.
3. Eseguire test, controllo statico, build e confezionamento da ambiente pulito.
4. Controllare versioni, dipendenze, licenze e file inclusi.
5. Verificare configurazioni, segreti, migrazioni e compatibilità.
6. Provare installazione, aggiornamento e avvio dell'artefatto reale.
7. Verificare log, metriche, errori e health check.
8. Preparare note, limitazioni e istruzioni operative.
9. Definire distribuzione graduale, backup e ripristino.
10. Registrare approvazione o motivi del rinvio.

## Controlli

- test critici superati
- build riproducibile
- artefatto installabile
- migrazioni verificate
- nessuna vulnerabilità grave nota non accettata
- rollback o recupero disponibile per modifiche irreversibili
- documentazione operativa sufficiente

## Errori frequenti

- verificare solo il codice e non l'artefatto
- cambiare dipendenze dopo i test
- pubblicare senza versione coerente
- considerare rollback una semplice reinstallazione
- ignorare compatibilità e dati persistenti

## Rapporto finale

Registrare versione, commit/tag, esito test e build, artefatti verificati, installazione/aggiornamento, sicurezza e configurazioni, note di rilascio, limitazioni, piano di distribuzione e ripristino. Verdetto: RILASCIO APPROVATO, APPROVATO CON LIMITAZIONI o RILASCIO BLOCCATO.

## Condizioni di uscita

- commit o tag identificato
- test e build superati
- artefatto verificato
- installazione o aggiornamento provati
- sicurezza e configurazioni controllate
- note e rollback disponibili
- decisione finale registrata

## Cronologia delle versioni

- **0.2.0** — Struttura uniformata a `STANDARD.md`; requisiti, controlli, rapporto e condizioni di uscita resi espliciti.
- **0.1.0** — Prima versione operativa.
