# ARI-1809 — Pipeline multimediale automatizzata

- **Categoria:** Multimedia e applicazioni specialistiche
- **Livello:** L4 Professionale
- **Stato:** Bozza verificabile
- **Versione:** 0.1.0
- **Utilizzo offline:** Sì, con strumenti e modelli già disponibili localmente

## Scopo

Coordinare un flusso locale riprendibile con dipendenze esplicite e verifica prima della consegna.

## Campo di applicazione

Prompt → risorse → voce → montaggio → sottotitoli → verifica → esportazione; riusa ARI-1803…ARI-1808 per le fasi specialistiche.

## Quando usarla

Quando serve pipeline multimediale automatizzata e sono definiti sorgenti locali, profilo di consegna e criteri di accettazione. Applicare solo i rami necessari al risultato.

## Quando non usarla

- Mancano input, diritti d'uso, perimetro o criteri di accettazione.
- Serve un servizio cloud obbligatorio o un motore locale indisponibile senza alternativa concordata.
- Si pretende qualità percettiva o fedeltà semantica senza ascolto/revisione visiva.

## Prerequisiti

Python o PowerShell per orchestrazione e strumenti richiesti dalle fasi. Ogni ramo deve essere disponibile; fasi opzionali esplicite nel piano.

Confermare lettura delle sorgenti, scrittura in directory nuova, spazio libero, budget temporale e RAM/VRAM. Licenze di modelli, voci, font e risorse compatibili con l'uso previsto. Nessuna installazione implicita.

## Materiale necessario

- **Input:** Brief, risorse locali, profilo di consegna, configurazione delle fasi, directory nuova e checkpoint precedenti se disponibili.
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

1. Convertire brief in piano con input/output, dipendenze, timeout e accettazione. Prompt e risorse possono essere manuali: nessun LLM remoto obbligatorio.
2. Definire grafo: risorse → voce → montaggio → sottotitoli → verifica → esportazione. Immagini/video alimentano il montaggio; sottotitoli derivano da ARI-1806 o testo realmente allineato, senza timestamp inventati.
3. Directory nuova per run, con input/lavoro/output/log; non riusare output precedenti né alterare sorgenti.

### Manifest e checkpoint

Esempio di configurazione, non evidenza di esecuzione:

```json
{
  "schema_version": 1,
  "run_id": "esempio-non-eseguito",
  "profilo": {"fps": 25, "larghezza": 1280, "altezza": 720},
  "fasi": [
    {"id": "voce", "dipende_da": ["risorse"], "stato": "pianificata", "tentativi": 0}
  ]
}
```

Nel manifest reale registrare anche SHA-256 input/output, argomenti come array, versioni strumenti/modelli, parametri, seed, orari, exit code, log, controlli e percorso checkpoint. Stati: pianificata, in_esecuzione, fallita, verificata, saltata_con_motivazione.

### Generazione e orchestrazione

Implementare adattatore distinto per motore con interfaccia locale verificata. Python: `subprocess.run` con lista argomenti, timeout e senza `shell=True`. PowerShell: eseguibile/array argomenti e `$LASTEXITCODE` subito dopo il comando.

Algoritmo da implementare nel progetto bersaglio:

1. Validare grafo aciclico, input e strumenti prima di generare.
2. Se output previsto esiste, fermare o scegliere directory nuova; non sovrascrivere.
3. Eseguire fase solo con dipendenze verificate o saltate secondo ramo approvato.
4. Registrare exit code/log e validare artefatto prima di segnare fase verificata.
5. Scrivere ogni checkpoint in nuovo file completo UTF-8 con numero progressivo e hash; non modificare checkpoint validi. Selezionare ultimo checkpoint completo verificabile.
6. Su errore/timeout/cancellazione interrompere discendenti; non esportare parziali come definitivi.

### Ripresa e verifica

Validare schema checkpoint e ricalcolare hash input, parametri e versioni. Riusare output solo se firma della fase e controlli coincidono. Un cambiamento invalida fase e discendenti, da rigenerare in percorsi nuovi.

Fase rimasta in_esecuzione è incompleta: un file presente non prova successo. Retry con limite esplicito e nuovo output. Non eseguire comandi arbitrari da manifest non attendibili.

### Esportazione

Consegnare artefatti finali validati, sottotitoli e manifest senza segreti. Verificare pacchetto dopo copia e confrontare hash; preservare log/lavoro. Stato verificata di una fase non promuove la procedura ARI a Verificata.

## Controlli

Controllare dipendenze, hash, checkpoint completi, retry limitati e mancata esportazione su errore. Prima della produzione provare ripresa dopo interruzione e invalidazione per input cambiato su caso locale.

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

Riprendere per sola esistenza file; usare checkpoint incompleti; riusare output con parametri diversi; ignorare fasi fallite; confondere stato fase e promozione ARI.

Non presumere motori installati, inventare opzioni/API o scambiare conformità per prova operativa. Non usare output preesistenti come destinazioni.

## Rapporto finale

Riportare ID run, input/hash, strumenti/versioni, modelli/licenze, parametri, output/hash, exit code, misure, revisione percettiva e limiti. Distinguere progettato, eseguito e non verificato. Verdetto **Idoneo**, **Idoneo con vincoli**, **Non idoneo** o **Inconcludente** per il risultato; non assegnare **Verificata** alla procedura senza evidenze secondo VERIFICA.md.

## Condizioni di uscita

- **Completamento:** output presenti, controlli deterministici superati, revisione contenuto quando richiesta, esportazione verificata e rapporto disponibile.
- **Arresto:** strumento/modello assente, output esistente, input illeggibile, rete inattesa, memoria/spazio insufficiente, timeout, exit code non zero o controllo fallito. Conservare input/log; fermare consegna definitiva.
- **Limiti:** riproducibilità dipendente da versioni/hardware/parametri. Controlli tecnici non dimostrano qualità estetica o correttezza semantica. Fallback che cambia risultato richiede scelta esplicita.

## Cronologia delle versioni

- **0.1.0** — 2026-10-01 — Prima stesura locale, esempi da confermare nell'ambiente bersaglio; nessuna evidenza operativa aggiunta.
