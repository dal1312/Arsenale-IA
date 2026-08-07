# Piano operativo — Completamento verifica v0.5

## Obiettivo

Portare le procedure del nucleo ancora non verificate, da ARI-0005 a ARI-0010, allo stato **Verificata** solo quando soddisfano `VERIFICA.md`, quindi eseguire una revisione incrociata della matrice prima di dichiarare conclusa la v0.5.

## Punto di partenza

- ARI-0001 — Verificata
- ARI-0002 — Verificata
- ARI-0003 — Verificata
- ARI-0004 — in verifica tramite il presente piano e una prova indipendente
- ARI-0005…ARI-0010 — da verificare

## Vincoli

- almeno due evidenze valide per procedura;
- almeno una prova indipendente da Arsenale IA per procedura;
- nessuna promozione basata sulla sola conformità automatica;
- ogni rapporto deve riferirsi a una versione registrata della procedura;
- nessuna modifica a repository esterni solo per creare una prova;
- CI Arsenale verde su Ubuntu e Windows prima di ogni merge;
- separare sempre analisi/review/diagnosi dalla successiva implementazione.

## Fuori ambito

- procedure specialistiche ARI-0101 e successive;
- creazione delle procedure IA pianificate ARI-1501+;
- scelta della licenza del repository;
- prima release/tag formale di Arsenale IA;
- modifiche opportunistiche a progetti esterni non richieste dal loro contesto.

## Dipendenze

```text
ARI-0004 piano v0.5
  ├─ ARI-0005 Implementazione controllata
  ├─ ARI-0006 Refactoring controllato
  ├─ ARI-0007 Analisi prestazioni
  ├─ ARI-0008 Analisi sicurezza
  ├─ ARI-0009 Verifica test
  └─ ARI-0010 Preparazione rilascio
          ↓
  Revisione incrociata matrice
          ↓
  Chiusura v0.5
```

Le verifiche ARI-0005…ARI-0010 possono procedere indipendentemente quando esistono casi reali adeguati. La revisione incrociata finale dipende dal completamento di tutte.

## Attività

### V05-01 — Verificare ARI-0005 Implementazione controllata

- **Obiettivo:** dimostrare implementazione incrementale da requisito approvato a criteri di accettazione soddisfatti.
- **Dipendenze:** requisito/piano reale già definito; baseline test disponibile.
- **File/moduli Arsenale:** `Verifiche/ARI-0005/`, procedura, catalogo, roadmap.
- **Passi:** selezionare caso interno; selezionare caso indipendente già autorizzato/realizzato; registrare baseline, incrementi, test e build; produrre due rapporti.
- **Test:** validatore evidenze + CI multipiattaforma.
- **Criterio di accettazione:** 2 rapporti `Valida`, almeno 1 indipendente, metodo coperto, nessuna contraddizione aperta.
- **Rischio:** confondere una patch già esistente con una prova di implementazione incrementale.
- **Stima relativa:** M.

### V05-02 — Verificare ARI-0006 Refactoring controllato

- **Obiettivo:** dimostrare un cambiamento strutturale con comportamento preservato.
- **Dipendenze:** test di caratterizzazione o suite sufficiente prima/dopo.
- **File/moduli:** `Verifiche/ARI-0006/`, procedura, catalogo, roadmap.
- **Passi:** scegliere due refactoring reali; registrare comportamento da preservare; confrontare test/build e trasformazioni; produrre rapporti.
- **Test:** suite prima/dopo + validatori Arsenale.
- **Criterio di accettazione:** comportamento invariato dimostrato e nessuna funzionalità nuova mescolata.
- **Rischio:** classificare come refactoring una modifica funzionale.
- **Stima relativa:** M.

### V05-03 — Verificare ARI-0007 Analisi prestazioni

- **Obiettivo:** dimostrare baseline, collo di bottiglia e confronto equivalente prima/dopo o piano motivato.
- **Dipendenze:** scenario misurabile e metriche disponibili.
- **File/moduli:** `Verifiche/ARI-0007/`, procedura, catalogo, roadmap.
- **Passi:** selezionare benchmark reali; registrare ambiente e dati; ripetere misure; localizzare percorso critico; verificare intervento quando disponibile.
- **Test:** confronto metriche ripetibili + correttezza funzionale.
- **Criterio di accettazione:** nessuna conclusione prestazionale senza baseline misurata.
- **Rischio:** usare run non comparabili.
- **Stima relativa:** M-L.

