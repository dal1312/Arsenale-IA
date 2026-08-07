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

Ogni `PROCEDURA.md` disponibile deve iniziare con un titolo H1 nel formato:

`# ARI-0001 — Titolo`

Subito dopo il titolo deve dichiarare almeno:

- **Categoria**;
- **Livello**;
- **Stato**;
- **Versione** in formato semantico `X.Y.Z`;
- **Utilizzo offline**.

Le sezioni canoniche obbligatorie, in questo ordine, sono:

1. `## Scopo`
2. `## Campo di applicazione`
3. `## Quando usarla`
4. `## Quando non usarla`
5. `## Prerequisiti`
6. `## Materiale necessario`
7. `## Procedura operativa`
8. `## Controlli`
9. `## Errori frequenti`
10. `## Rapporto finale`
11. `## Condizioni di uscita`
12. `## Cronologia delle versioni`

Ogni sezione deve contenere informazioni concrete. Sono ammesse sottosezioni aggiuntive, ma non devono sostituire le sezioni canoniche né modificarne il significato.

## Codifica

Formato ufficiale:

`ARI-0001`

Il codice resta permanente anche quando cambia il titolo. Il codice nel titolo deve coincidere con il prefisso della cartella della procedura.

## Versionamento delle procedure

- `PATCH` — correzioni editoriali, cambi di stato o registrazione di evidenze senza variazioni operative;
- `MINOR` — miglioramenti compatibili del metodo, nuovi controlli o maggiore precisione;
- `MAJOR` — modifica incompatibile del metodo o delle condizioni operative.

La versione corrente deve essere registrata anche nella cronologia del documento.

## Livelli

- L1 Base
- L2 Intermedio
- L3 Avanzato
- L4 Professionale
- L5 Audit

## Stati

- Bozza
- Bozza verificabile
- In revisione
- Verificata
- Pubblicata
- Obsoleta

Lo stato **Verificata** richiede evidenze di applicazione operativa; la sola conformità strutturale non è sufficiente. I criteri, il formato dei rapporti e la soglia minima sono definiti in `VERIFICA.md`.

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

## Validazione automatica

Prima di integrare modifiche eseguire:

```text
py Strumenti/verifica_procedure.py
py Strumenti/verifica_skills.py
py Strumenti/verifica_evidenze.py
```

Su Linux/macOS usare `python3` al posto di `py`.

I controlli automatici verificano struttura e coerenza minima. Non sostituiscono le prove operative su progetti reali descritte in `VERIFICA.md`.

## Regola fondamentale

**Metodo prima dell'automazione.**
