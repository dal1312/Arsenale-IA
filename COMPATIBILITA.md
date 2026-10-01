# Compatibilità con Codex e altri agenti

## Scopo

Arsenale IA adotta un modello **prima locale**: `PROCEDURA.md` contiene il metodo canonico, mentre `SKILL.md` è un adattatore leggero per i client che supportano il formato Competenze agente.

GitHub è utile per distribuire e versionare il progetto, ma non è una dipendenza dell'ambiente di esecuzione. Una copia locale del repository è sufficiente.

## Modello sorgente

```text
Procedure/
└── ARI-0001-Revisione-Repository/
    ├── PROCEDURA.md
    └── SKILL.md
```

Le cartelle sorgenti mantengono il codice ARI. Lo standard Competenze agente richiede invece che la cartella di esecuzione abbia lo stesso nome dichiarato nel campo `name` di `SKILL.md`.

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

Codex carica le competenze locali da `.agents/skills` nel repository oppure da `~/.agents/skills` per l'utente.

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

Codex può anche selezionare una competenza in base alla `description` quando la richiesta corrisponde al suo ambito.

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

Le competenze sono invocabili dall'utente per impostazione predefinita; non è necessario aggiungere campi proprietari al front matter comune.

## Altri client Competenze agente

Per un client che supporta Competenze agente ma usa una cartella differente, indicare una destinazione personalizzata.

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

Dopo aver modificato gli adattatori sorgente, rieseguire l'installatore con `-Forza` su Windows oppure `--force` sullo script POSIX, indicando la stessa destinazione. Senza il flag di forzatura, le competenze già presenti vengono saltate. I file dell'ambiente di esecuzione vengono così riallineati alla copia locale di Arsenale IA.

## Principio di compatibilità

1. Una sola fonte metodologica: `PROCEDURA.md`.
2. Un adattatore piccolo: `SKILL.md`.
3. Nessuna dipendenza da GitHub durante l'uso locale.
4. Nessuna regola specifica di un singolo agente dentro la procedura canonica.
5. Cartella di esecuzione conforme al `name` dichiarato dalla competenza.


## Competenze multimediali locali

ARI-1803…ARI-1809 usano adattatori portabili con PROCEDURA.md relativo: gli installatori copiano entrambi i file e non installano motori/modelli. Le descrizioni distinguono audio generale, TTS, video deterministico, video IA e orchestrazione.

Esempio Codex: `$montaggio-multimediale-ffmpeg Analizza le sorgenti locali e prepara un piano di montaggio con controlli di sincronizzazione.`

Esempio Claude Code: `/trascrizione-audio-video-locale Verifica motore e modello già presenti prima di trascrivere il file locale.`

Per agenti senza supporto nativo leggere il PROCEDURA.md della cartella ARI corrispondente. Uso offline con strumenti/modelli già disponibili; nessun download, cloud o avvio server implicito. Confermare CLI/API nell'help/documentazione locali della versione specifica.

Per provare l'installatore POSIX usare destinazione personalizzata nuova. Il flag di aggiornamento è attualmente letto come terzo argomento: `sh Strumenti/installa-skills.sh custom "/percorso/skills" --force`. Le invocazioni `codex --force` e `claude --force` non attivano la forzatura nell'installatore attuale; difetto separato dall'ampliamento documentale.

## Sintesi vocale online Edge TTS

ARI-1810 usa il nome runtime `sintesi-vocale-edge-tts`. L'adattatore è autonomo: gli installatori copiano PROCEDURA.md e SKILL.md come per le altre competenze, senza dipendenze da script fuori dalla cartella. È distinto da `sintesi-vocale-locale` (ARI-1807): il testo è inviato al servizio online Microsoft Edge.

Esempio Codex: `$sintesi-vocale-edge-tts Genera un MP3 da questo testo con Diego e velocità -5%, senza modificare il testo.`

Esempio Claude Code: `/sintesi-vocale-edge-tts Leggi il file UTF-8 indicato con Elsa e velocità +0%.`

Nella copia sorgente del repository lo script facoltativo `Strumenti/Genera-Audio-Edge.ps1` automatizza selezione voce, directory nuova, sintesi, FFprobe, decodifica e manifest. Richiede Python con edge-tts, FFmpeg e FFprobe già disponibili; non installa nulla:

```powershell
.\Strumenti\Genera-Audio-Edge.ps1 -TestoFile '.	esto.txt'
.\Strumenti\Genera-Audio-Edge.ps1 -TestoFile '.	esto.txt' -Voce it-IT-ElsaNeural -Velocita '+0%' -CartellaOutput 'C:\percorso\audio'
```

Il Desktop effettivo viene rilevato se non si indica CartellaOutput. Ogni esecuzione crea una directory distinta. L'installazione delle skill non copia lo script facoltativo: nell'ambiente agente si possono usare i comandi autonomi del PROCEDURA.md.

## Comando unificato per le voci accertate

`Strumenti/Genera-Audio.ps1` seleziona motore e voce senza installare dipendenze. Nicola (predefinita), Sara e Paola sono offline; Diego, Giuseppe, Elsa e Isabella usano Edge TTS online. Il parametro `-VelocitaPercento` è -5 per impostazione predefinita, modificabile da -50 a +100. Gli effetti della velocità dipendono dal motore, non sono identici fra voci.

```powershell
.\Strumenti\Genera-Audio.ps1 -TestoFile '.\testo.txt' -Voce Nicola
.\Strumenti\Genera-Audio.ps1 -TestoFile '.\testo.txt' -Voce Sara -VelocitaPercento 0
.\Strumenti\Genera-Audio.ps1 -TestoFile '.\testo.txt' -Voce Paola
.\Strumenti\Genera-Audio.ps1 -TestoFile '.\testo.txt' -Voce Diego
```

Output MP3 e manifest in una directory nuova sul Desktop effettivo, oppure nella directory esistente indicata con `-CartellaOutput`. Per voci offline conserva anche il master WAV. Il comando usa `sintesi_audio_locale.py` per Piper/Kokoro e delega `Genera-Audio-Edge.ps1` per le voci online: mantenere questi file nella stessa cartella.

I percorsi locali predefiniti sono quelli verificati su questo PC: modelli Kokoro di AI Ebook to Audio Converter sul disco D: e Piper Paola nella cache Calibre. Su altri PC indicare `-RuntimeRoot`, `-KokoroModelli` e `-PiperModello`. Il runtime è l'ambiente separato predisposto nella sessione; non vengono eseguiti gli eseguibili dei programmi che ospitano i modelli. Il comando non costituisce un nuovo motore né modifica la disponibilità nel catalogo delle procedure.

Le skill da scegliere restano `sintesi-vocale-locale` per offline e `sintesi-vocale-edge-tts` per online; il comando comune è uno strumento facoltativo della copia sorgente. Una richiesta generica usa Nicola offline come predefinita nel comando. La decodifica riuscita richiede comunque ascolto per valutare pronuncia e fedeltà.
