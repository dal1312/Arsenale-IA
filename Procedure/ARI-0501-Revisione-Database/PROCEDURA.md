# ARI-0501 — Revisione database

## Scopo
Valutare schema, query, migrazioni, integrità, prestazioni, sicurezza e operatività di un database utilizzato da un'applicazione.

## Campo di applicazione
Database relazionali e non relazionali, inclusi SQLite, PostgreSQL, MySQL, SQL Server, Redis e MongoDB.

## Procedura
1. Identificare motore, versione, schema, modalità di accesso e responsabilità applicative.
2. Verificare migrazioni, vincoli, chiavi, indici e gestione delle transazioni.
3. Analizzare query critiche con piani di esecuzione e dati rappresentativi.
4. Controllare consistenza, concorrenza, isolamento e gestione degli errori.
5. Verificare utenti, permessi, segreti, cifratura e accessi amministrativi.
6. Esaminare backup, ripristino, conservazione, monitoraggio e capacità.
7. Produrre interventi ordinati distinguendo correttezza, sicurezza e ottimizzazione.

## Controlli specifici
- schema versionato;
- migrazioni reversibili o con strategia di recupero;
- vincoli coerenti con il dominio;
- query parametrizzate;
- indici giustificati dai carichi reali;
- transazioni con confini chiari;
- backup verificati tramite prova di ripristino;
- privilegi minimi;
- dati sensibili protetti.

## Errori frequenti
- aggiungere indici senza analizzare scritture e selettività;
- affidare tutta l'integrità alla sola applicazione;
- modificare lo schema manualmente in produzione;
- usare dati minimi per valutare le prestazioni;
- dichiarare valido un backup mai ripristinato;
- ignorare lock, timeout e crescita dello spazio occupato.

## Rapporto finale
Riportare motore e versione, schema, stato migrazioni, query critiche, rischi di integrità e sicurezza, stato backup/ripristino e piano prioritizzato.

## Condizioni di uscita
- schema e accessi compresi;
- integrità verificata;
- query critiche misurate;
- backup e ripristino valutati;
- piano operativo prodotto.
