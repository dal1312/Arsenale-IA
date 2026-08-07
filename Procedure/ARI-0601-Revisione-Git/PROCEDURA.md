# ARI-0601 — Revisione Git

- **Categoria:** Sistemi e sviluppo
- **Livello:** L3 Avanzato
- **Stato:** Bozza verificabile
- **Versione:** 0.2.0
- **Utilizzo offline:** Sì

## Scopo

Valutare lo stato del repository Git, la chiarezza della cronologia, la strategia dei rami e i rischi operativi.

## Campo di applicazione

Repository Git locali e remoti, cronologia, branch, tag, file ignorati, artefatti e pratiche di integrazione.

## Quando usarla

- la cronologia è difficile da comprendere
- si prepara una strategia di branch o release
- si sospettano file generati, binari o segreti tracciati
- serve valutare disciplina operativa del repository

## Quando non usarla

- l'obiettivo è una revisione completa del software oltre Git
- si deve riscrivere la cronologia senza piano e autorizzazione
- il problema principale è una singola patch

## Prerequisiti

- accesso al repository Git
- ramo predefinito identificabile
- cronologia disponibile
- permesso prima di operazioni distruttive o riscritture

## Materiale necessario

- working tree e configurazione Git
- cronologia commit
- branch e tag
- file .gitignore/.gitattributes
- regole remote o protezioni ramo quando disponibili

## Procedura operativa

1. Verificare ramo predefinito, working tree e file ignorati.
2. Analizzare cronologia, messaggi e dimensione delle modifiche.
3. Controllare binari pesanti, segreti, artefatti e file generati.
4. Valutare strategia branch, tag, release e pull request.
5. Verificare conflitti ricorrenti, merge e commit correttivi ripetitivi.
6. Controllare protezioni del ramo principale e verifiche obbligatorie.
7. Produrre un piano ordinato per rischio senza riscrivere la cronologia automaticamente.

## Controlli

- repository pulito o anomalie documentate
- .gitignore coerente
- nessun segreto esposto nella cronologia analizzata
- commit leggibili e verificabili
- tag/versioni coerenti
- strategia rami documentata
- azioni distruttive non eseguite senza autorizzazione

## Errori frequenti

- riscrivere la cronologia come prima soluzione
- confondere molti commit con cattiva qualità
- rimuovere file tracciati senza valutarne l'uso
- ignorare tag e release
- considerare .gitignore sufficiente a rimuovere segreti storici

## Rapporto finale

Riportare stato working tree, struttura branch/tag, anomalie cronologia, file problematici, protezioni e piano di intervento con rischi e priorità.

## Condizioni di uscita

- stato repository compreso
- rischi cronologia e file classificati
- strategia branch/tag valutata
- nessuna modifica distruttiva non autorizzata
- piano operativo prodotto

## Cronologia delle versioni

- **0.2.0** — Struttura uniformata a `STANDARD.md`; requisiti, controlli, rapporto e condizioni di uscita resi espliciti.
- **0.1.0** — Prima versione operativa.
