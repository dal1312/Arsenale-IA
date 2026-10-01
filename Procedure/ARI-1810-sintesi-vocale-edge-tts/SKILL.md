---
name: sintesi-vocale-edge-tts
description: Genera voce italiana da testo tramite il servizio online Edge TTS con Diego, Giuseppe, Elsa o Isabella. Usa per richieste di Edge TTS, delle relative voci neurali, audio da testo o voice-over online. Per sintesi offline applica la procedura locale pertinente.
---

# Sintesi vocale con Edge TTS

Leggi e applica [PROCEDURA.md](PROCEDURA.md), fonte canonica nella stessa cartella.

- Dichiara che il testo viene inviato al servizio online di Microsoft Edge. Una richiesta esplicita di Edge TTS autorizza la sintesi richiesta; non aggiungere conferme ripetute. Se l'utente richiede offline, usa il metodo locale.
- Usa il testo già fornito senza riscriverlo. Chiedilo solo se manca e non è ricavabile dal contesto; se l'utente chiede un campione libero, puoi scegliere un breve testo di prova.
- Usa Diego e velocità -5% quando non sono specificate altre preferenze; consenti la scelta fra le quattro voci e una velocità diversa.
- Rileva interprete, pacchetto, voci disponibili e FFmpeg/FFprobe. Non reinstallare strumenti automaticamente.
- Leggi il testo da file UTF-8, crea output nuovi e controlla sintesi, MP3 e manifest prima della consegna.
- Mostra il campione nella chat per l'ascolto, specificando percorso, voce e durata; la decodifica non dimostra pronuncia corretta.
- La procedura è autonoma. Lo script facoltativo del repository è utilizzabile solo se effettivamente disponibile, non è un requisito dell'adattatore installato.
