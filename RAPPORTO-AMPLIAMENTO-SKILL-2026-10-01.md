# Rapporto ampliamento skill — 2026-10-01

## Sintesi

È stato ampliato il progetto **Arsenale IA** come biblioteca italiana locale di procedure operative e competenze per agenti.

Il lavoro ha riguardato:

- ampliamento del catalogo da 20 a 54 procedure;
- successivo ampliamento da 54 a 56 procedure;
- creazione di nuove categorie operative;
- aggiunta di adattatori `SKILL.md` per ogni nuova procedura;
- aggiornamento del router degli agenti;
- aggiornamento della guida rapida;
- verifica automatica locale della struttura.

Il progetto resta orientato all'uso locale. Non è stata richiesta né svolta pubblicazione su GitHub.

## Stato finale

- Procedure disponibili nel catalogo: **56**
- Procedure conformi allo standard: **56/56**
- Procedure con adattatore `SKILL.md`: **56/56**
- Procedure già verificate con evidenze operative: **6**
- Nuove procedure aggiunte rispetto alla versione da 20: **36**
- Nuove procedure ancora da verificare operativamente rispetto alla versione da 20: **36**
- Codici pianificati non ancora disponibili: **4**
- Totale codici catalogati: **60**

Nota: una procedura **Disponibile** è presente nel catalogo e utilizzabile. Lo stato **Verificata** richiede invece prove operative archiviate secondo `VERIFICA.md`.

## File principali aggiornati

- `README.md`
- `START_HERE.md`
- `AGENTI.md`
- `CATALOGO.md`
- `COMPATIBILITA.md`
- `Procedure/`
- `Strumenti/genera_procedure_consigliate.ps1`

## Nuove categorie inserite

### Documentazione e manualistica

Procedure aggiunte:

- `ARI-1101 — Documentazione tecnica progetto`
- `ARI-1102 — Manuale utente locale`
- `ARI-1103 — Glossario italiano tecnico`
- `ARI-1104 — Revisione e correzione testi`

Scopo: rendere il progetto documentabile, leggibile, correggibile e coerente in italiano tecnico.

### Automazione locale

Procedure aggiunte:

- `ARI-1201 — Automazione PowerShell`
- `ARI-1202 — Automazione Python CLI`
- `ARI-1203 — Flusso locale ripetibile`

Scopo: creare automazioni locali, ripetibili e controllabili senza dipendere da servizi esterni.

### Gestione locale e manutenzione

Procedure aggiunte:

- `ARI-1301 — Pulizia progetto locale`
- `ARI-1302 — Gestione backup locali`
- `ARI-1303 — Inventario progetto locale`
- `ARI-1304 — Ripristino controllato locale`

Scopo: mantenere il progetto ordinato, recuperabile e verificabile.

### Applicazioni desktop Windows

Procedure aggiunte:

- `ARI-1401 — Confezionamento app Windows`
- `ARI-1402 — Installatore Windows locale`
- `ARI-1403 — Icone e metadati app`

Scopo: preparare applicazioni Windows locali, installatori e metadati applicativi.

### Intelligenza artificiale e agenti

Procedure aggiunte:

- `ARI-1502 — Ottimizzazione inferenza locale`
- `ARI-1601 — Revisione modelli linguistici`
- `ARI-1701 — Revisione agenti IA`
- `ARI-1702 — Progettazione memoria agente`
- `ARI-1703 — Valutazione strumenti agente`
- `ARI-1704 — Orchestrazione multi-agente locale`
- `ARI-1705 — Progettazione prompt per agenti`

Scopo: coprire modelli locali, prestazioni, progettazione agenti, memoria, strumenti e prompt operativi.

### Web, applicazioni, grafica e risorse

Procedure aggiunte o consolidate:

- `ARI-2101 — Revisione siti web statici`
- `ARI-2102 — Revisione applicazioni web complete e a pagina singola`
- `ARI-2103 — Design e accessibilità interfaccia`
- `ARI-2104 — Prestazioni esperienza utente e interfaccia web/app`
- `ARI-2105 — Ricerca e selezione risorse visive`
- `ARI-2106 — Replica funzionale legale di un sito`
- `ARI-2107 — App Windows con interfaccia stile iOS/macOS`
- `ARI-2108 — Esperienza utente, accessibilità e conversione`

Scopo: creare e revisionare siti, applicazioni, interfacce, asset, repliche funzionali legali e app Windows con estetica iOS/macOS.

### Sicurezza, licenze e privacy

Procedure aggiunte:

- `ARI-2201 — Revisione sicurezza web e app`
- `ARI-2202 — Gestione segreti locali`
- `ARI-2203 — Privacy e dati personali`
- `ARI-2204 — Licenze risorse e dipendenze`

