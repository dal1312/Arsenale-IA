# ARI-0008 — Analisi della sicurezza

- **Categoria:** Nucleo
- **Livello:** L5 Audit
- **Stato:** Bozza verificabile
- **Versione:** 0.2.0
- **Utilizzo offline:** Sì

## Scopo

Valutare i rischi di sicurezza di un progetto e produrre interventi prioritizzati distinguendo vulnerabilità confermate, ipotesi e miglioramenti difensivi.

## Campo di applicazione

Codice, configurazioni, dipendenze, autenticazione, autorizzazione, dati sensibili, file, rete, distribuzione e superfici esposte di applicazioni e servizi.

## Quando usarla

- si prepara un hardening o rilascio
- cambiano superfici esposte, autenticazione o trattamento dati
- serve una revisione mirata dei controlli di sicurezza

## Quando non usarla

- si vuole eseguire una prova offensiva non autorizzata
- mancano accesso e contesto sufficienti per distinguere configurazione reale e ipotesi
- il problema è un singolo bug funzionale senza implicazioni di sicurezza

## Prerequisiti

- ambito e autorizzazioni definiti
- codice e configurazioni accessibili
- modello di utilizzo e dati trattati descritti
- ambienti e dipendenze principali identificati

## Materiale necessario

- codice e configurazioni
- diagrammi o descrizione dei flussi
- inventario dipendenze e immagini
- configurazioni di autenticazione e autorizzazione
- log e risultati di scanner solo come evidenze complementari

## Procedura operativa

1. Identificare beni, utenti, confini di fiducia e dati sensibili.
2. Elencare punti di ingresso, servizi, file, rete e dipendenze.
3. Verificare autenticazione, autorizzazione e separazione dei ruoli.
4. Controllare validazione input e codifica output.
5. Cercare segreti, credenziali, token e dati sensibili esposti.
6. Analizzare sessioni, errori, log e configurazioni predefinite.
7. Valutare injection, traversal, esecuzione comandi, upload e deserializzazione quando pertinenti.
8. Controllare crittografia, firme, nonce, timestamp e replay quando pertinenti.
9. Valutare dipendenze e immagini di distribuzione.
10. Classificare evidenze, impatto, probabilità e mitigazioni.

## Controlli

- superfici d'attacco identificate
- evidenze raccolte senza riportare segreti in chiaro
- mitigazioni collegate a test di verifica
- rischi residui documentati

### Classificazione delle evidenze

- **confermata**
- **altamente probabile**
- **da verificare**
- **miglioramento difensivo**

## Errori frequenti

- dichiarare vulnerabilità senza prova
- affidarsi solo a scanner automatici
- ignorare configurazione e distribuzione
- correggere il sintomo senza eliminare la causa
- pubblicare dettagli sensibili nel rapporto

## Rapporto finale

Per ogni elemento indicare identificativo, categoria, stato dell'evidenza, scenario di rischio, impatto, probabilità, priorità, mitigazione, verifica e rischio residuo. Separare chiaramente informazioni sensibili da quelle pubblicabili.

## Condizioni di uscita

- superfici identificate
- evidenze classificate
- priorità assegnate
- mitigazioni e test definiti
- nessun segreto esposto nel rapporto
- rischi residui documentati

## Cronologia delle versioni

- **0.2.0** — Struttura uniformata a `STANDARD.md` preservando la classificazione delle evidenze.
- **0.1.0** — Prima versione operativa.
