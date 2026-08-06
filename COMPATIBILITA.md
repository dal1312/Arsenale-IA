# Compatibilità con Codex e altri agenti

## Scopo

Arsenale IA adotta un modello **local-first**: `PROCEDURA.md` contiene il metodo canonico, mentre `SKILL.md` è un adattatore leggero per i client che supportano il formato Agent Skills.

GitHub è utile per distribuire e versionare il progetto, ma non è una dipendenza runtime. Una copia locale del repository è sufficiente.

## Modello sorgente

```text
Procedure/
└── ARI-0001-Revisione-Repository/
    ├── PROCEDURA.md
    └── SKILL.md
```

Le cartelle sorgenti mantengono il codice ARI. Lo standard Agent Skills richiede invece che la cartella runtime abbia lo stesso nome dichiarato nel campo `name` di `SKILL.md`.

Gli installatori locali trasformano quindi il modello sorgente in:

```text
<radice-skills>/
└── revisione-repository/
    ├── SKILL.md
    └── PROCEDURA.md
```

Non viene scaricato nulla dalla rete.

## Verifica degli adattatori

Da Windows:

```powershell
py Strumenti/verifica_skills.py
```

Da Linux/macOS:

```bash
python3 Strumenti/verifica_skills.py
```

Il controllo verifica presenza, front matter minimo, nomi univoci, descrizione e riferimento a `PROCEDURA.md`.

## Codex

Codex carica le skill locali da `.agents/skills` nel repository oppure da `~/.agents/skills` per l'utente.

### Installazione utente — Windows

```powershell
.\Strumenti\Installa-Skills.ps1 -Destinazione Codex -Forza
```

### Installazione utente — Linux/macOS

```bash
./Strumenti/installa-skills.sh codex
```

### Installazione nel progetto corrente — Windows

Dalla radice del progetto nel quale vuoi usare le procedure:

```powershell
& "C:\percorso\Arsenale-IA\Strumenti\Installa-Skills.ps1" `
  -Destinazione Personalizzato `
  -Percorso ".agents\skills" `
  -Forza
```

### Esempi Codex

Invocazione esplicita:

```text
$revisione-repository Analizza questo repository e fermati al piano prioritizzato.
```

```text
$diagnosi-errori Riproduci il problema descritto nel ticket e individua la causa radice prima di correggerlo.
```

```text
$implementazione-controllata Applica il piano approvato in PLAN.md e verifica ogni incremento.
```

Codex può anche selezionare una skill in base alla `description` quando la richiesta corrisponde al suo ambito.

## Claude Code

Claude Code usa normalmente `.claude/skills` nel progetto oppure `~/.claude/skills` per l'utente.

### Installazione utente — Windows

```powershell
.\Strumenti\Installa-Skills.ps1 -Destinazione Claude -Forza
```

### Installazione utente — Linux/macOS

```bash
./Strumenti/installa-skills.sh claude
```

### Esempi Claude Code

```text
/revisione-codice Controlla le modifiche rispetto al requisito e non riscrivere automaticamente il codice.
```

```text
/analisi-prestazioni Misura il percorso lento, registra la baseline e proponi interventi solo dopo il profiling.
```

Le skill sono invocabili dall'utente per impostazione predefinita; non è necessario aggiungere campi proprietari al front matter comune.

## Altri client Agent Skills

Per un client che supporta Agent Skills ma usa una cartella differente, indicare una destinazione personalizzata.

Windows:

```powershell
.\Strumenti\Installa-Skills.ps1 `
  -Destinazione Personalizzato `
  -Percorso "D:\Agente\skills" `
  -Forza
```

Linux/macOS:

```bash
./Strumenti/installa-skills.sh custom "$HOME/mio-agente/skills"
```

Poi configurare il client affinché legga quella radice.

## Agenti senza supporto nativo a SKILL.md

Le procedure restano utilizzabili direttamente. Esempio di istruzione generica:

```text
Leggi integralmente Procedure/ARI-0003-Diagnosi-Errori/PROCEDURA.md.
Applicala come metodo operativo al problema corrente.
Distingui fatti, ipotesi e informazioni mancanti e documenta le verifiche eseguite.
```

Questo percorso non richiede GitHub né un sistema di plugin.

## Aggiornamento locale

Dopo aver modificato gli adattatori sorgente, rieseguire l'installatore con `-Forza` su Windows oppure lo script shell sulla stessa destinazione. I file runtime vengono riallineati alla copia locale di Arsenale IA.

## Principio di compatibilità

1. Una sola fonte metodologica: `PROCEDURA.md`.
2. Un adattatore piccolo: `SKILL.md`.
3. Nessuna dipendenza da GitHub durante l'uso locale.
4. Nessuna regola specifica di un singolo agente dentro la procedura canonica.
5. Cartella runtime conforme al `name` dichiarato dalla skill.
