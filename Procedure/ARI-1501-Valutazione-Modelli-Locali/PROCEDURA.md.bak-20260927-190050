# ARI-1501 — Valutazione modelli locali

- **Categoria:** Intelligenza artificiale
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.1.0
- **Utilizzo offline:** Sì

## Scopo

Confrontare modelli di intelligenza artificiale eseguiti localmente con misure ripetibili di qualità, prestazioni, consumo di risorse e compatibilità, producendo una scelta motivata per uno specifico caso d'uso.

## Campo di applicazione

Modelli linguistici, multimodali e di embedding eseguiti su workstation, server o dispositivi locali tramite runtime come llama.cpp, Ollama, LM Studio, vLLM o motori equivalenti. La procedura copre confronti tra modelli, quantizzazioni, runtime e configurazioni hardware.

## Quando usarla

- prima di scegliere un modello locale per un'applicazione o un agente
- quando si confrontano quantizzazioni, runtime o acceleratori differenti
- dopo aggiornamenti di modello, driver o motore di inferenza
- quando servono dati verificabili su qualità, latenza, memoria e stabilità

## Quando non usarla

- il modello deve essere addestrato o sottoposto a fine-tuning
- serve ottimizzare una configurazione già scelta senza confrontare alternative
- l'ambiente non permette di fissare e registrare versioni, parametri e carico
- si vuole dedurre la qualità da impressioni o da una singola conversazione

## Prerequisiti

- caso d'uso, lingua, requisiti e vincoli hardware definiti
- almeno un modello e un runtime installabili o già disponibili localmente
- dataset di prova rappresentativo e privo di dati non autorizzati
- strumenti per misurare tempo, memoria e utilizzo dell'acceleratore
- condizioni di esecuzione sufficientemente stabili e ripetibili

## Materiale necessario

- identificativo esatto, versione, licenza e provenienza di ogni modello
- formato e quantizzazione dei pesi
- versione di runtime, driver e librerie di accelerazione
- scheda hardware con CPU, RAM, GPU o NPU e memoria disponibile
- prompt o dataset di valutazione versionato
- criteri di scoring e soglie di accettazione
- log grezzi delle esecuzioni e configurazioni utilizzate

## Procedura operativa

1. Definire il caso d'uso, gli errori inaccettabili e le soglie minime di qualità, latenza, memoria e stabilità.
2. Registrare hardware, sistema operativo, driver, runtime, modello, quantizzazione, contesto massimo e parametri di generazione.
3. Preparare un insieme di prove rappresentativo, separando controlli deterministici, valutazioni automatiche e giudizi umani.
4. Eseguire un riscaldamento iniziale non conteggiato e verificare che nessun altro carico alteri significativamente le misure.
5. Eseguire almeno tre ripetizioni per configurazione con stessi input, seed quando supportato e parametri invariati.
6. Misurare tempo di caricamento, latenza al primo token, token al secondo, durata totale, memoria di picco, errori e arresti.
7. Valutare la qualità con criteri espliciti: correttezza, aderenza alle istruzioni, lingua italiana, robustezza, formato e allucinazioni rilevabili.
8. Eseguire prove negative e limite su input lunghi, richieste ambigue, output strutturati e saturazione della memoria.
9. Confrontare le configurazioni a parità di condizioni; separare sempre l'effetto del modello da quello di runtime e quantizzazione.
10. Conservare configurazioni, risultati grezzi, aggregazioni e anomalie sufficienti a ripetere il confronto.
11. Formulare una raccomandazione per il caso d'uso dichiarato, indicando compromessi, limiti e condizioni che richiedono una nuova valutazione.

## Controlli

- modelli e runtime identificati con versione o hash verificabile
- stesso dataset e stessi parametri nelle prove comparabili
- almeno tre ripetizioni valide per ogni configurazione
- riscaldamento escluso dalle misure finali
- mediana e variabilità riportate, non solo il risultato migliore
- qualità e prestazioni valutate separatamente
- fallimenti, timeout e risultati anomali conservati
- licenza e requisiti hardware compatibili con l'uso previsto
- nessun dato riservato inviato a servizi esterni durante una prova dichiarata locale

## Errori frequenti

- confrontare modelli con prompt, contesto o parametri differenti
- usare nomi commerciali senza registrare file, versione e quantizzazione
- misurare una sola esecuzione o includere il caricamento in modo incoerente
- scegliere il modello solo per token al secondo ignorando qualità e memoria
- usare benchmark generici non rappresentativi del caso d'uso reale
- confondere limiti del runtime con limiti del modello
- scartare silenziosamente errori, risposte vuote o arresti per memoria
- dichiarare vincitore un modello senza soglie definite prima delle prove

## Rapporto finale

Riportare obiettivo, ambiente hardware e software, configurazioni confrontate, dataset e criteri, numero di ripetizioni, risultati grezzi e aggregati, qualità per categoria, latenza al primo token, token al secondo, memoria di picco, errori, limiti della prova e raccomandazione finale. Usare uno dei verdetti: **Idoneo**, **Idoneo con vincoli**, **Non idoneo** o **Inconcludente**.

## Condizioni di uscita

- ambiente e configurazioni registrati in modo riproducibile
- prove comparabili completate o impedimenti documentati
- soglie applicate senza modificarle dopo aver visto i risultati
- risultati anomali e limiti esplicitati
- raccomandazione collegata al caso d'uso e supportata da evidenze

## Cronologia delle versioni

- **0.1.0** — Prima versione operativa per confronto ripetibile di modelli, quantizzazioni e runtime locali.
