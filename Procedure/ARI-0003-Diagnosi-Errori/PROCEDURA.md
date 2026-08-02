# ARI-0003 — Diagnosi degli errori

## Scopo
Individuare la causa reale di un malfunzionamento prima di applicare correzioni.

## Principio
Non correggere il primo sintomo osservato. Riprodurre, ridurre e misurare il problema.

## Procedura
1. Raccogliere comportamento atteso e comportamento reale.
2. Registrare ambiente, versione, input e messaggio di errore.
3. Riprodurre il problema in modo affidabile.
4. Ridurre il caso fino al minimo esempio utile.
5. Separare fatti, ipotesi e informazioni mancanti.
6. Formulare poche ipotesi verificabili.
7. Aggiungere log o misurazioni mirate.
8. Verificare un'ipotesi alla volta.
9. Identificare la causa radice.
10. Applicare la correzione minima coerente.
11. Aggiungere un test di regressione.
12. Eseguire la suite pertinente e documentare l'esito.

## Informazioni obbligatorie
- passaggi di riproduzione;
- frequenza del problema;
- versione interessata;
- log essenziali;
- causa confermata o livello di incertezza;
- modifica applicata;
- test aggiunti.

## Errori frequenti
- modificare più parti contemporaneamente;
- affidarsi solo allo stack trace;
- eliminare un controllo per far passare il test;
- cambiare il test senza verificare il requisito;
- dichiarare risolto senza prova di regressione.

## Condizioni di uscita
Il problema è riprodotto, la causa è documentata, la correzione è verificata e un test impedisce il ritorno dello stesso errore.