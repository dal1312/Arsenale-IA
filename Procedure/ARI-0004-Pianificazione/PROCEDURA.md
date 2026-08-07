# ARI-0004 — Pianificazione tecnica

- **Categoria:** Nucleo
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.2.0
- **Utilizzo offline:** Sì

## Scopo

Trasformare un obiettivo in un piano tecnico verificabile, ordinato e suddiviso in attività eseguibili.

## Campo di applicazione

Nuove funzionalità, migrazioni, correzioni complesse, hardening, refactoring approvati e lavori che richiedono più passaggi coordinati.

## Quando usarla

- l'obiettivo è noto ma manca un piano eseguibile
- più componenti o dipendenze devono essere coordinati
- servono criteri di accettazione e ordine di lavoro prima dell'implementazione

## Quando non usarla

- manca ancora comprensione del repository o del problema
- la causa di un bug non è stata individuata
- il cambiamento è banale e ha già un criterio di accettazione completo e univoco

## Prerequisiti

- obiettivo e risultato atteso descritti
- vincoli principali disponibili
- accesso alla base di codice o alla documentazione necessaria
- decisioni già approvate chiaramente distinte dalle ipotesi

## Materiale necessario

- requisiti, ticket o specifica
- mappa dei componenti interessati
- vincoli tecnici, operativi e temporali
- test esistenti e criteri di accettazione disponibili

## Procedura operativa

1. Definire obiettivo, utenti e risultato atteso.
2. Raccogliere vincoli tecnici, operativi e temporali.
3. Individuare componenti e file probabilmente interessati.
4. Esplicitare ipotesi, dipendenze e punti incerti.
5. Definire criteri di accettazione misurabili.
6. Scomporre il lavoro in attività piccole e verificabili.
7. Ordinare dipendenze e blocchi.
8. Associare a ogni attività test e prova di completamento.
9. Identificare rischi e strategie di riduzione.
10. Stabilire esplicitamente cosa è fuori ambito.

## Controlli

- ogni requisito è collegato ad almeno un'attività
- ogni attività ha test o criterio di verifica
- le dipendenze sono ordinate
- analisi e implementazione non sono confuse nello stesso ticket
- le ipotesi non sono presentate come decisioni definitive

## Errori frequenti

- creare attività generiche come 'sistemare il backend'
- fissare dettagli architetturali senza evidenza
- omettere rollback o migrazioni quando necessarie
- stimare senza esplicitare dipendenze
- ampliare l'ambito durante la pianificazione

## Rapporto finale

Produrre un piano con sintesi, ambito, fuori ambito, ipotesi, rischi, dipendenze e schede attività. Ogni scheda deve contenere titolo, obiettivo, dipendenze, file o moduli, passi operativi, test, criterio di accettazione, rischio e stima relativa.

## Condizioni di uscita

- ogni requisito ha almeno un'attività
- ogni attività ha una verifica finale
- dipendenze e rischi sono espliciti
- fuori ambito definito
- piano pronto per ARI-0005

## Cronologia delle versioni

- **0.2.0** — Struttura uniformata a `STANDARD.md`; requisiti, controlli, rapporto e condizioni di uscita resi espliciti.
- **0.1.0** — Prima versione operativa.
