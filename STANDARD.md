# Standard Arsenale IA

## Scopo

Questo documento definisce le regole comuni per tutte le Procedure Arsenale IA.

## Principi

1. Comprendere prima di intervenire.
2. Basarsi su evidenze verificabili.
3. Separare analisi, pianificazione ed esecuzione.
4. Produrre risultati ripetibili.
5. Documentare limiti, rischi e verifiche.

## Struttura obbligatoria di una procedura

Ogni procedura deve contenere:

- codice e titolo;
- scopo;
- campo di applicazione;
- quando usarla;
- quando non usarla;
- prerequisiti;
- materiale necessario;
- procedura operativa;
- controlli;
- errori frequenti;
- rapporto finale;
- condizioni di uscita;
- cronologia delle versioni.

## Codifica

Formato ufficiale:

`ARI-0001`

Il codice resta permanente anche quando cambia il titolo.

## Livelli

- L1 Base
- L2 Intermedio
- L3 Avanzato
- L4 Professionale
- L5 Audit

## Stati

- Bozza
- In revisione
- Verificata
- Pubblicata
- Obsoleta

## Compatibilità con agenti

Ogni procedura marcata **Disponibile** in `CATALOGO.md` deve contenere, nella propria cartella sorgente:

- `PROCEDURA.md` — fonte canonica del metodo;
- `SKILL.md` — adattatore sintetico per agenti compatibili con Agent Skills.

`SKILL.md` deve:

1. usare front matter YAML con almeno `name` e `description`;
2. usare un `name` univoco, minuscolo e separato da trattini;
3. spiegare nella `description` cosa fa la skill e quando deve essere usata;
4. rinviare a `PROCEDURA.md` con un percorso relativo;
5. contenere solo le regole operative essenziali necessarie all'attivazione;
6. non duplicare integralmente la procedura;
7. non introdurre regole in conflitto con `PROCEDURA.md`.

La cartella sorgente conserva il codice `ARI-xxxx` per catalogazione e manutenzione. Per l'uso con un client Agent Skills, l'adattatore viene materializzato in una cartella runtime il cui nome coincide con il campo `name`, insieme al relativo `PROCEDURA.md`.

## Portabilità locale

- Le procedure devono restare utilizzabili direttamente dal filesystem.
- GitHub e la rete non devono essere prerequisiti per caricare o applicare una procedura già presente localmente.
- Eventuali accessi a rete, build, test o strumenti esterni dipendono dalla singola procedura, non dal formato Arsenale IA.
- Percorsi e comandi specifici dei client sono documentati in `COMPATIBILITA.md`, non duplicati nelle procedure canoniche.
- Gli adattatori devono poter essere installati o esportati con gli strumenti locali presenti in `Strumenti/`.

## Regola fondamentale

**Metodo prima dell'automazione.**