Scopo: controllare rischi tecnici, segreti, dati personali, licenze e dipendenze.

### Browser e test interfaccia

Procedure aggiunte:

- `ARI-2501 — Automazione browser controllata`
- `ARI-2502 — Test end-to-end interfaccia`
- `ARI-2503 — Audit schermate adattive`

Scopo: verificare flussi browser, schermate, layout adattivi e comportamento interfaccia.

## Nuove skill finali richieste

### `ARI-1104 — Revisione e correzione testi`

Questa skill corregge e riscrive testi proposti dall'utente.

Competenze principali:

- correzione grammaticale;
- riscrittura tecnica;
- mantenimento del significato originale;
- miglioramento di chiarezza, tono e struttura;
- correzione di prompt, messaggi, documentazione e manuali.

Esempio:

```text
Correggi questo testo e rendilo più tecnico.
```

### `ARI-1705 — Progettazione prompt per agenti`

Questa skill crea e migliora prompt per agenti IA.

Competenze principali:

- definizione ruolo agente;
- definizione obiettivo;
- definizione strumenti e limiti;
- definizione formato di risposta;
- criteri di completamento;
- trasformazione di idee grezze in istruzioni operative.

Esempio:

```text
Crea un prompt per un agente che revisiona siti web.
```

## Router aggiornato

Il file `AGENTI.md` è stato aggiornato per instradare le richieste in linguaggio naturale.

Esempi:

```text
Correggi questo testo.
```

Instradamento:

```text
Agente Documentazione / ARI-1104
```

```text
Crea un prompt per un agente.
```

Instradamento:

```text
Agente IA / ARI-1705
```

```text
Crea una app Windows stile iOS/macOS.
```

Instradamento:

```text
Agente Web/App/Grafica / ARI-2107
Agente Desktop Windows / ARI-1401
```

## Verifiche eseguite

Sono stati eseguiti i controlli locali:

```powershell
python Strumenti/verifica_procedure.py
python Strumenti/verifica_skills.py
python Strumenti/verifica_evidenze.py
python Strumenti/verifica_promozioni.py
python -m unittest Strumenti.test_verifica_evidenze Strumenti.test_verifica_promozioni
```

Esiti registrati:

```text
VERIFICA PROCEDURE SUPERATA: 56 procedure conformi a STANDARD.md
OK: 56 procedure, 56 adattatori SKILL.md validi e nomi runtime univoci
VERIFICA EVIDENZE SUPERATA: 12 rapporti strutturalmente validi
VERIFICA PROMOZIONI SUPERATA: 6 procedure Verificate rispettano la soglia automatizzabile
Ran 9 tests — OK
```

## Correzione matrice operativa

Durante il controllo successivo è stata rilevata un'anomalia: il catalogo dichiarava **56 procedure disponibili**, ma la matrice di verifica operativa conteneva solo **47 righe**.

Mancavano queste procedure già disponibili:

- `ARI-0101 — Revisione Python`
- `ARI-0201 — Revisione C#`
- `ARI-0301 — Revisione C++`
- `ARI-0401 — Revisione JavaScript e TypeScript`
- `ARI-0501 — Revisione database`
- `ARI-0601 — Revisione Git`
- `ARI-0701 — Revisione Docker`
- `ARI-0801 — Diagnostica Windows`
- `ARI-0901 — Diagnostica Linux`

La matrice è stata corretta e portata a **56 righe operative**.

È stato inoltre esteso il validatore `Strumenti/verifica_promozioni.py` affinché confronti automaticamente:

- procedure dichiarate **Disponibile** nel catalogo;
- righe presenti nella matrice `Verifica operativa`.

In questo modo una matrice incompleta viene intercettata dai controlli locali.

## Limiti residui

Le nuove procedure sono disponibili e strutturalmente valide, ma non sono ancora tutte verificate con prove operative reali.

Azioni residue consigliate:

1. usare ogni nuova procedura in un caso reale;
2. creare due evidenze operative per procedura;
3. includere almeno una prova indipendente;
4. promuovere lo stato solo quando la soglia di `VERIFICA.md` è rispettata.

## Stato operativo

Il progetto ora funziona come biblioteca locale più ampia e meno dispersiva:

- l'utente può chiedere in linguaggio naturale;
- `START_HERE.md` guida l'uso rapido;
- `AGENTI.md` sceglie il macro-agente;
- `CATALOGO.md` conserva l'elenco ufficiale;
- ogni procedura ha il proprio `PROCEDURA.md`;
- ogni competenza ha il proprio `SKILL.md`.

Verdetto: **Idoneo con vincoli**.

Motivo: struttura, catalogo e adattatori sono validi; la verifica operativa completa delle nuove procedure resta da svolgere su casi reali.
