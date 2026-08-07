# ARI-0301 — Revisione C++

- **Categoria:** Sistemi e sviluppo
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.2.0
- **Utilizzo offline:** Sì

## Scopo

Analizzare un progetto C++ per individuare problemi di correttezza, memoria, portabilità, concorrenza, prestazioni e qualità della build.

## Campo di applicazione

Applicazioni native, librerie, CLI, componenti ad alte prestazioni e progetti multipiattaforma in C++.

## Quando usarla

- prima di release o cambiamenti strutturali
- durante upgrade di compilatore o standard C++
- quando esistono rischi di memoria, concorrenza o portabilità

## Quando non usarla

- serve diagnosticare un crash specifico non ancora isolato
- l'ambito è una patch limitata e basta una code review
- si vuole ottimizzare senza misure

## Prerequisiti

- toolchain e sistema di build identificabili
- piattaforme supportate note
- accesso ai test
- possibilità di compilare almeno una configurazione quando disponibile

## Materiale necessario

- CMakeLists.txt o sistema di build equivalente
- configurazioni compiler
- suite di test
- analizzatori statici e sanitizzatori disponibili
- documentazione delle piattaforme supportate

## Procedura operativa

1. Individuare standard C++, compilatori, build system e piattaforme.
2. Eseguire configurazione, compilazione, test e analisi statica quando disponibili.
3. Controllare ownership, durata oggetti e RAII.
4. Verificare puntatori, riferimenti, iteratori, conversioni e limiti.
5. Analizzare eccezioni, error codes, concorrenza e sincronizzazione.
6. Controllare separazione interfacce/implementazione, dipendenze e tempi di compilazione.
7. Misurare prima di proporre ottimizzazioni.

## Controlli

- assenza di use-after-free o doppi rilasci evidenti
- ownership comprensibile
- warning elevati abilitati quando possibile
- sanitizzatori usati dove compatibili
- sincronizzazione dello stato condiviso verificata
- portabilità dichiarata verificabile

## Errori frequenti

- ottimizzare senza profiling
- sostituire automaticamente ogni puntatore grezzo
- ignorare comportamento indefinito
- mescolare API pubblica e dettagli interni
- usare macro senza necessità
- introdurre concorrenza senza modello di sincronizzazione

## Rapporto finale

Riportare toolchain, standard, build system, esito build/test, rischi di memoria, concorrenza, portabilità, prestazioni e piano di intervento.

## Condizioni di uscita

- build riprodotta o impedimento documentato
- aree critiche analizzate
- rischi memoria/concorrenza classificati
- misure disponibili registrate
- piano verificabile prodotto

## Cronologia delle versioni

- **0.2.0** — Struttura uniformata a `STANDARD.md`; requisiti, controlli, rapporto e condizioni di uscita resi espliciti.
- **0.1.0** — Prima versione operativa.
