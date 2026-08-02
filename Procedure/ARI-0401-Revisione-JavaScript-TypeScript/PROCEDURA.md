# ARI-0401 — Revisione JavaScript e TypeScript

## Scopo
Valutare un progetto JavaScript o TypeScript esistente in termini di correttezza, struttura, dipendenze, sicurezza, test e qualità della distribuzione.

## Campo di applicazione
Applicazioni web, servizi Node.js, librerie, strumenti da riga di comando e interfacce basate su React, Vue, Angular o framework equivalenti.

## Procedura
1. Individuare runtime, gestore pacchetti, framework, strumenti di build e ambienti previsti.
2. Verificare installazione deterministica, lint, controllo dei tipi, test e build.
3. Analizzare configurazioni TypeScript, alias, moduli e compatibilità ESM/CommonJS.
4. Controllare validazione degli input, gestione degli errori, chiamate di rete e variabili d'ambiente.
5. Individuare componenti o moduli troppo grandi, stato condiviso e dipendenze nascoste.
6. Verificare bundle, caricamento differito, dipendenze client e compatibilità browser quando pertinenti.
7. Produrre un piano prioritizzato con test di regressione richiesti.

## Controlli specifici
- file di blocco presente e coerente;
- script di progetto documentati;
- tipi non aggirati inutilmente con `any`;
- input esterni validati a runtime;
- promesse gestite senza errori silenziosi;
- segreti assenti dal codice client;
- dipendenze non necessarie identificate;
- build riproducibile.

## Errori frequenti
- confondere i tipi TypeScript con validazione a runtime;
- aggiornare tutte le dipendenze insieme;
- ignorare differenze tra sviluppo e produzione;
- usare stato globale senza confini;
- ottimizzare il bundle senza misurazioni;
- considerare superati test che non esercitano il comportamento reale.

## Rapporto finale
Indicare runtime, gestore pacchetti, esito installazione, lint, tipi, test e build; elencare problemi, rischi, dipendenze e piano di correzione.

## Condizioni di uscita
- ambiente compreso;
- build e test verificati;
- rischi client/server distinti;
- dipendenze valutate;
- piano operativo prodotto.
