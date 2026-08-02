# ARI-0006 — Refactoring controllato

## Scopo
Migliorare la struttura interna del software senza alterarne il comportamento osservabile.

## Quando usarla
- codice duplicato o difficile da comprendere;
- moduli con responsabilità confuse;
- modifiche semplici che richiedono interventi in troppi file;
- test sufficienti a rilevare regressioni.

## Quando non usarla
- in presenza di bug critici non compresi;
- senza verifiche minime disponibili;
- quando l'obiettivo reale è aggiungere una nuova funzione;
- durante una modifica urgente non isolata.

## Input
- codice interessato;
- test esistenti;
- motivazione del refactoring;
- confini della modifica.

## Output
- codice più semplice;
- comportamento invariato;
- test eseguiti;
- rapporto con benefici e rischi residui.

## Procedura
1. Definire il comportamento da preservare.
2. Individuare il problema strutturale con evidenze.
3. Delimitare file e funzioni coinvolti.
4. Scrivere o rafforzare i test di caratterizzazione.
5. Applicare una sola trasformazione significativa alla volta.
6. Eseguire test, controllo statico e build dopo ogni passaggio.
7. Confrontare complessità, dipendenze e leggibilità prima e dopo.
8. Aggiornare documentazione e nomi pubblici, se necessario.

## Trasformazioni ammesse
- estrazione di funzione o modulo;
- rinomina motivata;
- eliminazione di duplicazione reale;
- riduzione di annidamenti;
- separazione di responsabilità;
- rimozione di codice morto verificato.

## Errori frequenti
- mescolare refactoring e nuove funzioni;
- creare astrazioni premature;
- dividere file solo perché sono lunghi;
- eliminare codice senza cercarne gli utilizzatori;
- dichiarare invariato il comportamento senza test.

## Condizioni di uscita
- [ ] comportamento esterno invariato;
- [ ] test pertinenti superati;
- [ ] build riuscita;
- [ ] complessità non aumentata;
- [ ] nessuna nuova dipendenza non necessaria;
- [ ] rapporto finale prodotto.

## Rapporto finale
Indicare: motivazione, file modificati, trasformazioni eseguite, verifiche, benefici misurabili, rischi residui e decisione finale.
