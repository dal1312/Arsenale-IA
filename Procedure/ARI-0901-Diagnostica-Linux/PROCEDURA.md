# ARI-0901 — Diagnostica Linux

- **Categoria:** Sistemi e sviluppo
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.2.0
- **Utilizzo offline:** Sì

## Scopo

Analizzare problemi di servizi, prestazioni, dipendenze e configurazione su Linux con un metodo documentato, minimo e reversibile.

## Campo di applicazione

Distribuzioni Linux, servizi systemd o equivalenti, applicazioni, processi, filesystem, rete, permessi, pacchetti e configurazioni.

## Quando usarla

- un servizio o processo fallisce
- esistono problemi di risorse, rete, permessi o dipendenze
- serve isolare una regressione di configurazione o pacchetto

## Quando non usarla

- non esiste un sintomo osservabile
- si vuole applicare hardening o tuning generico senza obiettivo
- il problema è chiaramente indipendente dal sistema operativo

## Prerequisiti

- distribuzione e kernel identificabili
- sintomo e comportamento atteso definiti
- accesso ai log pertinenti
- autorizzazione prima di modifiche privilegiate

## Materiale necessario

- journal/log di sistema e applicazione
- stato servizi e processi
- informazioni pacchetti e dipendenze
- configurazioni interessate
- metriche CPU, memoria, disco e rete

## Procedura operativa

1. Identificare distribuzione, kernel, ambiente e sintomo.
2. Riprodurre il problema e registrare il contesto.
3. Esaminare log di sistema e applicazione pertinenti.
4. Verificare CPU, memoria, spazio, rete e permessi.
5. Controllare pacchetti, dipendenze e configurazioni recenti.
6. Ridurre il problema al componente minimo.
7. Valutare un'ipotesi alla volta con verifiche non distruttive.
8. Applicare la correzione minima e documentare il ripristino.

## Controlli

- modifiche privilegiate motivate
- permessi non ampliati per aggirare il problema
- protezioni non disattivate senza causa
- configurazioni precedenti salvate quando necessario
- evidenze utili conservate

## Errori frequenti

- usare sudo come soluzione universale
- disattivare SELinux/AppArmor o firewall per aggirare il problema
- cambiare più configurazioni insieme
- ignorare log temporali
- dichiarare risolto senza verifica finale

## Rapporto finale

Riportare distribuzione/kernel, sintomo, riproduzione, log essenziali, ipotesi, causa confermata o probabile, correzione, ripristino e verifica finale.

## Condizioni di uscita

- sintomo riprodotto o impedimento spiegato
- causa confermata o probabilità motivata
- correzione minima verificata quando applicata
- ripristino documentato
- evidenze conservate

## Cronologia delle versioni

- **0.2.0** — Struttura uniformata a `STANDARD.md`; requisiti, controlli, rapporto e condizioni di uscita resi espliciti.
- **0.1.0** — Prima versione operativa.
