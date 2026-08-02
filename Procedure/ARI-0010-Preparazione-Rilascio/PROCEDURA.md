# ARI-0010 — Preparazione al rilascio

## Scopo
Verificare che una versione sia tecnicamente pronta per essere distribuita e che esistano controlli, artefatti e procedure di recupero adeguati.

## Input
- versione candidata;
- codice sorgente;
- note di rilascio;
- pipeline di build;
- configurazioni e dipendenze;
- criteri di accettazione.

## Output
- decisione di rilascio;
- elenco dei blocchi;
- artefatti verificati;
- note di rilascio;
- piano di distribuzione e ripristino.

## Procedura
1. Definire versione, contenuto e ambiente destinatario.
2. Verificare stato del repository e modifiche incluse.
3. Eseguire test, controllo statico, build e confezionamento da ambiente pulito.
4. Controllare versioni, dipendenze, licenze e file inclusi.
5. Verificare configurazioni, segreti, migrazioni e compatibilità.
6. Provare installazione, aggiornamento e avvio dell'artefatto reale.
7. Verificare log, metriche, gestione errori e controlli di salute.
8. Preparare note di rilascio, limitazioni note e istruzioni operative.
9. Definire distribuzione graduale, backup e ripristino.
10. Registrare approvazione oppure motivi del rinvio.

## Blocchi al rilascio
- test critici falliti;
- build non riproducibile;
- vulnerabilità grave nota;
- migrazione non verificata;
- artefatto non installabile;
- assenza di recupero per modifiche irreversibili;
- documentazione operativa insufficiente.

## Errori frequenti
- verificare solo il codice e non l'artefatto finale;
- cambiare dipendenze dopo i test;
- pubblicare senza note o numero di versione coerente;
- considerare il rollback come semplice reinstallazione;
- ignorare compatibilità e dati persistenti.

## Condizioni di uscita
- [ ] commit o tag identificato;
- [ ] test e build superati;
- [ ] artefatti verificati;
- [ ] installazione o aggiornamento provati;
- [ ] sicurezza e configurazioni controllate;
- [ ] note e limitazioni pubblicabili;
- [ ] piano di ripristino disponibile;
- [ ] decisione finale registrata.

## Verdetto
Usare uno dei seguenti: `RILASCIO APPROVATO`, `APPROVATO CON LIMITAZIONI`, `RILASCIO BLOCCATO`.
