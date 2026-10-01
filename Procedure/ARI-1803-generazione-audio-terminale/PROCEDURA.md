# ARI-1803 — Generazione audio da terminale

- **Categoria:** Multimedia e applicazioni specialistiche
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.1.0
- **Utilizzo offline:** Sì, con strumenti e modelli già disponibili localmente

## Scopo

Produrre audio locale tracciabile da sintesi, risorse esistenti e trasformazioni CLI.

## Campo di applicazione

TTS tramite ARI-1807, musica ed effetti da risorse o motori locali, conversione, normalizzazione e metadati.

## Quando usarla

Quando serve generazione audio da terminale e sono definiti sorgenti locali, profilo di consegna e criteri di accettazione. Applicare solo i rami necessari al risultato.

## Quando non usarla

- Mancano input, diritti d'uso, perimetro o criteri di accettazione.
- Serve un servizio cloud obbligatorio o un motore locale indisponibile senza alternativa concordata.
- Si pretende qualità percettiva o fedeltà semantica senza ascolto/revisione visiva.

## Prerequisiti

FFmpeg e FFprobe; un motore locale già configurato solo se è richiesta sintesi IA musicale o vocale. Non esiste una CLI musicale universale.

Confermare lettura delle sorgenti, scrittura in directory nuova, spazio libero, budget temporale e RAM/VRAM. Licenze di modelli, voci, font e risorse compatibili con l'uso previsto. Nessuna installazione implicita.

## Materiale necessario

- **Input:** Brief, sorgenti con licenza, durata, eventuale testo/voce, frequenza audio, canali, target LUFS e true peak.
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

1. Selezionare il ramo: voce tramite ARI-1807, musica tramite motore locale documentato, effetti tramite sintesi o risorse esistenti, trasformazione di audio locale.
2. Definire formato master lossless, sample rate, canali, durata e profilo di consegna. Concordare loudness, picco e tolleranze: non esiste un valore universale.
3. Per musica IA registrare motore/versione, modello e hash, prompt, seed quando supportato e licenza. Se il motore manca, fermare quel ramo; un'alternativa locale richiede una scelta esplicita.

### Generazione

Effetto tonale di prova, non musica IA, e conversione lossless in file nuovi:

```text
ffmpeg -n -f lavfi -i "sine=frequency=440:sample_rate=48000:duration=2" -c:a pcm_s16le "effetto.wav"
ffmpeg -n -i "sorgente.wav" -ar 48000 -ac 2 -c:a flac "master.flac"
```

Per TTS applicare ARI-1807. Per musica/effetti IA costruire l'invocazione solo dall'help e dalla documentazione locali del motore; non ipotizzare flag o download.

### Verifica e normalizzazione

Misurare il master; il riepilogo loudnorm è scritto su stderr:

```text
ffmpeg -v info -i "master.flac" -af "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json" -f null -
```

Il profilo numerico è un esempio da concordare. Per due passaggi valorizzare nel secondo filtro `measured_I`, `measured_TP`, `measured_LRA`, `measured_thresh` e `offset` con le misure del primo passaggio sullo stesso input. Non copiare numeri da altri file. Rieseguire la misura sul risultato e confrontare con le tolleranze.

### Esportazione

Esempio di normalizzazione dinamica a un passaggio, distinto dal metodo a due passaggi:

```text
ffmpeg -n -i "master.flac" -af "loudnorm=I=-16:TP=-1.5:LRA=11" -ar 48000 -c:a pcm_s16le -metadata title="Titolo concordato" "audio-normalizzato.wav"
```

Rileggere i metadati effettivamente conservati dal container. Non inserire dati personali o percorsi privati superflui.

## Controlli

Misurare loudness/picchi finali, durata, sample rate e canali. Ascoltare inizio, fine e transizioni per rumore, clipping e silenzi inattesi.

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

Confondere un tono di prova con musica IA; normalizzare ripetutamente file lossy; presumere conservazione dei tag; valutare qualità con sola decodifica.

Non presumere motori installati, inventare opzioni/API o scambiare conformità per prova operativa. Non usare output preesistenti come destinazioni.

## Rapporto finale

Riportare ID run, input/hash, strumenti/versioni, modelli/licenze, parametri, output/hash, exit code, misure, revisione percettiva e limiti. Distinguere progettato, eseguito e non verificato. Verdetto **Idoneo**, **Idoneo con vincoli**, **Non idoneo** o **Inconcludente** per il risultato; non assegnare **Verificata** alla procedura senza evidenze secondo VERIFICA.md.

## Condizioni di uscita

- **Completamento:** output presenti, controlli deterministici superati, revisione contenuto quando richiesta, esportazione verificata e rapporto disponibile.
- **Arresto:** strumento/modello assente, output esistente, input illeggibile, rete inattesa, memoria/spazio insufficiente, timeout, exit code non zero o controllo fallito. Conservare input/log; fermare consegna definitiva.
- **Limiti:** riproducibilità dipendente da versioni/hardware/parametri. Controlli tecnici non dimostrano qualità estetica o correttezza semantica. Fallback che cambia risultato richiede scelta esplicita.

## Cronologia delle versioni

- **0.1.0** — 2026-10-01 — Prima stesura locale, esempi da confermare nell'ambiente bersaglio; nessuna evidenza operativa aggiunta.
