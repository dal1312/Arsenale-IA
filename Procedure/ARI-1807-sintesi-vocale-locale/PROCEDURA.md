# ARI-1807 — Sintesi vocale locale

- **Categoria:** Multimedia e applicazioni specialistiche
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.1.0
- **Utilizzo offline:** Sì, con strumenti e modelli già disponibili localmente

## Scopo

Convertire testo in voce locale controllando pronuncia, ritmo, segmentazione e qualità.

## Campo di applicazione

TTS/voice-over con Piper, Kokoro o equivalenti presenti. Musica ed effetti appartengono ad ARI-1803; trascrizione ad ARI-1806.

## Quando usarla

Quando serve sintesi vocale locale e sono definiti sorgenti locali, profilo di consegna e criteri di accettazione. Applicare solo i rami necessari al risultato.

## Quando non usarla

- Mancano input, diritti d'uso, perimetro o criteri di accettazione.
- Serve un servizio cloud obbligatorio o un motore locale indisponibile senza alternativa concordata.
- Si pretende qualità percettiva o fedeltà semantica senza ascolto/revisione visiva.

## Prerequisiti

Motore TTS specifico, voce configurata e FFmpeg/FFprobe per misura e montaggio. Le distribuzioni Piper/Kokoro possono esporre interfacce differenti.

Confermare lettura delle sorgenti, scrittura in directory nuova, spazio libero, budget temporale e RAM/VRAM. Licenze di modelli, voci, font e risorse compatibili con l'uso previsto. Nessuna installazione implicita.

## Materiale necessario

- **Input:** Testo UTF-8, lingua, voce/modello locali, dizionario di pronuncia, velocità, pause e formato finale.
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

1. Identificare eseguibile/versione/help, modello e configurazione voce. Per Piper ONNX controllare anche configurazione associata richiesta dalla distribuzione.
2. Scegliere voce/lingua e verificare licenza, sample rate e limiti. Non promettere clonazione quando non è offerta dal motore.
3. Espandere numeri, sigle e abbreviazioni conservando originale e testo normalizzato; segmentare per frasi/paragrafi con ID stabili, senza superare i limiti.

### Generazione

Esempio per distribuzioni Piper con testo su stdin e opzioni `--model`/`--output_file`, da confermare con `piper --help`. Non è un comando Kokoro; non è stato provato su una voce in questa attività. Verificare che modello/configurazione siano locali e output assente: il motore può sovrascrivere.

PowerShell, singola frase di prova:

```powershell
$frase = 'Prova di sintesi vocale locale.'
$frase | piper --model "modelli/voce.onnx" --output_file "voce-prova.wav"
if ($LASTEXITCODE -ne 0) { throw 'Sintesi non riuscita' }
```

Linux/macOS:

```sh
printf '%s\n' 'Prova di sintesi vocale locale.' | piper --model "modelli/voce.onnx" --output_file "voce-prova.wav"
```

Per testi estesi usare input UTF-8 e un adattatore che invii byte UTF-8; la pipeline PowerShell 5.1 può usare altra codifica, da verificare prima della produzione. Non cambiare variabili di sistema globali.

Per Kokoro usare solo CLI/libreria realmente presente e documentata localmente: non presumere eseguibile `kokoro` o flag Piper. Se l'interfaccia manca, fermare il ramo.

Generare un campione, validare pronuncia e poi produrre segmenti numerati. Usare controllo velocità del motore se supportato oppure una trasformazione tracciata:

```text
ffmpeg -n -i "voce-prova.wav" -af "atempo=1.1" -c:a pcm_s16le "voce-veloce.wav"
```

### Verifica

Controllare completezza/ordine segmenti, troncamenti, silenzi, sample rate e clipping. Ascoltare testo completo quando serve fedeltà di lettura; approvare pronuncia/ritmo sul campione prima del batch.

### Esportazione

Concatenare segmenti con pause intenzionali tramite ARI-1805 e normalizzare tramite ARI-1803. Conservare testo, voce, parametri e manifest. Un controllo ASR aiuta a rilevare omissioni ma non sostituisce ascolto.

## Controlli

Verificare durata plausibile, segmenti completi, picchi e uniformità. Confermare pronuncia/ritmo e assenza di parole saltate tramite ascolto.

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

Presumere CLI Kokoro universale; inviare encoding errato; accelerare senza rivalutare intelligibilità; unire sample rate incompatibili.

Non presumere motori installati, inventare opzioni/API o scambiare conformità per prova operativa. Non usare output preesistenti come destinazioni.

## Rapporto finale

Riportare ID run, input/hash, strumenti/versioni, modelli/licenze, parametri, output/hash, exit code, misure, revisione percettiva e limiti. Distinguere progettato, eseguito e non verificato. Verdetto **Idoneo**, **Idoneo con vincoli**, **Non idoneo** o **Inconcludente** per il risultato; non assegnare **Verificata** alla procedura senza evidenze secondo VERIFICA.md.

## Condizioni di uscita

- **Completamento:** output presenti, controlli deterministici superati, revisione contenuto quando richiesta, esportazione verificata e rapporto disponibile.
- **Arresto:** strumento/modello assente, output esistente, input illeggibile, rete inattesa, memoria/spazio insufficiente, timeout, exit code non zero o controllo fallito. Conservare input/log; fermare consegna definitiva.
- **Limiti:** riproducibilità dipendente da versioni/hardware/parametri. Controlli tecnici non dimostrano qualità estetica o correttezza semantica. Fallback che cambia risultato richiede scelta esplicita.

## Cronologia delle versioni

- **0.1.0** — 2026-10-01 — Prima stesura locale, esempi da confermare nell'ambiente bersaglio; nessuna evidenza operativa aggiunta.
