# Piano tecnico — Omega FL Pilot issue #22

## Obiettivo

Eseguire, **solo dopo la chiusura con evidenza accettata dei review gate SecAgg v2**, la validazione fisica multi-PC del provider revisionato e preparare/pubblicare `v0.12.0-rc2` senza alterare `rc1`.

## Baseline dichiarata

`c2af618bc5851aaa4a67169ca5090293f29e48e7`

## Blocco iniziale non negoziabile

**NON AVVIARE la validazione multi-PC finché le evidenze richieste dalle issue #19, #20 e #21 non sono state accettate.**

Gate dipendenti:

- #19 — review crittografica e protocollo, con decisione esplicita di attivazione;
- #20 — second implementation/reference vectors e validazione adversarial indipendente;
- #21 — lifecycle/disposal del materiale effimero e rischio residuo CPython.

Il completamento formale delle issue senza evidenze attribuibili non soddisfa la dipendenza.

## Fuori ambito

- cambiare la costruzione crittografica durante la validazione fisica;
- accettare nuovi provider non inclusi nella review;
- spostare o sovrascrivere il tag `rc1`;
- dichiarare zeroizzazione deterministica non dimostrata;
- chiudere readiness gate sulla base di aspettative invece che di artefatti attribuibili.

## Attività

### OP22-00 — Accettare i gate di review

- **Obiettivo:** dimostrare che #19, #20 e #21 hanno evidenza completa e disposizioni dei findings.
- **Dipendenze:** nessuna attività fisica #22 può precederla.
- **File:** `docs/reviews/`, `docs/SECAGG_V2_READINESS.json` solo dove autorizzato dalle evidenze.
- **Passi:** verificare SHA completo, reviewer/organizzazione, findings, disposition, residual risk e activation decision per ciascun gate.
- **Test:** controllo manuale attribuibilità + workflow/review package pertinente.
- **Accettazione:** tre gate con evidenze accettate; nessun finding bloccante irrisolto.
- **Rischio:** Alto.
- **Stima:** variabile/esterna.

### OP22-01 — Congelare build e provider revisionato

- **Obiettivo:** impedire deriva tra oggetto revisionato e oggetto validato.
- **Dipendenze:** OP22-00.
- **File:** provider registry/configurazione, commit/tag candidato, readiness JSON.
- **Passi:** registrare SHA finale; selezionare esclusivamente il provider id revisionato; verificare activation interlock/allowlist; registrare hash del build.
- **Test:** provider activation check.
- **Accettazione:** provider e commit corrispondono alle evidenze delle review.
- **Rischio:** Alto.
- **Stima:** S.

### OP22-02 — Preparare matrice e inventario multi-PC

- **Obiettivo:** rendere la prova fisica riproducibile.
- **Dipendenze:** OP22-01.
- **File:** `docs/reviews/SECAGG_V2_MULTI_PC_VALIDATION_TEMPLATE.md` e allegati evidenza.
- **Passi:** identificare macchine fisicamente distinte; OS/runtime/hardware; identità client; rete; hash binari; orologi; comandi; directory output.
- **Test:** checklist di completezza prima della prima run.
- **Accettazione:** ogni macchina e artefatto ha identità e checksum registrati.
- **Rischio:** Medio.
- **Stima:** M.

### OP22-03 — Definire scenari di validazione

- **Obiettivo:** coprire tutti i percorsi richiesti dall'issue.
- **Dipendenze:** OP22-02.
- **Scenari obbligatori:** completamento normale; early dropout; late dropout; retry/idempotency; replay rejection; recovery failure.
- **Per ogni scenario:** precondizioni, partecipanti, soglia, input, evento iniettato, risultato atteso, log attesi, criteri pass/fail.
- **Test:** dry-run della matrice senza dichiarare readiness.
- **Accettazione:** ogni requisito #22 è mappato ad almeno uno scenario.
- **Rischio:** Medio.
- **Stima:** M.

### OP22-04 — Eseguire validazione fisica

