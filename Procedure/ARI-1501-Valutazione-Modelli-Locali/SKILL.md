---
name: valutazione-modelli-locali
description: Valuta modelli IA locali con evidenze verificabili. Per richieste sul modello attualmente usato/caricato, identifica prima processo server, listener e command line reale, poi ispeziona il GGUF passato al processo; non usare BAT, filename o configurazioni storiche come prova del runtime attivo.
---

# Valutazione modelli locali

Segui integralmente `PROCEDURA.md` nella stessa cartella, fonte canonica del metodo.

## Vincoli di attivazione

- Per “modello attivo/attualmente usato/caricato”, applica la catena obbligatoria della procedura: processo → listener associato al PID → command line completa → GGUF indicato da `-m` → metadata GGUF → provider/client → hardware → benchmark esistenti.
- Non scegliere un BAT o launcher trovato sul disco come runtime attivo senza prova che sia collegato al processo corrente. Non fermarti al filename; se un livello non è verificabile, dichiaralo **NON VERIFICATO** e non sostituirlo con ipotesi.
- Classifica le affermazioni come **OSSERVATO**, **DERIVATO**, **NON VERIFICATO** o **STIMA** (solo se richiesta). Cita la fonte.
- Per GGUF distingui `general.file_type` dai tensor types effettivi e controlla i metadata architetturali, MoE, tokenizer, chat template e provenienza disponibili. Non interpretare sigle del filename come specifiche.
- In llama.cpp `-ngl` è richiesta di offload; `-np` indica parallel sequences/slots, non thread CPU. `-fa on` non prova Vulkan: verifica il backend separatamente.
- Distingui GPU discreta e iGPU/UMA; non usare strumenti NVIDIA senza hardware NVIDIA verificato. Non dedurre tool calling dal solo provider.
- Riporta solo benchmark documentati, separando PP da TG. Se non disponibili, scrivi **non misurato**; non inventare prestazioni o latenze.
