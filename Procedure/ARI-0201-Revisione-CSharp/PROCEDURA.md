# ARI-0201 — Revisione C#

- **Categoria:** Sistemi e sviluppo
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.2.0
- **Utilizzo offline:** Sì

## Scopo

Valutare un progetto C# sotto il profilo di struttura, correttezza, testabilità, prestazioni e manutenibilità.

## Campo di applicazione

Applicazioni console, servizi, librerie, API ASP.NET, WPF, WinUI e altre soluzioni .NET in C#.

## Quando usarla

- prima di release o modifiche importanti
- durante upgrade del target framework
- quando warning, asincronia, risorse o dipendenze risultano fragili

## Quando non usarla

- si deve diagnosticare un singolo bug non compreso
- l'ambito è una patch limitata già isolata
- si vuole implementare direttamente un requisito approvato

## Prerequisiti

- soluzione o progetto accessibile
- SDK .NET compatibile disponibile quando possibile
- target framework identificabile
- comandi di build e test noti o deducibili

## Materiale necessario

- file .sln/.slnx e .csproj
- configurazioni NuGet
- suite di test
- analizzatori e impostazioni compiler
- configurazioni applicative pertinenti

## Procedura operativa

1. Individuare soluzione, progetti, target framework e dipendenze NuGet.
2. Verificare build, warning, analizzatori e test.
3. Controllare nullable reference types, eccezioni e cancellazione asincrona.
4. Analizzare responsabilità, dipendenze statiche e dependency injection.
5. Verificare async/await, IDisposable, stream e risorse native.
6. Controllare configurazione, logging, serializzazione e accesso dati.
7. Produrre problemi prioritizzati e piano di miglioramento.

## Controlli

- target framework supportato
- warning gestiti in modo coerente
- assenza di blocchi sincroni ingiustificati su codice asincrono
- cancellazione propagata dove necessaria
- risorse rilasciate
- test sulle aree critiche
- pacchetti NuGet necessari e coerenti

## Errori frequenti

- usare .Result o .Wait() senza necessità
- catturare Exception senza azione utile
- classi di servizio troppo grandi
- stato globale mutabile
- logica applicativa nella UI
- segreti hardcoded

## Rapporto finale

Indicare versione .NET, struttura soluzione, esito restore/build/test, warning, problemi con file e simboli, rischi, correzioni consigliate e ordine di intervento.

## Condizioni di uscita

- soluzione compresa
- build verificata o impedimento motivato
- test registrati
- problemi prioritizzati
- piano operativo prodotto

## Cronologia delle versioni

- **0.2.0** — Struttura uniformata a `STANDARD.md`; requisiti, controlli, rapporto e condizioni di uscita resi espliciti.
- **0.1.0** — Prima versione operativa.
