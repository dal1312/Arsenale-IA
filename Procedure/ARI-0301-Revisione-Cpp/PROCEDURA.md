# ARI-0301 — Revisione C++

## Scopo
Analizzare un progetto C++ esistente per individuare problemi di correttezza, gestione della memoria, portabilità, prestazioni e qualità della build.

## Campo di applicazione
Applicazioni native, librerie, strumenti da riga di comando, moduli ad alte prestazioni e componenti multipiattaforma.

## Procedura
1. Individuare standard C++, compilatori, sistema di build e piattaforme supportate.
2. Eseguire configurazione, compilazione, test e analisi statica quando disponibili.
3. Controllare proprietà delle risorse, durata degli oggetti e uso di RAII.
4. Verificare puntatori, riferimenti, iteratori, conversioni e accessi ai limiti.
5. Analizzare eccezioni, codici di errore, concorrenza e sincronizzazione.
6. Controllare separazione tra interfacce e implementazione, dipendenze e tempi di compilazione.
7. Misurare prima di proporre ottimizzazioni.

## Controlli specifici
- assenza di possibili use-after-free e doppi rilasci;
- uso motivato dei puntatori grezzi;
- ownership comprensibile;
- compilazione con warning elevati;
- test con sanitizzatori quando compatibili;
- sincronizzazione corretta dello stato condiviso;
- portabilità dichiarata e verificabile.

## Errori frequenti
- ottimizzare senza profiling;
- sostituire automaticamente ogni puntatore grezzo;
- ignorare comportamento indefinito;
- mescolare interfacce pubbliche e dettagli interni;
- usare macro dove bastano costrutti del linguaggio;
- introdurre concorrenza senza modello di sincronizzazione.

## Rapporto finale
Riportare toolchain, standard, esito build e test, rischi di memoria, problemi di concorrenza, portabilità, prestazioni e piano di intervento.

## Condizioni di uscita
- build riprodotta;
- aree critiche analizzate;
- rischi di memoria classificati;
- misure disponibili registrate;
- piano verificabile prodotto.
