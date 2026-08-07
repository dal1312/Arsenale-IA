# Contribuire ad Arsenale IA

Arsenale IA accetta contributi in italiano.

## Regole principali

- usare una terminologia tecnica chiara;
- evitare inglese non necessario;
- seguire `STANDARD.md`;
- non presentare ipotesi come fatti;
- includere esempi concreti;
- indicare limiti e condizioni di applicazione;
- aggiornare il catalogo quando si aggiunge una nuova procedura.

## Nuove procedure

Una procedura può essere marcata **Disponibile** solo se:

1. usa un codice ARI riservato nel catalogo;
2. contiene `PROCEDURA.md` conforme alle sezioni canoniche di `STANDARD.md`;
3. contiene `SKILL.md` con `name` e `description` validi;
4. usa una versione semantica e registra la cronologia;
5. supera i validatori locali.

Usare `Modelli/PROCEDURA-TEMPLATE.md` come base strutturale. Il template non sostituisce l'analisi del dominio specifico.

## Verifica locale

Windows:

```powershell
py Strumenti/verifica_procedure.py
py Strumenti/verifica_skills.py
```

Linux/macOS:

```bash
python3 Strumenti/verifica_procedure.py
python3 Strumenti/verifica_skills.py
```

## Struttura di una proposta

1. Scopo della modifica.
2. Problema risolto.
3. File interessati.
4. Verifiche eseguite.
5. Eventuali limiti.

## Revisione

Ogni contributo deve essere verificabile, coerente con il catalogo e comprensibile anche a chi non conosce l'inglese tecnico.

La conformità automatica dimostra solo la struttura minima. Lo stato **Verificata** richiede anche evidenze operative secondo la roadmap.
