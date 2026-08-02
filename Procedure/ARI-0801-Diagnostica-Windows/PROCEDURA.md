# ARI-0801 — Diagnostica Windows

## Scopo
Diagnosticare problemi di avvio, prestazioni, compatibilità e configurazione su Windows senza applicare modifiche indiscriminate.

## Procedura
1. Raccogliere versione Windows, hardware, driver, aggiornamenti e sintomo osservato.
2. Riprodurre il problema e annotare orario, messaggi, processi e condizioni.
3. Consultare Visualizzatore eventi, Affidabilità, Gestione attività e log applicativi pertinenti.
4. Verificare servizi, elementi di avvio, spazio disco, memoria, CPU, GPU e rete.
5. Controllare integrità dei file applicativi e dipendenze richieste.
6. Isolare il problema con avvio pulito o configurazione minima, quando appropriato.
7. Formulare ipotesi ordinate per probabilità e testarle una alla volta.
8. Applicare una correzione reversibile e verificare la regressione.

## Regole
- non modificare il registro senza backup e motivazione;
- non disattivare servizi casualmente;
- non aggiornare driver se il problema non è correlato;
- registrare ogni modifica applicata.

## Output
Diagnosi con causa confermata o probabile, evidenze, correzione, verifica e procedura di ripristino.