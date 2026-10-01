# Revisione Python CLI

Target: esporta_pianificate.py, singolo script esistente; revisione senza modifica del codice.

- P2: Versione minima Python e istruzioni di distribuzione della CLI non dichiarate in un documento dedicato. Documentare interprete supportato e comando di uso, senza aggiornare dipendenze.
- P3: Copertura precedente limitata al percorso positivo; questa revisione copre soltanto il ramo errore UTF-8. Nessuna correzione del codice: il ramo esercitato gestisce l’errore esplicitamente.

Lint/type check/build di pacchetto non configurati; niente installazioni. Compilazione AST/bytecode in memoria riuscita. Portabilità Linux non eseguita; packaging minimale analizzato, non inventato. Versione Python esatta e hash in revisione.json.
