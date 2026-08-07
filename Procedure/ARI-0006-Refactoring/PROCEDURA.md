# ARI-0006 — Refactoring controllato

- **Categoria:** Nucleo
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.2.0
- **Utilizzo offline:** Sì

## Scopo

Migliorare la struttura interna del software senza alterarne il comportamento osservabile.

## Campo di applicazione

Codice duplicato, moduli con responsabilità confuse, dipendenze eccessive, annidamenti complessi, nomi fuorvianti e codice morto verificato.

## Quando usarla

- il comportamento corrente è compreso e deve restare invariato
- esistono test sufficienti o possono essere aggiunti test di caratterizzazione
- un problema strutturale reale rende più costose le modifiche

## Quando non usarla

- esistono bug critici non compresi
- mancano verifiche minime sul comportamento
- l'obiettivo reale è aggiungere una nuova funzionalità
- la modifica urgente non è isolabile

## Prerequisiti

- comportamento da preservare definito
- confini della modifica identificati
- test esistenti o possibilità di crearne di caratterizzazione
- baseline di build e test disponibile

## Materiale necessario

- codice interessato
- test esistenti
- motivazione del refactoring
- metriche o evidenze del problema strutturale
- comandi di build e controllo statico

## Procedura operativa

1. Definire il comportamento da preservare.
2. Individuare il problema strutturale con evidenze.
3. Delimitare file e funzioni coinvolti.
4. Scrivere o rafforzare i test di caratterizzazione.
5. Applicare una sola trasformazione significativa alla volta.
6. Eseguire test, controllo statico e build dopo ogni passaggio.
7. Confrontare complessità, dipendenze e leggibilità prima e dopo.
8. Aggiornare documentazione e nomi pubblici se necessario.

## Controlli

- comportamento esterno invariato
- test pertinenti superati dopo ogni trasformazione
- build riuscita
- complessità non aumentata
- nessuna nuova dipendenza non necessaria
- codice morto rimosso solo dopo ricerca degli utilizzatori

### Trasformazioni ammesse

- estrazione di funzione o modulo
- rinomina motivata
- eliminazione di duplicazione reale
- riduzione di annidamenti
- separazione di responsabilità
- rimozione di codice morto verificato

## Errori frequenti

- mescolare refactoring e nuove funzioni
- creare astrazioni premature
- dividere file solo perché sono lunghi
- eliminare codice senza cercarne gli utilizzatori
- dichiarare invariato il comportamento senza test

## Rapporto finale

Indicare motivazione, confini, file modificati, trasformazioni eseguite, verifiche prima/dopo, benefici misurabili, rischi residui e decisione finale.

## Condizioni di uscita

- comportamento preservato
- test e build pertinenti verdi
- problema strutturale ridotto
- nessun ampliamento funzionale non richiesto
- rapporto finale prodotto

## Cronologia delle versioni

- **0.2.0** — Struttura uniformata a `STANDARD.md` preservando le trasformazioni ammesse.
- **0.1.0** — Prima versione operativa.
