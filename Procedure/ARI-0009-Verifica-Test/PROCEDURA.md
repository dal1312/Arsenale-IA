# ARI-0009 — Verifica dei test

## Scopo
Valutare se i test dimostrano davvero il comportamento del software e se sono affidabili, leggibili e utili contro le regressioni.

## Input
- suite di test;
- codice coperto;
- comandi di esecuzione;
- eventuali rapporti di copertura;
- pipeline di integrazione continua.

## Output
- esito reale della suite;
- mappa delle aree critiche coperte e scoperte;
- elenco di test deboli, instabili o mancanti;
- piano di miglioramento.

## Procedura
1. Individuare tutti i livelli di test presenti.
2. Eseguire la suite in ambiente pulito.
3. Registrare test superati, falliti, saltati, durata e avvisi.
4. Ripetere i test sospetti per individuare instabilità.
5. Collegare i test ai comportamenti e ai rischi reali.
6. Controllare qualità delle asserzioni e gestione dei casi negativi.
7. Verificare dipendenze da rete, tempo, ordine, file e stato globale.
8. Analizzare uso di mock e sostituzioni.
9. Controllare casi limite, errori, concorrenza e regressioni note.
10. Proporre nuovi test specificando input, risultato atteso e motivo.

## Categorie
- test valido;
- test debole;
- test duplicato;
- test instabile;
- test troppo accoppiato all'implementazione;
- comportamento critico non coperto.

## Errori frequenti
- usare la percentuale di copertura come unica misura;
- aggiungere test che ripetono l'implementazione;
- ignorare test saltati o disabilitati;
- correggere un test fallito senza capire se il difetto è nel codice;
- considerare affidabile una suite che dipende dall'ordine.

## Condizioni di uscita
- [ ] suite eseguita e conteggi registrati;
- [ ] aree critiche collegate ai test;
- [ ] instabilità analizzate;
- [ ] test mancanti descritti concretamente;
- [ ] piano di miglioramento prodotto.

## Rapporto finale
Riportare comandi, ambiente, risultati, durata, test problematici, lacune, priorità e criteri di accettazione dei nuovi test.
