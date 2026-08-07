# ARI-0005 — Implementazione controllata

- **Categoria:** Nucleo
- **Livello:** L4 Professionale
- **Stato:** Verificata
- **Versione:** 0.2.1
- **Utilizzo offline:** Sì

## Scopo

Realizzare una modifica tecnica in modo incrementale, verificabile e coerente con una specifica o un piano approvato.

## Campo di applicazione

Implementazioni di funzionalità, correzioni, migrazioni e modifiche tecniche per le quali esistono criteri di accettazione verificabili.

## Quando usarla

- esiste un requisito o piano approvato
- i criteri di accettazione sono sufficientemente chiari
- l'ambiente permette di verificare gli incrementi

## Quando non usarla

- manca ancora la diagnosi del problema
- il repository non è stato compreso abbastanza per stimare l'impatto
- l'obiettivo reale è un refactoring senza variazione funzionale: usare ARI-0006

## Prerequisiti

- requisito o piano approvato
- criteri di accettazione
- ambiente funzionante
- baseline dei test pertinenti nota

## Materiale necessario

- piano o specifica
- codice sorgente
- suite di test
- comandi di lint, type check, build e avvio pertinenti
- documentazione da aggiornare

## Procedura operativa

1. Confermare ambito e punto di partenza.
2. Eseguire i test pertinenti prima delle modifiche.
3. Scegliere il più piccolo incremento funzionante.
4. Aggiungere o aggiornare il test che descrive il comportamento.
5. Applicare la modifica minima necessaria.
6. Eseguire il test specifico.
7. Rifattorizzare solo mantenendo i test verdi.
8. Ripetere per l'incremento successivo.
9. Eseguire controlli statici, suite completa e build.
10. Verificare manualmente il flusso principale quando necessario.
11. Aggiornare documentazione e registro delle modifiche.

## Controlli

- nessun ampliamento di ambito non motivato
- i test iniziali e finali sono registrati
- test falliti non vengono nascosti o rimossi per ottenere esito positivo
- ogni incremento soddisfa un criterio di accettazione
- documentazione e configurazione restano coerenti

## Errori frequenti

- implementare più requisiti insieme senza separazione
- aggiungere astrazioni premature
- rimuovere controlli per far passare i test
- saltare la baseline iniziale
- dichiarare completato senza build o verifica equivalente

## Rapporto finale

Riepilogare requisito, incrementi eseguiti, file modificati, test aggiunti o aggiornati, comandi di verifica, esito build, criteri di accettazione soddisfatti, rischi residui e limiti.

## Condizioni di uscita

- criteri di accettazione soddisfatti
- test pertinenti superati
- build verificata quando prevista
- documentazione aggiornata
- rischi residui dichiarati

## Cronologia delle versioni

- **0.2.1** — Procedura promossa a **Verificata** dopo due implementazioni operative documentate, inclusa una prova indipendente su Omega FL e una prova interna RED→GREEN. Nessuna modifica al metodo operativo.
- **0.2.0** — Struttura uniformata a `STANDARD.md`; requisiti, controlli, rapporto e condizioni di uscita resi espliciti.
- **0.1.0** — Prima versione operativa.
