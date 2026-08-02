# ARI-0201 — Revisione C#

## Scopo
Valutare un progetto C# esistente sotto il profilo di struttura, correttezza, testabilità, prestazioni e manutenibilità.

## Campo di applicazione
Applicazioni console, desktop, servizi, librerie, API ASP.NET, progetti WPF e WinUI.

## Procedura
1. Individuare soluzione, progetti, target framework e dipendenze NuGet.
2. Verificare build, warning, analizzatori e test.
3. Controllare nullable reference types, gestione eccezioni e cancellazione asincrona.
4. Analizzare separazione delle responsabilità, dipendenze statiche e uso dell'iniezione delle dipendenze.
5. Verificare uso corretto di `async`/`await`, `IDisposable`, flussi e risorse native.
6. Controllare configurazione, logging, serializzazione e accesso dati.
7. Produrre problemi classificati per priorità e piano di miglioramento.

## Controlli specifici
- target framework supportato;
- warning trattati in modo coerente;
- assenza di blocchi sincroni su codice asincrono;
- cancellazione propagata dove necessaria;
- risorse rilasciate correttamente;
- test sulle aree critiche;
- pacchetti NuGet necessari e aggiornabili.

## Errori frequenti
- usare `.Result` o `.Wait()` senza necessità;
- catturare `Exception` senza azione utile;
- classi di servizio troppo grandi;
- stato globale mutabile;
- logica applicativa inserita nell'interfaccia grafica;
- configurazioni e segreti hardcoded.

## Rapporto finale
Indicare versione .NET, esito build e test, problemi con file e simboli, rischi, correzioni consigliate e ordine di intervento.

## Condizioni di uscita
- soluzione compresa;
- build verificata;
- test registrati;
- problemi prioritizzati;
- piano operativo prodotto.
