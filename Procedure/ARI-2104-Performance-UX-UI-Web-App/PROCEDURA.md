# ARI-2104 — Prestazioni esperienza utente e interfaccia web/app

- **Categoria:** Web, Applicazioni, Interfacce e Risorse
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.1.0
- **Utilizzo offline:** Sì

## Scopo

Analizzare e migliorare prestazioni percepite e misurabili di interfacce web e app, collegando tempi di caricamento, reattività, stabilità visuale e peso delle risorse all'esperienza utente reale.

## Campo di applicazione

Siti, applicazioni web, pannelli di controllo, applicazioni web installabili e interfacce desktop basate su tecnologie web. La procedura copre rendering, risorse, pacchetti, font, immagini, caricamento differito, interazioni, stabilità del layout e flussi operativi critici.

## Quando usarla

- prima di rilascio pubblico o demo importante
- quando l'app appare lenta o instabile
- dopo introduzione di immagini, animazioni o librerie pesanti
- quando Lighthouse o metriche real user indicano degrado

## Quando non usarla

- il problema principale è il servizio applicativo o una query database
- mancano costruzione o ambiente eseguibile
- serve solo un giudizio estetico
- non è possibile distinguere rete, device e codice applicativo

## Prerequisiti

- scenario utente da misurare
- ambiente locale o URL controllabile
- dispositivo o finestra di visualizzazione target
- costruzione rappresentativa
- soglie o obiettivi minimi di prestazioni

## Materiale necessario

- codice sorgente e risorse
- rapporto Lighthouse, DevTools o metriche equivalenti se disponibili
- elenco risorse principali
- configurazione di costruzione e strumento di pacchettizzazione
- screenshot o registrazioni del problema quando presenti

## Procedura operativa

1. Definire scenario critico, dispositivo target e metrica prioritaria.
2. Distinguere caricamento iniziale, navigazione successiva, interazione e stabilità visuale.
3. Misurare o stimare peso di pacchetti, immagini, font e richieste principali.
4. Identificare blocchi di rendering, script non necessari, immagini sovradimensionate e font caricati male.
5. Valutare reattività degli input, transizioni, schermate provvisorie e gestione degli stati lenti.
6. Controllare stabilità del layout, overflow, ricalcoli e componenti che causano rendering inutili.
7. Proporre interventi ordinati per impatto, rischio e costo.
8. Separare ottimizzazioni misurabili da rifiniture soggettive.

## Controlli

- scenario e dispositivo target dichiarati
- risorse principali inventariate
- immagini dimensionate e compresse in modo adeguato
- font limitati e caricati con strategia ragionevole
- pacchetti e dipendenze pesanti giustificati
- stati lenti gestiti in modo leggibile
- layout stabile durante caricamento e interazione
- raccomandazioni collegate a metriche o evidenze

## Errori frequenti

- ottimizzare numeri di laboratorio ignorando il flusso reale
- caricare immagini principali troppo grandi
- introdurre animazioni costose per micro-interazioni
- usare molte famiglie font e pesi non necessari
- non distinguere lentezza servizio applicativo da lentezza interfaccia client
- proporre riscritture totali senza misurare il collo di bottiglia

## Rapporto finale

Riportare scenario, ambiente, metriche o osservazioni, colli di bottiglia, priorità degli interventi, rischio regressione, prove consigliate e verdetto. Specificare cosa migliorare subito e cosa rinviare.

## Condizioni di uscita

- scenario misurato o osservato chiaramente
- cause probabili ordinate per impatto
- interventi applicabili e proporzionati
- limiti delle misure dichiarati
- verdetto operativo pronto per pianificazione

## Cronologia delle versioni

- **0.1.0** — Prima versione per prestazioni di esperienza utente e interfaccia web/app.

