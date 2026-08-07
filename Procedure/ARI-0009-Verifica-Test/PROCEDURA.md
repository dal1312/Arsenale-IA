# ARI-0009 — Verifica dei test

- **Categoria:** Nucleo
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.2.0
- **Utilizzo offline:** Sì

## Scopo

Valutare se i test dimostrano realmente il comportamento del software e se sono affidabili, leggibili e utili contro le regressioni.

## Campo di applicazione

Suite unitarie, integrazione, end-to-end, test di contratto, test di regressione e pipeline CI associate a un progetto.

## Quando usarla

- si vuole valutare affidabilità della suite
- si sospettano test instabili, deboli o troppo accoppiati
- si prepara un rilascio o un refactoring importante

## Quando non usarla

- manca completamente una suite e serve progettarla da zero come attività separata
- il problema principale è un singolo errore non ancora diagnosticato
- si vuole usare la sola percentuale di coverage come verdetto

## Prerequisiti

- comandi di test identificati
- accesso al codice coperto
- ambiente sufficientemente pulito e riproducibile
- eventuali report di copertura o CI disponibili

## Materiale necessario

- suite di test
- codice coperto
- comandi di esecuzione
- rapporti di copertura quando esistono
- pipeline CI e log di esecuzioni precedenti

## Procedura operativa

1. Individuare tutti i livelli di test presenti.
2. Eseguire la suite in ambiente pulito.
3. Registrare passati, falliti, saltati, durata e avvisi.
4. Ripetere i test sospetti per individuare instabilità.
5. Collegare i test ai comportamenti e ai rischi reali.
6. Controllare qualità delle asserzioni e casi negativi.
7. Verificare dipendenze da rete, tempo, ordine, file e stato globale.
8. Analizzare mock e sostituzioni.
9. Controllare casi limite, errori, concorrenza e regressioni note.
10. Proporre nuovi test indicando input, risultato atteso e motivo.

## Controlli

- conteggi reali della suite registrati
- test saltati o disabilitati esplicitati
- aree critiche collegate a test reali
- instabilità ripetuta e misurata
- coverage usata solo come indicatore complementare

### Categorie di valutazione

- test valido
- test debole
- test duplicato
- test instabile
- test troppo accoppiato all'implementazione
- comportamento critico non coperto

## Errori frequenti

- usare la percentuale di copertura come unica misura
- aggiungere test che ripetono l'implementazione
- ignorare test saltati
- correggere un test fallito senza capire il requisito
- considerare affidabile una suite dipendente dall'ordine

## Rapporto finale

Riportare comandi, ambiente, risultati, durata, test problematici, lacune, aree critiche scoperte, priorità e criteri di accettazione dei nuovi test.

## Condizioni di uscita

- suite eseguita e conteggi registrati
- aree critiche mappate
- instabilità analizzate
- test mancanti descritti concretamente
- piano di miglioramento prodotto

## Cronologia delle versioni

- **0.2.0** — Struttura uniformata a `STANDARD.md` preservando le categorie di valutazione dei test.
- **0.1.0** — Prima versione operativa.
