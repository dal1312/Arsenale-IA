# ARI-2107 — App Windows con interfaccia stile iOS/macOS

- **Categoria:** Web, Applicazioni, Interfacce e Risorse
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.1.0
- **Utilizzo offline:** Sì

## Scopo

Progettare o revisionare applicazioni Windows con interfaccia ispirata a iOS/macOS, mantenendo ergonomia scrivania, coerenza tecnica, prestazioni e differenziazione da brand o componenti proprietari.

## Campo di applicazione

App Windows realizzate con Electron, Tauri, Flutter, .NET MAUI, WinUI, WPF, Qt o interfaccia client web impacchettato. La procedura copre finestre, navigazione, controlli, tema, confezionamento, input scrivania e look Apple-like originale.

## Quando usarla

- quando si crea un'app Windows con grafica iOS/macOS
- quando si porta una applicazione web su scrivania
- quando si sceglie tra Electron, Tauri, Flutter, MAUI o WinUI
- prima di confezionamento o distribuzione Windows

## Quando non usarla

- si vuole creare un'app iOS nativa
- l'obiettivo è copiare componenti Apple protetti in modo indistinguibile
- l'app richiede driver, kernel mode o integrazioni Windows non UI
- il progetto non ha requisiti di piattaforma Windows

## Prerequisiti

- funzionalità principali dell'app definite
- target Windows e modalità di distribuzione chiariti
- stack candidato o vincoli tecnologici noti
- stile visuale richiesto e limiti di brand dichiarati
- requisiti di input mouse, tastiera, touch e ridimensionamento finestra

## Materiale necessario

- sorgente o specifica dell'app
- wireframe o riferimento visuale autorizzato
- elenco schermate e flussi principali
- requisiti di confezionamento, update e firma se presenti
- asset, icone e font con licenza valida
- metriche minime di prestazione e memoria quando rilevanti

## Procedura operativa

1. Definire piattaforma, stack e vincoli di confezionamento Windows.
2. Stabilire principi visuali Apple-like: chiarezza, spacing, blur controllato, tipografia pulita e stati coerenti.
3. Adattare i pattern a uso scrivania: finestre ridimensionabili, tastiera, hover, focus, menu, file picker e notifiche.
4. Progettare componenti base: barra, sidebar, toolbar, bottoni icona, input, modali, liste e stati vuoti.
5. Controllare accessibilità, contrasto, focus, scaling DPI e comportamento con testo lungo.
6. Valutare prestazioni, memoria, startup time e peso del ambiente di esecuzione scelto.
7. Verificare confezionamento, icona, metadati, aggiornamento e configurazioni di distribuzione.
8. Segnalare rischi tecnici, visuali e legali con correzioni concrete.

## Controlli

- interfaccia coerente con Windows come piattaforma di esecuzione
- stile iOS/macOS reinterpretato e non copiato
- input scrivania completi: mouse, tastiera, focus e ridimensionamento
- componenti base con stati visibili
- nessun testo tagliato o layout instabile
- asset e icone licenziati
- confezionamento e avvio valutati
- prestazioni adeguate al ambiente di esecuzione scelto

## Errori frequenti

- creare una skin Apple-like senza comportamento scrivania
- usare blur e trasparenze eccessive con scarso contrasto
- ignorare DPI scaling e finestre strette
- scegliere Electron per app minime senza valutare peso
- copiare icone o marchi Apple
- trascurare installazione, update e firma

## Rapporto finale

Riportare stack, schermate, componenti, stile, rischi Windows, accessibilità, prestazioni, confezionamento e verdetto. Usare **Idonea**, **Idonea con vincoli**, **Non idonea** o **Inconcludente**.

## Condizioni di uscita

- stack e vincoli Windows chiariti
- componenti e pattern scrivania valutati
- stile Apple-like distinto da copia protetta
- rischi di confezionamento e prestazioni esplicitati
- raccomandazione operativa motivata

## Cronologia delle versioni

- **0.1.0** — Prima versione per app Windows con interfaccia stile iOS/macOS.

