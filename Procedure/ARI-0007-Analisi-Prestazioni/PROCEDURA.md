# ARI-0007 — Analisi delle prestazioni

- **Categoria:** Nucleo
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.2.0
- **Utilizzo offline:** Sì

## Scopo

Individuare colli di bottiglia reali e proporre o verificare interventi basati su misurazioni ripetibili.

## Campo di applicazione

Latenza, throughput, uso CPU, memoria, I/O, rete, query, tempi di build o elaborazioni lente con uno scenario misurabile.

## Quando usarla

- esiste uno scenario lento o costoso riproducibile
- è disponibile o definibile una soglia prestazionale
- si può misurare prima e dopo con condizioni comparabili

## Quando non usarla

- manca uno scenario concreto
- si vuole ottimizzare solo per intuizione
- il problema principale è correttezza funzionale o sicurezza

## Prerequisiti

- scenario e obiettivo prestazionale definiti
- ambiente di prova controllabile
- dati o carico rappresentativi
- strumenti di misurazione o profiling disponibili

## Materiale necessario

- comandi o workload di benchmark
- dataset o input rappresentativi
- profiler e metriche pertinenti
- versione o commit di baseline
- risultati delle prove

## Procedura operativa

1. Definire scenario e soglia attesa.
2. Stabilire dati, carico e ambiente di prova.
3. Misurare tempo, CPU, memoria, I/O e rete quando pertinenti.
4. Ripetere le prove per ridurre il rumore.
5. Profilare il percorso critico.
6. Separare sintomi, cause e ipotesi.
7. Stimare impatto e costo degli interventi.
8. Applicare una modifica per volta quando autorizzato.
9. Ripetere esattamente la stessa prova.
10. Documentare miglioramenti e regressioni.

## Controlli

- baseline registrata
- prove prima/dopo equivalenti
- numero di ripetizioni sufficiente a escludere risultati casuali
- collo di bottiglia supportato da metriche
- correttezza funzionale preservata
- cache e concorrenza valutate insieme ai relativi costi

## Errori frequenti

- usare impressioni al posto delle metriche
- confrontare ambienti diversi
- ottimizzare un percorso non critico
- introdurre cache senza invalidazione
- sacrificare correttezza per guadagni irrilevanti

## Rapporto finale

Riportare scenario, ambiente, strumenti, dati di prova, metriche iniziali, collo di bottiglia, ipotesi, interventi, risultati finali, variazione percentuale quando utile e rischi residui.

## Condizioni di uscita

- baseline registrata
- collo di bottiglia dimostrato
- intervento misurato con prova equivalente quando applicato
- correttezza verificata
- limiti documentati

## Cronologia delle versioni

- **0.2.0** — Struttura uniformata a `STANDARD.md`; requisiti, controlli, rapporto e condizioni di uscita resi espliciti.
- **0.1.0** — Prima versione operativa.
