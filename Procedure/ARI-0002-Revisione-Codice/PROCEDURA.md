# ARI-0002 — Revisione del codice

## Scopo
Valutare una modifica o un insieme di file per individuare difetti di correttezza, manutenzione, sicurezza e aderenza ai requisiti.

## Quando usarla
Prima di unione, rilascio o consegna; dopo modifiche importanti; quando serve una valutazione indipendente.

## Quando non usarla
Non sostituisce la diagnosi di un errore non ancora riprodotto né una revisione completa dell'intero repository.

## Procedura
1. Definire l'ambito e il punto di confronto.
2. Leggere requisito, specifica o ticket collegato.
3. Esaminare la modifica file per file.
4. Verificare correttezza dei flussi principali e dei casi limite.
5. Controllare gestione errori, input, autorizzazioni e dati sensibili.
6. Cercare duplicazioni, responsabilità mescolate e dipendenze inutili.
7. Verificare i test esistenti e quelli mancanti.
8. Eseguire test, controlli statici e build quando disponibili.
9. Classificare i rilievi per gravità.
10. Produrre il rapporto finale senza riscrivere automaticamente il codice.

## Classificazione
- Bloccante: impedisce utilizzo o rilascio.
- Critica: rischio elevato di errore, perdita dati o vulnerabilità.
- Alta: regressione probabile o forte debito tecnico.
- Media: problema reale ma non urgente.
- Bassa: miglioramento facoltativo.

## Formato di ogni rilievo
- identificativo;
- titolo;
- gravità;
- file e funzione;
- evidenza;
- impatto;
- correzione consigliata;
- test richiesto.

## Condizioni di uscita
La procedura è conclusa solo se ambito, requisiti, verifiche eseguite, rilievi e verdetto sono documentati.