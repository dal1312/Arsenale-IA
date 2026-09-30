# ARI-2103 — Design e accessibilità interfaccia

- **Categoria:** Web, Applicazioni, Interfacce e Risorse
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.1.0
- **Utilizzo offline:** Sì

## Scopo

Valutare e progettare interfacce coerenti, leggibili, accessibili e adatte al contesto d'uso, producendo indicazioni operative su layout, gerarchia, componenti, colori, tipografia e interazioni.

## Campo di applicazione

Interfacce web, app, pannello di controllo, pannelli scrivania, prototipi, sistema di progettazione e componenti UI. La procedura copre anche UI in stile iOS/macOS o altri linguaggi visuali quando richiesti, senza copiare brand o risorse protette.

## Quando usarla

- prima di implementare una nuova interfaccia
- quando un prodotto appare incoerente o poco leggibile
- per definire o correggere un sistema di progettazione
- quando servono controlli di accessibilità e usabilità

## Quando non usarla

- serve solo scegliere immagini o risorse esterne
- il problema principale è prestazionale o servizio applicativo
- si richiede copia fedele di brand, testi o asset non autorizzati
- mancano obiettivo utente e contesto operativo minimo

## Prerequisiti

- utenti o scenario d'uso identificati
- piattaforme e viewport target definiti
- vincoli di brand o stile dichiarati
- contenuti principali disponibili o rappresentativi
- requisiti minimi di accessibilità noti

## Materiale necessario

- screenshot, mockup o codice dell'interfaccia
- palette, font e componenti esistenti se presenti
- flussi principali e priorità utente
- riferimenti visuali autorizzati
- eventuali criteri WCAG o policy interne

## Procedura operativa

1. Definire scopo della schermata, utente primario e azione principale.
2. Valutare gerarchia visiva, densità, spacing, allineamenti, contrasto e leggibilità.
3. Controllare coerenza di componenti, stati, icone, affordance e feedback.
4. Verificare accessibilità: semantica, contrasto, focus, tastiera, label, target touch e riduzione del carico cognitivo.
5. Valutare adattamento adattivo e uso in input mouse, tastiera e touch quando rilevante.
6. Se richiesto stile iOS/macOS, tradurre principi visuali in pattern originali e compatibili con il prodotto.
7. Proporre modifiche concrete a componenti, layout, token visivi o contenuti.
8. Prioritizzare interventi tra bloccanti, alta utilità e rifiniture.

## Controlli

- azione primaria evidente
- gerarchia tipografica coerente
- contrasto e focus adeguati
- componenti con stati chiari
- icone comprensibili o supportate da tooltip
- nessuna sovrapposizione o overflow rilevante
- pattern visuali coerenti con piattaforma e pubblico
- elementi protetti non copiati senza autorizzazione

## Errori frequenti

- usare estetica Apple-like senza ergonomia reale
- aumentare dimensioni e blur invece di migliorare gerarchia
- ignorare tastiera e focus
- progettare solo per scrivania
- mischiare componenti con linguaggi visuali incompatibili
- confondere accessibilità con sola scelta dei colori

## Rapporto finale

Riportare contesto d'uso, schermate analizzate, principi visuali applicati, problemi di accessibilità e usabilità, modifiche proposte, token o componenti da aggiornare e verdetto finale.

## Condizioni di uscita

- obiettivo e utente dell'interfaccia chiariti
- rilievi visuali e accessibilità separati
- proposte applicabili a codice o sistema di progettazione
- limiti e assunzioni documentati
- decisione finale motivata

## Cronologia delle versioni

- **0.1.0** — Prima versione per design UI e accessibilità.

