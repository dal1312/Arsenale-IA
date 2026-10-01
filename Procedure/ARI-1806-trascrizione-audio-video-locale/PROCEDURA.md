# ARI-1806 — Trascrizione audio e video locale

- **Categoria:** Multimedia e applicazioni specialistiche
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.1.0
- **Utilizzo offline:** Sì, con strumenti e modelli già disponibili localmente

## Scopo

Trascrivere parlato locale con lingua e timestamp controllati, senza traduzione implicita.

## Campo di applicazione

Trascrizione audio/video, lingua esplicita/rilevata, diarizzazione opzionale e TXT/SRT/VTT/JSON.

## Quando usarla

Quando serve trascrizione audio e video locale e sono definiti sorgenti locali, profilo di consegna e criteri di accettazione. Applicare solo i rami necessari al risultato.

## Quando non usarla

- Mancano input, diritti d'uso, perimetro o criteri di accettazione.
- Serve un servizio cloud obbligatorio o un motore locale indisponibile senza alternativa concordata.
- Si pretende qualità percettiva o fedeltà semantica senza ascolto/revisione visiva.

## Prerequisiti

FFmpeg, FFprobe e specifica implementazione Whisper o equivalente già installata con modello locale. Diarizzazione richiede motore/modelli distinti.

Confermare lettura delle sorgenti, scrittura in directory nuova, spazio libero, budget temporale e RAM/VRAM. Licenze di modelli, voci, font e risorse compatibili con l'uso previsto. Nessuna installazione implicita.

## Materiale necessario

- **Input:** Media autorizzato, lingua attesa, modello locale, glossario, campione manuale e formati richiesti.
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

1. Identificare implementazione/versione: openai-whisper, whisper.cpp e faster-whisper hanno interfacce differenti. Registrare task, lingua, modello e hash.
2. Distinguere trascrizione e traduzione. Concordare granularità temporale e necessità di speaker ID; timestamp non implicano diarizzazione.
3. Preparare campione di riferimento manuale e soglia di errore. Conservare offset se il media è un estratto.

### Preparazione e generazione

```text
ffmpeg -n -i "intervista.mp4" -vn -ac 1 -ar 16000 -c:a pcm_s16le "parlato.wav"
```

Verificare `whisper --help`. Esempio esclusivo per CLI openai-whisper che supporta modello `.pt` per percorso, da confermare nella versione installata; non vale per whisper.cpp. Il file modello deve esistere e la directory output deve essere nuova:

```text
whisper "parlato.wav" --model "modelli/whisper-local.pt" --language Italian --task transcribe --output_format all --output_dir "trascrizione-nuova" --fp16 False
```

Non passare un nome modello che inneschi download. Se il motore tenta rete, arrestare. `--fp16 False` è una scelta per CPU; misurare tempi/memoria prima di grandi input. Per implementazioni diverse costruire il comando dal loro help locale.

Diarizzazione: registrare motore, speaker ID, intervalli e incertezze. Se indisponibile, consegnare senza interlocutori solo quando il requisito lo ammette; non inventare le attribuzioni.

### Verifica

TXT: UTF-8 e non vuoto quando è atteso parlato. JSON: parsing/schema del motore e segmenti ordinati con `0 <= start < end <= durata + tolleranza`. SRT: indici progressivi e virgola nei timestamp; VTT: intestazione WEBVTT e punto nei timestamp. Verificare sovrapposizioni e leggibilità secondo il profilo scelto.

Ascoltare campioni a inizio/centro/fine e segmenti con nomi, numeri, silenzi e cambi speaker. WER/CER richiedono riferimento manuale: dichiarare campione e normalizzazione. La validità sintattica non prova fedeltà al parlato.

### Esportazione

Conservare JSON originario; produrre TXT/SRT/VTT richiesti, convertendo dai segmenti validati quando il motore non li offre nativamente. Conservare lingua/offset e verificare sottotitoli sul media. Minimizzare dati personali nel rapporto.

## Controlli

Controllare schema, encoding, timestamp e corrispondenza dei testi fra formati. Registrare errori sul campione manuale e verificare speaker ID separatamente.

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

Scaricare modello per nome; usare flag di un’altra implementazione; scambiare timestamp per diarizzazione; presentare confidence come WER.

Non presumere motori installati, inventare opzioni/API o scambiare conformità per prova operativa. Non usare output preesistenti come destinazioni.

## Rapporto finale

Riportare ID run, input/hash, strumenti/versioni, modelli/licenze, parametri, output/hash, exit code, misure, revisione percettiva e limiti. Distinguere progettato, eseguito e non verificato. Verdetto **Idoneo**, **Idoneo con vincoli**, **Non idoneo** o **Inconcludente** per il risultato; non assegnare **Verificata** alla procedura senza evidenze secondo VERIFICA.md.

## Condizioni di uscita

- **Completamento:** output presenti, controlli deterministici superati, revisione contenuto quando richiesta, esportazione verificata e rapporto disponibile.
- **Arresto:** strumento/modello assente, output esistente, input illeggibile, rete inattesa, memoria/spazio insufficiente, timeout, exit code non zero o controllo fallito. Conservare input/log; fermare consegna definitiva.
- **Limiti:** riproducibilità dipendente da versioni/hardware/parametri. Controlli tecnici non dimostrano qualità estetica o correttezza semantica. Fallback che cambia risultato richiede scelta esplicita.

## Cronologia delle versioni

- **0.1.0** — 2026-10-01 — Prima stesura locale, esempi da confermare nell'ambiente bersaglio; nessuna evidenza operativa aggiunta.
