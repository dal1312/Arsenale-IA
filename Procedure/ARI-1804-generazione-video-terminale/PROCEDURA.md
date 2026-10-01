# ARI-1804 — Generazione video da terminale

- **Categoria:** Multimedia e applicazioni specialistiche
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.1.0
- **Utilizzo offline:** Sì, con strumenti e modelli già disponibili localmente

## Scopo

Costruire video deterministici da immagini, testo, audio e frame tramite CLI locali.

## Campo di applicazione

Slideshow, titoli rasterizzati, visualizzazioni audio e sequenze numerate. La generazione semantica testo-video mediante modelli appartiene ad ARI-1808.

## Quando usarla

Quando serve generazione video da terminale e sono definiti sorgenti locali, profilo di consegna e criteri di accettazione. Applicare solo i rami necessari al risultato.

## Quando non usarla

- Mancano input, diritti d'uso, perimetro o criteri di accettazione.
- Serve un servizio cloud obbligatorio o un motore locale indisponibile senza alternativa concordata.
- Si pretende qualità percettiva o fedeltà semantica senza ascolto/revisione visiva.

## Prerequisiti

FFmpeg, FFprobe ed encoder/filtri richiesti; per testo verificare drawtext e font locale oppure usare titoli già renderizzati.

Confermare lettura delle sorgenti, scrittura in directory nuova, spazio libero, budget temporale e RAM/VRAM. Licenze di modelli, voci, font e risorse compatibili con l'uso previsto. Nessuna installazione implicita.

## Materiale necessario

- **Input:** Storyboard, immagini/frame numerati, testo UTF-8, font con licenza, eventuale audio, codec, risoluzione, FPS e durata.
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

1. Definire risoluzione, aspect ratio, FPS costante/variabile, durata e codec. Il profilo di esempio è H.264, 1280x720, 25 FPS, yuv420p.
2. Scegliere input e padding/crop senza deformare implicitamente immagini. Per sequenze controllare indice iniziale, buchi, dimensioni e durata = numero frame / FPS.
3. Per testo usare tavole raster locali quando manca il filtro/font; i percorsi drawtext richiedono escaping specifico del sistema. Il testo non genera scene semantiche senza un modello IA.

### Generazione

```text
ffmpeg -n -loop 1 -i "immagine.png" -i "voce.wav" -t 10 -vf "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2,setsar=1" -r 25 -c:v libx264 -pix_fmt yuv420p -c:a aac -shortest "immagine-con-voce.mp4"
ffmpeg -n -framerate 25 -start_number 1 -i "frame-%06d.png" -c:v libx264 -pix_fmt yuv420p "sequenza.mp4"
ffmpeg -n -i "audio.wav" -filter_complex "[0:a]showwaves=s=1280x720:mode=line:rate=25[v]" -map "[v]" -map 0:a -c:v libx264 -pix_fmt yuv420p -c:a aac "onda-audio.mp4"
```

Nel primo esempio `-t 10` e `-shortest` limitano la durata: decidere cosa fare quando l'audio è più corto. Per slideshow multipli usare il montaggio di ARI-1805. Prima delle opzioni verificare filtri showwaves ed encoder libx264 della build locale.

### Verifica

Controllare FPS razionale, conteggio frame, durata, aspect ratio e dimensioni. Ispezionare primo, ultimo e frame intermedi; verificare titoli leggibili e immagini non tagliate. Concordare tolleranza temporale, ad esempio un frame quando appropriato.

### Esportazione

Se richiesto per consegna web, creare un file nuovo con indice MP4 anticipato:

```text
ffmpeg -n -i "sequenza.mp4" -c copy -movflags +faststart "consegna.mp4"
```

Verificare l'artefatto di consegna, oltre al master.

## Controlli

Verificare stream audio presente o assente intenzionalmente, pixel format, FPS, frame e durata attesi. Leggibilità e adeguatezza visiva richiedono revisione umana.

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

Confondere framerate di input e FPS di output; ignorare buchi nei frame; stirare immagini; promettere video IA con filtri deterministici.

Non presumere motori installati, inventare opzioni/API o scambiare conformità per prova operativa. Non usare output preesistenti come destinazioni.

## Rapporto finale

Riportare ID run, input/hash, strumenti/versioni, modelli/licenze, parametri, output/hash, exit code, misure, revisione percettiva e limiti. Distinguere progettato, eseguito e non verificato. Verdetto **Idoneo**, **Idoneo con vincoli**, **Non idoneo** o **Inconcludente** per il risultato; non assegnare **Verificata** alla procedura senza evidenze secondo VERIFICA.md.

## Condizioni di uscita

- **Completamento:** output presenti, controlli deterministici superati, revisione contenuto quando richiesta, esportazione verificata e rapporto disponibile.
- **Arresto:** strumento/modello assente, output esistente, input illeggibile, rete inattesa, memoria/spazio insufficiente, timeout, exit code non zero o controllo fallito. Conservare input/log; fermare consegna definitiva.
- **Limiti:** riproducibilità dipendente da versioni/hardware/parametri. Controlli tecnici non dimostrano qualità estetica o correttezza semantica. Fallback che cambia risultato richiede scelta esplicita.

## Cronologia delle versioni

- **0.1.0** — 2026-10-01 — Prima stesura locale, esempi da confermare nell'ambiente bersaglio; nessuna evidenza operativa aggiunta.
