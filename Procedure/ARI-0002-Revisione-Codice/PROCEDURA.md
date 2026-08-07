# ARI-0002 — Revisione del codice

- **Categoria:** Nucleo
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.2.0
- **Utilizzo offline:** Sì

## Scopo

Valutare una modifica o un insieme di file per individuare difetti di correttezza, manutenibilità, sicurezza e aderenza ai requisiti.

## Campo di applicazione

Patch, commit, pull request, moduli o gruppi limitati di file già modificati. La procedura riguarda la qualità della modifica, non l'intero repository.

## Quando usarla

- prima di merge, rilascio o consegna
- dopo modifiche importanti o rischiose
- quando serve una valutazione indipendente rispetto a requisito o ticket

## Quando non usarla

- il problema è un errore non ancora riprodotto: usare ARI-0003
- serve una revisione complessiva del progetto: usare ARI-0001
- l'obiettivo è implementare direttamente una specifica approvata: usare ARI-0005

## Prerequisiti

- ambito della modifica identificato
- baseline o punto di confronto disponibile
- requisito, specifica o ticket collegato quando esiste
- ambiente sufficiente per test, controlli statici o build

## Materiale necessario

- diff o file interessati
- requisiti e criteri di accettazione
- test pertinenti
- output di lint, type check, build o CI se disponibili

## Procedura operativa

1. Definire ambito e punto di confronto.
2. Leggere requisito, specifica o ticket collegato.
3. Esaminare la modifica file per file e seguire i flussi principali.
4. Verificare casi limite, gestione errori, input, autorizzazioni e dati sensibili.
5. Cercare duplicazioni, responsabilità mescolate, dipendenze inutili e regressioni.
6. Verificare test esistenti e test mancanti.
7. Eseguire test, controlli statici e build quando disponibili.
8. Classificare i rilievi e produrre il rapporto senza riscrivere automaticamente il codice.

## Controlli

- ogni rilievo indica file o simbolo ed evidenza concreta
- la gravità riflette impatto e probabilità, non preferenze personali
- la modifica è confrontata con il requisito
- i test mancanti sono descritti con comportamento atteso
- nessun codice è modificato automaticamente durante la revisione

### Classificazione dei rilievi

- **Bloccante:** impedisce utilizzo o rilascio
- **Critica:** rischio elevato di errore, perdita dati o vulnerabilità
- **Alta:** regressione probabile o forte debito tecnico
- **Media:** problema reale ma non urgente
- **Bassa:** miglioramento facoltativo

## Errori frequenti

- confondere preferenze stilistiche con difetti
- commentare file fuori ambito senza motivo
- dichiarare una regressione senza ricostruire il flusso
- proporre grandi riscritture dove basta una correzione locale
- ignorare i test perché la patch sembra semplice

## Rapporto finale

Per ogni rilievo indicare identificativo, titolo, gravità, file e funzione, evidenza, impatto, correzione consigliata e test richiesto. Concludere con sintesi, punti di forza, rischi residui e verdetto sulla modifica.

## Condizioni di uscita

- ambito e requisito documentati
- verifiche eseguite registrate
- rilievi prioritizzati con evidenze
- test mancanti identificati
- verdetto finale prodotto

## Cronologia delle versioni

- **0.2.0** — Struttura uniformata a `STANDARD.md` preservando la classificazione dei rilievi.
- **0.1.0** — Prima versione operativa.
