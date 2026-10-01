# ARI-1810 — Sintesi vocale con Edge TTS

- **Categoria:** Multimedia e applicazioni specialistiche
- **Livello:** L3 Avanzato
- **Stato:** Bozza verificabile
- **Versione:** 0.1.0
- **Utilizzo offline:** No, la sintesi richiede il servizio online Microsoft Edge

## Scopo

Generare MP3 di parlato italiano da testo preservato, con voce selezionabile, output nuovi e verifica tecnica prima della consegna.

## Campo di applicazione

Narrazione, lettura di testi e voice-over online con Edge TTS. Le quattro voci ammesse sono Diego, Giuseppe Multilingual, Elsa e Isabella. Musica ed effetti seguono ARI-1803; sintesi offline con Piper, Kokoro o Windows segue ARI-1807. Il pacchetto Python locale non rende locale il motore: il testo viene trasmesso al servizio Microsoft Edge.

## Quando usarla

- L'utente richiede Edge TTS, una delle relative voci neurali italiane o esplicitamente voce online.
- Serve un MP3 da testo con impostazioni ripetibili e una connessione disponibile.
- Serve un campione vocale; scegliere un breve testo originale solo se l'utente lascia libera la scelta.

## Quando non usarla

- È richiesta elaborazione offline o il testo non deve essere inviato a servizi esterni.
- La richiesta riguarda musica, effetti o generazione video.
- Manca il testo e non è autorizzata la scelta di un campione.
- La voce non è disponibile, il servizio è irraggiungibile o sono richieste garanzie di disponibilità permanente.

## Prerequisiti

Python con pacchetto edge-tts già disponibile, connessione di rete, FFmpeg e FFprobe, directory output scrivibile. Non installare dipendenze come effetto implicito della sintesi. Su Windows verificare il launcher `py`; su Linux/macOS usare l'interprete effettivo, per esempio `python3`. L'interfaccia di riferimento è edge-tts 7.2.8, da confermare con help e versione locali.

L'utente deve sapere che la sintesi è online. Una richiesta esplicita di Edge TTS autorizza l'invio del testo necessario a quel lavoro; una richiesta ambigua con vincoli offline va chiarita prima dell'invio.

## Materiale necessario

- **Input:** testo originale o file UTF-8, senza correzioni editoriali implicite.
- **Voce:** `it-IT-DiegoNeural` predefinita; alternative `it-IT-GiuseppeMultilingualNeural`, `it-IT-ElsaNeural`, `it-IT-IsabellaNeural`.
- **Velocità:** `-5%` predefinita, modificabile su richiesta; registrare il valore effettivo.
- **Output:** MP3, log e manifest JSON con versione, voce, velocità, durata e hash input/output.
- **Destinazione:** Desktop effettivo per impostazione predefinita oppure directory indicata dall'utente. Per campioni da ascoltare nella chat è ammessa la directory artefatti della chat.

## Procedura operativa

### Rilevamento e progettazione

1. Riutilizzare testo e preferenze già presenti. Chiedere solo il testo mancante; non chiedere obbligatoriamente la voce quando può essere usata Diego.
2. Rilevare l'interprete e confermare `python -m edge_tts --help`, `--version`, `--list-voices` con l'interprete effettivo. Su Windows il comando corrispondente è `py -m edge_tts`.
3. Verificare che la voce scelta esista nel catalogo restituito dal servizio. Le caratteristiche timbriche vanno valutate tramite campioni, non dichiarate come garantite.
4. Rilevare FFmpeg/FFprobe e verificarne le versioni. Se il launcher non vede l'interprete nell'ambiente isolato, usare il percorso dell'interprete già installato senza modificare il sistema.
5. Definire destinazione, velocità, limite temporale e criterio di consegna. Per il Desktop Windows usare `[Environment]::GetFolderPath('Desktop')`; non presumere `$env:USERPROFILE\Desktop`, perché può essere reindirizzato.

### Generazione da UTF-8

Salvare il testo letterale in UTF-8 senza interpolarlo come codice PowerShell. Per testo già in un file, leggerlo senza riscriverlo. Lo script facoltativo `Strumenti/Genera-Audio-Edge.ps1` nel repository automatizza i controlli; l'adattatore installato resta autonomo grazie ai comandi seguenti.

Esempio PowerShell, dopo rilevamento positivo; sostituire il percorso input con quello reale e usare velocità/voce richieste:

```powershell
$inputFile = (Resolve-Path -LiteralPath '.\testo.txt').Path
$desktop = [Environment]::GetFolderPath('Desktop')
if (-not $desktop -or -not (Test-Path -LiteralPath $desktop -PathType Container)) {
    throw 'Desktop non disponibile: specificare una destinazione esistente'
}
$runDir = Join-Path $desktop ('audio-edge-' + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $runDir -ErrorAction Stop | Out-Null
$mp3 = Join-Path $runDir 'audio.mp3'
py -m edge_tts --voice it-IT-DiegoNeural --rate=-5% --file $inputFile --write-media $mp3
if ($LASTEXITCODE -ne 0) { throw 'Sintesi fallita: conservare il log e non consegnare il parziale' }
```

