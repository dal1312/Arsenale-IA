# ARI-0501 — Revisione database

- **Categoria:** Sistemi e sviluppo
- **Livello:** L5 Audit
- **Stato:** Bozza verificabile
- **Versione:** 0.2.0
- **Utilizzo offline:** Sì

## Scopo

Valutare schema, query, migrazioni, integrità, prestazioni, sicurezza e operatività di un database usato da un'applicazione.

## Campo di applicazione

Database relazionali e non relazionali, inclusi SQLite, PostgreSQL, MySQL, SQL Server, Redis e MongoDB.

## Quando usarla

- si prepara una migrazione o release con cambi dati
- esistono query critiche o problemi di integrità
- si deve valutare backup, privilegi e operatività

## Quando non usarla

- non è disponibile un ambiente o schema rappresentativo e si pretendono conclusioni prestazionali definitive
- il problema è una sola query già isolata e basta una diagnosi mirata
- si vuole modificare direttamente produzione senza piano di recupero

## Prerequisiti

- motore e versione identificati
- schema o modello dati accessibile
- modalità di accesso applicativa compresa
- autorizzazione per analizzare dati e configurazioni

## Materiale necessario

- schema e migrazioni
- query critiche e piani di esecuzione
- configurazioni utenti/permessi
- procedure backup/ripristino
- metriche di capacità e monitoraggio

## Procedura operativa

1. Identificare motore, versione, schema, accessi e responsabilità applicative.
2. Verificare migrazioni, vincoli, chiavi, indici e transazioni.
3. Analizzare query critiche con piani di esecuzione e dati rappresentativi.
4. Controllare consistenza, concorrenza, isolamento ed error handling.
5. Verificare utenti, permessi, segreti, cifratura e accessi amministrativi.
6. Esaminare backup, ripristino, conservazione, monitoraggio e capacità.
7. Produrre interventi separando correttezza, sicurezza e ottimizzazione.

## Controlli

- schema versionato
- migrazioni reversibili o con recupero
- vincoli coerenti con il dominio
- query parametrizzate
- indici giustificati dai carichi
- transazioni con confini chiari
- backup verificati con restore
- privilegi minimi
- dati sensibili protetti

## Errori frequenti

- aggiungere indici senza valutare scritture e selettività
- affidare tutta l'integrità all'applicazione
- modificare schema manualmente in produzione
- usare dati minimi per prestazioni
- dichiarare valido un backup mai ripristinato
- ignorare lock, timeout e crescita spazio

## Rapporto finale

Riportare motore/versione, schema, migrazioni, query critiche, integrità, sicurezza, backup/ripristino, capacità e piano prioritizzato.

## Condizioni di uscita

- schema e accessi compresi
- integrità verificata
- query critiche misurate o marcate non misurabili
- backup e ripristino valutati
- piano operativo prodotto

## Cronologia delle versioni

- **0.2.0** — Struttura uniformata a `STANDARD.md`; requisiti, controlli, rapporto e condizioni di uscita resi espliciti.
- **0.1.0** — Prima versione operativa.
