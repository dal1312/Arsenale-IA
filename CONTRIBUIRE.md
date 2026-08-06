# Contribuire ad Arsenale IA

Arsenale IA accetta contributi in italiano.

## Regole principali

- usare una terminologia tecnica chiara;
- evitare inglese non necessario;
- seguire `STANDARD.md`;
- non presentare ipotesi come fatti;
- includere esempi concreti;
- indicare limiti e condizioni di applicazione;
- aggiornare il catalogo quando si aggiunge una nuova procedura;
- aggiungere o aggiornare `SKILL.md` quando una procedura diventa **Disponibile**;
- mantenere l'utilizzo locale senza dipendenza runtime obbligatoria da GitHub.

## Requisiti dell'adattatore

Per ogni procedura disponibile:

1. `PROCEDURA.md` resta la fonte canonica;
2. `SKILL.md` usa almeno `name` e `description` nel front matter;
3. `name` è univoco, minuscolo e separato da trattini;
4. `description` indica cosa fa la skill e quando usarla;
5. il corpo rinvia a `PROCEDURA.md` e non la duplica;
6. le regole dell'adattatore non contraddicono la procedura.

Prima di proporre la modifica eseguire:

```powershell
py Strumenti/verifica_skills.py
```

Su Linux/macOS è equivalente:

```bash
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
