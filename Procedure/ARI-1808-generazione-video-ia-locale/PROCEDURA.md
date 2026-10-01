# ARI-1808 — Generazione video IA locale

- **Categoria:** Multimedia e applicazioni specialistiche
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.1.0
- **Utilizzo offline:** Sì, con strumenti e modelli già disponibili localmente

## Scopo

Orchestrare inferenza video IA locale con configurazioni, risorse e risultati tracciabili.

## Campo di applicazione

Motori text-to-video/image-to-video già configurati, inclusi workflow ComfyUI locali. Composizione deterministica e slideshow appartengono ad ARI-1804.

## Quando usarla

Quando serve generazione video ia locale e sono definiti sorgenti locali, profilo di consegna e criteri di accettazione. Applicare solo i rami necessari al risultato.

## Quando non usarla

- Mancano input, diritti d'uso, perimetro o criteri di accettazione.
- Serve un servizio cloud obbligatorio o un motore locale indisponibile senza alternativa concordata.
- Si pretende qualità percettiva o fedeltà semantica senza ascolto/revisione visiva.

## Prerequisiti

Motore installato, modelli completi e servizio già avviato quando necessario; hardware/backend compatibili. Nessun avvio o download implicito.

Confermare lettura delle sorgenti, scrittura in directory nuova, spazio libero, budget temporale e RAM/VRAM. Licenze di modelli, voci, font e risorse compatibili con l'uso previsto. Nessuna installazione implicita.

## Materiale necessario

- **Input:** Prompt, immagine iniziale opzionale, workflow API, modelli/checkpoint, seed, budget RAM/VRAM/disco, profilo e timeout.
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

1. Inventariare motore/backend/driver, modelli, VAE, encoder e nodi custom; registrare versioni, hash e compatibilità. Checkpoint del modello e checkpoint di esecuzione sono distinti.
2. Definire risoluzione, frame, FPS, passi, sampler e seed solo se supportati. Il budget include attivazioni/offload; partire da una prova ridotta concordata.
3. Selezionare CLI verificata con help o API documentata su loopback. Non inventare un comando generico `comfyui generate`.

### Rilevamento e generazione

Servizio già presente all'indirizzo concordato. Esempio di sola lettura per famiglia API ComfyUI convenzionale, da confermare nella documentazione locale della versione:

```powershell
Invoke-RestMethod -Uri 'http://127.0.0.1:8188/system_stats' -Method Get -TimeoutSec 10
```

Linux/macOS, se curl esiste:

```sh
curl --fail --max-time 10 'http://127.0.0.1:8188/system_stats'
```

Raggiungibilità non prova disponibilità dei nodi video. Usare workflow esportato in formato API, verificare classi/input e respingere nodi che scaricano modelli o contattano servizi esterni.

Contratto di orchestrazione, non invocazione universale:

- preparare richiesta con workflow API e parametri realmente supportati;
- per ComfyUI convenzionale verificato localmente, inviare JSON con campo `prompt` a `/prompt` e conservare `prompt_id`;
- leggere `/history/{prompt_id}` dove supportato, distinguendo attesa, successo ed errore secondo schema effettivo;
- imporre timeout e limite di tentativi; registrare risposte e output senza scambiare preview per video finale;
- risolvere percorsi soltanto nelle directory output autorizzate.

Questi endpoint non sono stati verificati su un'istanza in questa attività. Documentare ogni adattamento di schema/workflow prima dell'invio; se non verificabile, fermare.

### Memoria, fallback e verifica

Su OOM conservare log/parametri e fermare il job. Non ripeterlo indefinitamente: proporre minore risoluzione/frame, batch ridotto, offload supportato o modello già disponibile. Registrare cambiamenti e relativo impatto.

Motore assente: dichiarare generazione non eseguita. Fallback deterministico ARI-1804 solo con accettazione del risultato diverso, senza chiamarlo generazione IA. Seed identico non garantisce identità bit-a-bit fra backend/hardware.

### Esportazione

Controllare frame e video con FFprobe/decodifica. Se il motore restituisce frame, assemblare con ARI-1804 mantenendo ordine/FPS. Conservare workflow, hash modelli, parametri, job ID e log; distinguere preview e master.

## Controlli

Verificare stato terminale reale, frame attesi, codec/durata e output non vuoti. Revisionare flicker, deformazioni, coerenza temporale e aderenza al prompt: non sono misurati dalla sola decodifica.

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

Scaricare checkpoint automaticamente; esporre API su rete senza necessità; attribuire riproducibilità assoluta al seed; ignorare nodi custom e output preview.

Non presumere motori installati, inventare opzioni/API o scambiare conformità per prova operativa. Non usare output preesistenti come destinazioni.

## Rapporto finale

Riportare ID run, input/hash, strumenti/versioni, modelli/licenze, parametri, output/hash, exit code, misure, revisione percettiva e limiti. Distinguere progettato, eseguito e non verificato. Verdetto **Idoneo**, **Idoneo con vincoli**, **Non idoneo** o **Inconcludente** per il risultato; non assegnare **Verificata** alla procedura senza evidenze secondo VERIFICA.md.

## Condizioni di uscita

- **Completamento:** output presenti, controlli deterministici superati, revisione contenuto quando richiesta, esportazione verificata e rapporto disponibile.
- **Arresto:** strumento/modello assente, output esistente, input illeggibile, rete inattesa, memoria/spazio insufficiente, timeout, exit code non zero o controllo fallito. Conservare input/log; fermare consegna definitiva.
- **Limiti:** riproducibilità dipendente da versioni/hardware/parametri. Controlli tecnici non dimostrano qualità estetica o correttezza semantica. Fallback che cambia risultato richiede scelta esplicita.

## Cronologia delle versioni

- **0.1.0** — 2026-10-01 — Prima stesura locale, esempi da confermare nell'ambiente bersaglio; nessuna evidenza operativa aggiunta.
