# ARI-0003 — Diagnosi degli errori

- **Categoria:** Nucleo
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.2.0
- **Utilizzo offline:** Sì

## Scopo

Individuare la causa reale di un malfunzionamento prima di applicare correzioni, usando riproduzione, riduzione e verifiche mirate.

## Campo di applicazione

Bug applicativi, errori di integrazione, regressioni, crash, comportamenti intermittenti e fallimenti di test con un sintomo osservabile.

## Quando usarla

- esiste un comportamento reale diverso da quello atteso
- un errore è riproducibile o esistono log sufficienti per tentare la riproduzione
- serve distinguere causa radice da sintomi secondari

## Quando non usarla

- non esiste ancora un sintomo concreto e serve una revisione generale
- la causa è già confermata e il lavoro consiste solo nell'implementare una correzione approvata
- l'obiettivo è ottimizzare prestazioni senza un errore funzionale

## Prerequisiti

- comportamento atteso definito
- accesso all'ambiente o a una riproduzione equivalente
- versione, input e condizioni iniziali identificabili
- possibilità di raccogliere log o misurazioni mirate

## Materiale necessario

- passaggi di riproduzione
- messaggi di errore e log pertinenti
- versione o commit interessato
- test esistenti e strumenti diagnostici disponibili

## Procedura operativa

1. Raccogliere comportamento atteso e reale.
2. Registrare ambiente, versione, input, frequenza e messaggio di errore.
3. Riprodurre il problema in modo affidabile.
4. Ridurre il caso fino al minimo esempio utile.
5. Separare fatti, ipotesi e informazioni mancanti.
6. Formulare poche ipotesi verificabili.
7. Aggiungere log o misurazioni mirate e verificare un'ipotesi alla volta.
8. Identificare la causa radice con evidenze.
9. Applicare la correzione minima coerente.
10. Aggiungere un test di regressione ed eseguire la suite pertinente.

## Controlli

- la causa è distinta dal primo sintomo osservato
- ogni ipotesi viene verificata separatamente
- le modifiche diagnostiche non alterano il comportamento in modo non controllato
- la correzione minima elimina la causa e non solo il messaggio di errore
- esiste una prova di regressione dopo la correzione

## Errori frequenti

- modificare più parti contemporaneamente
- affidarsi solo allo stack trace
- eliminare un controllo per far passare un test
- cambiare il test senza verificare il requisito
- dichiarare risolto senza prova di regressione

## Rapporto finale

Riportare passaggi di riproduzione, frequenza, ambiente e versione, log essenziali, ipotesi considerate, causa confermata o livello di incertezza, modifica applicata, test aggiunti ed esito finale.

## Condizioni di uscita

- problema riprodotto o impossibilità motivata
- causa radice confermata oppure incertezza esplicitata
- correzione minima verificata quando applicabile
- test di regressione presente
- suite pertinente eseguita e documentata

## Cronologia delle versioni

- **0.2.0** — Struttura uniformata a `STANDARD.md`; requisiti, controlli, rapporto e condizioni di uscita resi espliciti.
- **0.1.0** — Prima versione operativa.