- **Obiettivo:** ottenere evidenza attribuibile multi-PC.
- **Dipendenze:** OP22-03.
- **Passi:** eseguire uno scenario alla volta sul build congelato; non correggere durante la stessa run; conservare output grezzi; ripetere solo con nuova run-id documentata.
- **Test:** scenari OP22-03.
- **Accettazione:** tutti gli scenari hanno esito e artefatti; failure non vengono cancellate dal report.
- **Rischio:** Alto.
- **Stima:** L.

### OP22-05 — Costruire bundle evidenze

- **Obiettivo:** rendere ogni conclusione riconducibile a dati originali.
- **Dipendenze:** OP22-04.
- **Passi:** raccogliere log, hash, identità, ambiente, run-id, timestamp e checksum; compilare il template multi-PC; collegare scenari e risultati.
- **Test:** ricalcolo checksum e verifica presenza artefatti.
- **Accettazione:** template completo e nessun riferimento a file mancante.
- **Rischio:** Medio.
- **Stima:** M.

### OP22-06 — Aggiornare readiness da evidenza

- **Obiettivo:** aggiornare `docs/SECAGG_V2_READINESS.json` senza dichiarazioni non supportate.
- **Dipendenze:** OP22-05.
- **Passi:** chiudere soltanto gate dimostrati; inserire riferimenti a SHA/report/artefatti; lasciare aperto ogni gate dubbio.
- **Test:** validatori readiness/provider esistenti.
- **Accettazione:** ogni stato `complete` possiede evidenza attribuibile.
- **Rischio:** Alto.
- **Stima:** S-M.

### OP22-07 — Eseguire release gate canonico

- **Obiettivo:** verificare candidato dopo l'aggiornamento readiness.
- **Dipendenze:** OP22-06.
- **Passi:** eseguire pipeline canonica senza modifiche post-test; verificare package, SBOM, checksum, Docker E2E e provider activation.
- **Test:** release gate ufficiale.
- **Accettazione:** tutti i gate richiesti verdi sul commit candidato.
- **Rischio:** Alto.
- **Stima:** M.

### OP22-08 — Costruire e vincolare rc2

- **Obiettivo:** produrre artefatti riproducibili legati al commit finale.
- **Dipendenze:** OP22-07.
- **Passi:** costruire package/artefatti; generare SBOM e checksum; registrare commit; verificare installazione/avvio; non muovere rc1.
- **Test:** verifica artefatti e checksum; confronto tag esistente rc1.
- **Accettazione:** artefatti rc2 riconducibili al commit finale; rc1 immutato.
- **Rischio:** Alto.
- **Stima:** M.

### OP22-09 — Pubblicare v0.12.0-rc2

- **Obiettivo:** pubblicare soltanto il candidato che ha superato OP22-07/08.
- **Dipendenze:** OP22-08.
- **Passi:** creare tag/release rc2; allegare artefatti; pubblicare note con limiti/residual risk; ricontrollare immutabilità rc1.
- **Test:** scaricamento e verifica checksum degli artefatti pubblicati.
- **Accettazione:** rc2 pubblicata e legata allo SHA finale; rc1 invariata.
- **Rischio:** Alto.
- **Stima:** S-M.

## Mappa requisiti → attività

| Requisito issue #22 | Attività |
| --- | --- |
| review gate accettati prima della prova | OP22-00 |
| solo provider revisionato | OP22-01 |
| macchine fisicamente distinte | OP22-02, OP22-04 |
| normal/dropout/retry/replay/recovery failure | OP22-03, OP22-04 |
| log/hash/identità/ambiente/checksum | OP22-02, OP22-05 |
| readiness solo da evidenza | OP22-06 |
| provider activation check | OP22-01, OP22-07 |
| canonical package/SBOM/checksum/Docker E2E | OP22-07, OP22-08 |
| artifact binding al commit finale | OP22-08, OP22-09 |
| rc1 immutabile | OP22-08, OP22-09 |

## Stato attuale del piano

**BLOCCATO DA PRECONDIZIONI.** Al momento della pianificazione le issue #19, #20 e #21 risultano aperte. Il piano è pronto all'esecuzione, ma OP22-01 e successive non devono iniziare finché OP22-00 non è realmente soddisfatta.
