# ARI-0401 — Revisione JavaScript e TypeScript

- **Categoria:** Sistemi e sviluppo
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.2.0
- **Utilizzo offline:** Sì

## Scopo

Valutare un progetto JavaScript o TypeScript in termini di correttezza, struttura, dipendenze, sicurezza, test e qualità della distribuzione.

## Campo di applicazione

Applicazioni web, servizi Node.js, librerie, CLI e frontend React, Vue, Angular o framework equivalenti.

## Quando usarla

- prima di release o migrazioni
- quando dipendenze, build o tipi risultano fragili
- quando client e server possono avere rischi diversi da separare

## Quando non usarla

- serve diagnosticare un singolo errore non ancora compreso
- l'ambito è una sola patch già isolata
- si vuole aggiornare indiscriminatamente tutte le dipendenze

## Prerequisiti

- runtime e package manager identificabili
- file di lock disponibile o assenza motivabile
- comandi di lint/type check/test/build noti o deducibili
- ambienti target descritti

## Materiale necessario

- package.json e lockfile
- tsconfig e configurazioni build
- suite di test
- configurazioni runtime e variabili ambiente
- documentazione browser/server quando pertinente

## Procedura operativa

1. Individuare runtime, package manager, framework, build tool e ambienti.
2. Verificare installazione deterministica, lint, type check, test e build.
3. Analizzare TypeScript, alias, moduli ed ESM/CommonJS.
4. Controllare validazione input, errori, rete e variabili ambiente.
5. Individuare moduli troppo grandi, stato condiviso e dipendenze nascoste.
6. Verificare bundle, lazy loading e compatibilità browser quando pertinenti.
7. Produrre piano prioritizzato con test di regressione richiesti.

## Controlli

- lockfile coerente
- script progetto documentati
- uso di any motivato
- input esterni validati a runtime
- promesse senza errori silenziosi
- segreti assenti dal client
- dipendenze non necessarie identificate
- build riproducibile

## Errori frequenti

- confondere tipi TypeScript con validazione runtime
- aggiornare tutte le dipendenze insieme
- ignorare differenze dev/prod
- usare stato globale senza confini
- ottimizzare bundle senza misure
- fidarsi di test che non esercitano comportamento reale

## Rapporto finale

Indicare runtime, package manager, esito installazione, lint, tipi, test e build; elencare problemi, rischi client/server, dipendenze e piano di correzione.

## Condizioni di uscita

- ambiente compreso
- build e test verificati o impedimenti motivati
- rischi client/server distinti
- dipendenze valutate
- piano operativo prodotto

## Cronologia delle versioni

- **0.2.0** — Struttura uniformata a `STANDARD.md`; requisiti, controlli, rapporto e condizioni di uscita resi espliciti.
- **0.1.0** — Prima versione operativa.