### V05-04 — Verificare ARI-0008 Analisi sicurezza

- **Obiettivo:** dimostrare classificazione prudente delle evidenze e mitigazioni verificabili.
- **Dipendenze:** ambito autorizzato e codice/configurazioni disponibili.
- **File/moduli:** `Verifiche/ARI-0008/`, procedura, catalogo, roadmap.
- **Passi:** due audit reali; mappa superfici; controlli auth/input/segreti/dipendenze; classificazione confermata/probabile/da verificare; mitigazioni.
- **Test:** controlli difensivi e CI; nessun segreto riportato in chiaro.
- **Criterio di accettazione:** 2 prove valide con almeno una indipendente e nessuna vulnerabilità inventata.
- **Rischio:** sovrastimare findings senza prova.
- **Stima relativa:** L.

### V05-05 — Verificare ARI-0009 Verifica test

- **Obiettivo:** valutare qualità reale di suite e copertura dei comportamenti critici.
- **Dipendenze:** suite eseguibile o risultati CI tracciabili.
- **File/moduli:** `Verifiche/ARI-0009/`, procedura, catalogo, roadmap.
- **Passi:** eseguire/analizzare suite; conteggi; skip/flaky; asserzioni; mock; lacune; piano miglioramento.
- **Test:** ripetizione dei test sospetti quando possibile.
- **Criterio di accettazione:** i rapporti non usano la sola coverage come verdetto.
- **Rischio:** confondere CI verde con suite adeguata.
- **Stima relativa:** M.

### V05-06 — Verificare ARI-0010 Preparazione rilascio

- **Obiettivo:** validare un candidato di rilascio reale fino a go/no-go e rollback.
- **Dipendenze:** release candidate identificabile con artefatti e pipeline.
- **File/moduli:** `Verifiche/ARI-0010/`, procedura, catalogo, roadmap.
- **Passi:** tag/commit, test/build/package, installazione, configurazioni, migrazioni, note, rollback, verdetto.
- **Test:** artefatto reale e controlli release esistenti.
- **Criterio di accettazione:** 2 prove valide, almeno una indipendente, decisione finale supportata da artefatti.
- **Rischio:** verificare solo il codice e non il pacchetto finale.
- **Stima relativa:** L.

### V05-07 — Revisione incrociata della matrice

- **Obiettivo:** assicurare che tutte le promozioni del nucleo rispettino la stessa soglia.
- **Dipendenze:** V05-01…V05-06 completate.
- **File/moduli:** `CATALOGO.md`, `Verifiche/`, `ROADMAP.md`, `VERIFICA.md`.
- **Passi:** contare evidenze; verificare indipendenza; controllare versioni; cercare prove duplicate o auto-referenziali; controllare limiti irrisolti.
- **Test:** `verifica_procedure.py`, `verifica_skills.py`, `verifica_evidenze.py`, unittest e CI Windows/Linux.
- **Criterio di accettazione:** ARI-0001…ARI-0010 tutte coerenti con `VERIFICA.md` oppure v0.5 resta aperta con motivazione.
- **Rischio:** trasformare la roadmap in una checklist formale senza riesaminare la qualità delle evidenze.
- **Stima relativa:** M.

## Ordine consigliato

1. ARI-0005 e ARI-0009, perché esistono già modifiche e suite reali utilizzabili come casi.
2. ARI-0006 e ARI-0007, selezionando solo casi con baseline verificabile.
3. ARI-0008, con particolare cautela sulla classificazione delle evidenze.
4. ARI-0010, usando release candidate reali e artefatti verificabili.
5. Revisione incrociata V05-07.

## Criterio finale di completamento v0.5

La v0.5 può passare a **Completata** solo quando ARI-0001…ARI-0010 risultano tutte **Verificata**, ciascuna con almeno due rapporti validi e una prova indipendente, e la CI Arsenale è verde su Windows e Ubuntu dopo la revisione incrociata.
