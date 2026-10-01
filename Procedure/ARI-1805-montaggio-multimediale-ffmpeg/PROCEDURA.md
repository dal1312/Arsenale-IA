# ARI-1805 — Montaggio multimediale con FFmpeg

- **Categoria:** Multimedia e applicazioni specialistiche
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.1.0
- **Utilizzo offline:** Sì, con strumenti e modelli già disponibili localmente

## Scopo

Montare media locali con timeline esplicita e controllo qualità ripetibile.

## Campo di applicazione

Taglio, concatenazione, transcodifica, filtri, sottotitoli esterni/muxati/impressi e sincronizzazione audio/video.

## Quando usarla

Quando serve montaggio multimediale con ffmpeg e sono definiti sorgenti locali, profilo di consegna e criteri di accettazione. Applicare solo i rami necessari al risultato.

## Quando non usarla

- Mancano input, diritti d'uso, perimetro o criteri di accettazione.
- Serve un servizio cloud obbligatorio o un motore locale indisponibile senza alternativa concordata.
- Si pretende qualità percettiva o fedeltà semantica senza ascolto/revisione visiva.

## Prerequisiti

FFmpeg e FFprobe; libx264 se selezionato e libass per filtro subtitles. Verificare capacità reali della build.

Confermare lettura delle sorgenti, scrittura in directory nuova, spazio libero, budget temporale e RAM/VRAM. Licenze di modelli, voci, font e risorse compatibili con l'uso previsto. Nessuna installazione implicita.

## Materiale necessario

- **Input:** Sorgenti, timeline con timecode e unità, tracce audio, sottotitoli, profilo codec e tolleranze.
- **Configurazione:** versioni strumenti, percorsi modelli, parametri e tolleranze.
- **Output:** artefatti del ramo selezionato, manifest con hash/parametri, log e rapporto controlli.
- **Tracciabilità:** ID run, origine/licenze risorse e decisioni sul risultato.

## Procedura operativa

### Rilevamento degli strumenti

Rilevare soltanto gli strumenti richiesti dal ramo selezionato, registrando percorso, versione, capacità e modelli presenti. Non installare strumenti, scaricare modelli, avviare servizi o modificare configurazioni di sistema implicitamente. Se manca un requisito, documentare il prerequisito e istruzioni separate per una futura installazione autorizzata.

PowerShell:

```powershell
Get-Command ffmpeg, ffprobe -ErrorAction SilentlyContinue | Select-Object Name, Source
# Eseguire solo dopo averne confermato la presenza:
ffmpeg -version
ffprobe -version
ffmpeg -encoders
ffmpeg -filters
```

Linux/macOS:

```sh
command -v ffmpeg
command -v ffprobe
# Eseguire solo se i controlli precedenti hanno avuto successo:
ffmpeg -version
ffprobe -version
ffmpeg -encoders
ffmpeg -filters
```

Per ogni altro motore usare rilevamento equivalente e help locale. Non trasferire flag tra implementazioni differenti. Gli esempi FFmpeg usano opzioni della famiglia 6/7 da confermare nella build disponibile; gli altri esempi identificano la specifica interfaccia. Non è stata eseguita generazione multimediale nella stesura di questa procedura né consultata documentazione remota.

Operare in una directory di esecuzione nuova, con sorgenti locali. Verificare prima che ogni output sia assente; FFmpeg usa `-n` per impedirne la sovrascrittura, mai `-y`. I comandi FFmpeg su una riga sono utilizzabili sia in PowerShell sia in shell POSIX, dopo verifica di percorsi, filtri ed encoder. Controllare immediatamente exit code e stderr: in PowerShell `$LASTEXITCODE`, in shell POSIX lo stato del comando. Fermare le fasi dipendenti su errore.

### Progettazione

1. Inventariare codec, stream, timebase, start time, FPS, sample rate e canali di tutte le sorgenti.
2. Definire tagli/ordine: stream copy non garantisce precisione fuori dai keyframe; per tagli precisi prevedere ricodifica.
3. Scegliere sottotitoli separati, muxati o impressi. Stabilire lingua, ordine tracce e tolleranza del sincronismo.

### Generazione e montaggio

Taglio ricodificato e ridimensionamento in file nuovi:

```text
ffmpeg -n -ss 2 -i "sorgente.mp4" -t 5 -map 0:v:0 -map "0:a:0?" -c:v libx264 -c:a aac "taglio.mp4"
ffmpeg -n -i "sorgente.mp4" -vf "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2,setsar=1" -c:v libx264 -pix_fmt yuv420p -c:a aac "ridimensionato.mp4"
```