Linux/macOS, con interprete e strumenti rilevati e `testo.txt` UTF-8. La directory base è configurabile; non presumere un Desktop POSIX:

```sh
run_dir=$(mktemp -d ./audio-edge-XXXXXXXX) || exit 1
python3 -m edge_tts --voice it-IT-DiegoNeural --rate=-5% --file ./testo.txt --write-media "$run_dir/audio.mp3" || exit 1
ffprobe -v error -show_format -show_streams -of json "$run_dir/audio.mp3" || exit 1
ffmpeg -v error -xerror -i "$run_dir/audio.mp3" -map 0:a:0 -f null - || exit 1
```

Per testi lunghi Edge TTS segmenta internamente le richieste; non occorre inventare una soglia universale di caratteri né concatenare file manualmente. Il servizio ha limiti e può fallire: non promettere funzionamento per qualsiasi lunghezza. Per lavori estesi definire timeout e segmenti logici tracciati quando serve ripresa, preservando tutte le parole. Non cambiare il testo per aggirare errori. Ogni retry deve essere limitato e usare output nuovo.

### Verifica

Controllare exit code, file presente e dimensione positiva. Analizzare realmente il JSON di FFprobe: stream audio MP3, durata finita positiva, frequenza e canali. Eseguire la decodifica completa:

```powershell
ffprobe -v error -show_format -show_streams -of json $mp3
if ($LASTEXITCODE -ne 0) { throw 'Analisi MP3 fallita' }
ffmpeg -v error -xerror -i $mp3 -map 0:a:0 -f null -
if ($LASTEXITCODE -ne 0) { throw 'Decodifica MP3 fallita' }
Get-FileHash -Algorithm SHA256 -LiteralPath $inputFile
Get-FileHash -Algorithm SHA256 -LiteralPath $mp3
```

Conservare log e manifest UTF-8 con input/output hash, impostazioni e misure effettive. Ascoltare campioni a inizio/centro/fine e parti con nomi propri, numeri, sigle e accenti. Per fedeltà integrale richiesta, ascoltare il testo completo. Controllare pause, omissioni e troncamenti; la durata non dimostra fedeltà semantica.

### Esportazione e consegna

Consegnare solo il MP3 verificato. Specificare voce, velocità, durata e percorso effettivi; in chat mostrare l'audio con un riferimento assoluto al file locale. Conservare output precedenti e distinguere verifica tecnica da approvazione percettiva. Non modificare il testo per correggere pronuncia senza richiesta: proporre prima una variante esplicita.

## Controlli

- Voce reale presente nel catalogo e appartenente alle quattro ammesse.
- Input UTF-8 non vuoto, conservato senza riscrittura e con hash.
- Directory nuova, nessuna sovrascrittura di audio precedenti.
- Sintesi con exit code zero, MP3 positivo, durata valida e decodifica completa riuscita.
- Manifest coerente con file, voce e velocità effettive.
- Revisione percettiva dichiarata, controlli mancanti esplicitati.

## Errori frequenti

- Definire Edge TTS offline perché il pacchetto è installato sul PC.
- Inserire testo utente in una stringa di comando interpolata anziché usare un file UTF-8.
- Sovrascrivere sempre audio_generato.mp3 oppure presumere il percorso Desktop.
- Fissare la velocità senza rispettare preferenze o chiedere ripetutamente la voce.
- Garantire una specifica timbrica o il successo su qualsiasi testo.
- Consegnare un parziale dopo errore di rete o confondere decodifica e qualità della pronuncia.

## Rapporto finale

Riportare input/hash, versione Edge TTS, voce, velocità, dipendenza online, destinazione, durata, codec, hash output, log, controlli e limiti. Usare Idoneo, Idoneo con vincoli, Non idoneo o Inconcludente. Una prova tecnica interna non promuove la procedura a Verificata.

## Condizioni di uscita

- **Completamento:** MP3 verificato, manifest disponibile, percorso comunicato e campione ascoltabile consegnato.
- **Arresto:** requisito mancante, voce indisponibile, input vuoto/non UTF-8, timeout, errore rete/processo, file vuoto, durata invalida o decodifica fallita. Conservare log, non presentare parziali come definitivi e non reinstallare automaticamente.
- **Limiti:** servizio online soggetto a disponibilità e modifiche; controllo tecnico non garantisce correttezza di pronuncia. Nuovi tentativi solo entro il limite concordato, senza sovrascrivere output.

## Cronologia delle versioni

- **0.1.0** — 2026-10-01 — Prima procedura dedicata a Edge TTS, distinta dalla sintesi offline.
