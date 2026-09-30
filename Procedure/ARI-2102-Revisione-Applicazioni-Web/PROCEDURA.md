# ARI-2102 — Revisione applicazioni web (complete e a pagina singola)

- **Categoria:** Web, Applicazioni, Interfacce e Risorse
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.1.0
- **Utilizzo offline:** Sì

## Scopo

Revisionare applicazioni web interattive valutando architettura dell'interfaccia client, flussi utente, gestione dello stato, chiamate API, gestione errori, sicurezza di base, prestazioni e qualità dell'esperienza.

## Campo di applicazione

Applicazioni a pagina singola, applicazioni web installabili, pannelli di controllo, pannelli gestionali, app React, Vue, Svelte, Next, Vite o equivalenti, con o senza servizio applicativo locale. La procedura copre codice, costruzione, instradamento, componenti, moduli, API client e stati dell'interfaccia.

## Quando usarla

- prima di integrare una funzionalita web interattiva
- quando una applicazione web presenta bug di flusso o stato
- prima di rilascio o demo con utenti reali
- durante revisione tecnica di interfaccia client e integrazione API

## Quando non usarla

- serve solo una revisione visuale di una pagina statica
- il focus esclusivo è infrastruttura cloud o database
- mancano sorgente, costruzione o istruzioni minime di esecuzione
- l'app è nativa scrivania o mobile senza componente web

## Prerequisiti

- codice sorgente disponibile
- flussi principali e ruoli utente noti
- comandi di installazione, costruzione o avvio disponibili quando necessari
- endpoint o mock API identificati
- vincoli di autenticazione e dati sensibili chiariti

## Materiale necessario

- sorgente interfaccia client e configurazioni
- componenti condivisi e sistema di progettazione se presenti
- schema API o esempi payload
- elenco dei flussi critici
- log, schermate o rapporto errore se la revisione parte da un problema
- criteri di accettazione o definizione di pronto

## Procedura operativa

1. Identificare stack, entrypoint, routing, layout principali e flussi utente critici.
2. Valutare separazione tra presentazione, stato, validazione, chiamate API e gestione errori.
3. Controllare moduli, caricamenti, stati vuoti, stati di errore, permessi e feedback utente.
4. Revisionare accessibilità dei controlli, navigazione tastiera, focus e semantica.
5. Valutare sicurezza interfaccia client di base: esposizione segreti, fiducia nei dati client, sanitizzazione e gestione token.
6. Controllare prestazioni: bundle, rendering inutile, immagini, lazy loading e richieste ridondanti.
7. Verificare coerenza visuale e usabilità ripetuta dei flussi principali.
8. Collegare ogni rilievo a impatto utente o rischio tecnico.
9. Proporre correzioni ordinate per priorità e costo stimato.

## Controlli

- flussi principali identificati e coperti dalla revisione
- stati di caricamento, vuoto, errore e successo presenti o esplicitamente valutati
- nessun segreto client evidente
- input validati lato interfaccia senza sostituire validazione lato server
- gestione errori leggibile e non muta
- componenti riusabili coerenti con il sistema di progettazione
- navigazione adattivo e accessibile
- dipendenze e script coerenti con lo stack tecnico

## Errori frequenti

- controllare solo il percorso felice
- lasciare errori API senza feedback utente
- duplicare logica di stato in componenti non coordinati
- salvare token o segreti in modo improprio
- introdurre librerie pesanti per problemi piccoli
- ignorare ruoli, permessi e casi vuoti

## Rapporto finale

Riportare stack, flussi revisionati, componenti o moduli analizzati, rilievi con priorità, rischi residui, test o verifiche consigliate e verdetto. Usare uno dei verdetti: **Pronta**, **Pronta con correzioni**, **Non pronta** o **Inconcludente**.

## Condizioni di uscita

- flussi critici analizzati
- rischi funzionali, esperienza utente e tecnici separati
- rilievi riproducibili e prioritizzati
- correzioni proposte senza cambiare ambito prodotto
- limiti della revisione dichiarati

## Cronologia delle versioni

- **0.1.0** — Prima versione per revisione di applicazioni web interattive.