Per concat demuxer creare `concat.txt` UTF-8 con righe `file 'clip-01.mp4'` e `file 'clip-02.mp4'` e nomi relativi semplici. Codec, parametri e timebase devono essere compatibili. Altrimenti normalizzare in nuovi file o progettare il filtro concat con ricodifica.

```text
ffmpeg -n -f concat -safe 1 -i "concat.txt" -c copy "unito.mp4"
ffmpeg -n -i "unito.mp4" -i "testo.srt" -map 0:v:0 -map "0:a:0?" -map 1:0 -c:v copy -c:a copy -c:s mov_text "con-sottotitoli.mp4"
ffmpeg -n -i "unito.mp4" -vf "subtitles=testo.srt" -c:v libx264 -c:a copy "sottotitoli-impressi.mp4"
```

Per ritardare audio separato di 0,25 secondi, concordare il segno dello scarto:

```text
ffmpeg -n -i "video.mp4" -itsoffset 0.25 -i "audio.wav" -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -shortest "sincronizzato.mp4"
```

Se la deriva cresce nel tempo, un offset fisso non basta: controllare clock, campionamento e timebase. Non correggere con tentativi senza misura.

### Verifica

Decodificare integralmente e verificare timestamp/continuità delle giunzioni. Misurare sincro a inizio, centro e fine con riferimenti osservabili. Controllare sottotitoli e tracce su un player destinatario.

### Esportazione

Usare nuovo nome e codec/container concordati; un'uscita `-c copy` può conservare difetti della sorgente. Controllare il file finale completo.

## Controlli

Misurare durata dei tagli/totale e scarto audio-video entro tolleranza. Verificare timestamp monotoni, sottotitoli entro durata e tracce mappate. Ascoltare e osservare tutte le giunzioni.

### Verifica deterministica comune

Verificare presenza, dimensione positiva, hash SHA-256 e metadati rispetto al profilo concordato. Sostituire `artefatto.mp4` con il percorso effettivo, anche audio:

```text
ffprobe -v error -show_format -show_streams -of json "artefatto.mp4"
ffmpeg -v error -xerror -i "artefatto.mp4" -map "0:v?" -map "0:a?" -f null -
```

Analizzare il JSON: stream attesi, codec, durata finita positiva e parametri pertinenti (risoluzione, frequenza audio, canali). Per video, quando richiesto, leggere il conteggio effettivo:

```text
ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames,avg_frame_rate,width,height -of json "artefatto.mp4"
```

Definire le tolleranze prima della misura; gli stream opzionali nell'esempio di decodifica non sostituiscono il controllo degli stream obbligatori. La decodifica riuscita non dimostra fedeltà semantica o qualità percettiva.

Hash PowerShell: `Get-FileHash -Algorithm SHA256 -LiteralPath "artefatto.mp4"`. Linux: `sha256sum "artefatto.mp4"`; macOS: `shasum -a 256 "artefatto.mp4"`, dopo rilevamento del comando. Per testi e manifest controllare UTF-8, schema e timestamp. Documentare campioni ascoltati o visionati e verifiche non eseguibili.

## Errori frequenti

Concatenare file incompatibili; pretendere taglio al frame con stream copy; invertire offset; perdere tracce per mapping implicito.

Non presumere motori installati, inventare opzioni/API o scambiare conformità per prova operativa. Non usare output preesistenti come destinazioni.

## Rapporto finale

Riportare ID run, input/hash, strumenti/versioni, modelli/licenze, parametri, output/hash, exit code, misure, revisione percettiva e limiti. Distinguere progettato, eseguito e non verificato. Verdetto **Idoneo**, **Idoneo con vincoli**, **Non idoneo** o **Inconcludente** per il risultato; non assegnare **Verificata** alla procedura senza evidenze secondo VERIFICA.md.

## Condizioni di uscita

- **Completamento:** output presenti, controlli deterministici superati, revisione contenuto quando richiesta, esportazione verificata e rapporto disponibile.
- **Arresto:** strumento/modello assente, output esistente, input illeggibile, rete inattesa, memoria/spazio insufficiente, timeout, exit code non zero o controllo fallito. Conservare input/log; fermare consegna definitiva.
- **Limiti:** riproducibilità dipendente da versioni/hardware/parametri. Controlli tecnici non dimostrano qualità estetica o correttezza semantica. Fallback che cambia risultato richiede scelta esplicita.

## Cronologia delle versioni

- **0.1.0** — 2026-10-01 — Prima stesura locale, esempi da confermare nell'ambiente bersaglio; nessuna evidenza operativa aggiunta.
