# Arsenale IA

Biblioteca italiana di procedure operative per l'Intelligenza Artificiale.

## Obiettivo

Arsenale IA raccoglie procedure tecniche in italiano, riutilizzabili da persone, team e agenti IA.

## Principio guida

**Metodo prima dell'automazione.**

## Stato

La roadmap **v0.3 — Compatibilità** è completata:

- 19 procedure disponibili;
- 19 adattatori `SKILL.md`;
- supporto a Codex, Claude Code e client compatibili con Agent Skills;
- utilizzo locale senza dipendenza runtime da GitHub.

## Struttura

Ogni procedura disponibile vive in `Procedure/ARI-xxxx-.../` e contiene:

- `PROCEDURA.md` — metodo canonico e completo;
- `SKILL.md` — adattatore sintetico per agenti.

La cartella sorgente usa il codice ARI. Gli strumenti in `Strumenti/` installano ogni skill nella cartella runtime con il nome previsto dal relativo front matter.

## Uso locale

Le procedure possono essere lette e applicate direttamente dal filesystem: GitHub serve per distribuzione e versionamento, non è necessario durante l'esecuzione locale.

Per Codex, Claude Code, altri agenti e installazione offline vedere [`COMPATIBILITA.md`](COMPATIBILITA.md).

## Documenti principali

- [`STANDARD.md`](STANDARD.md) — regole comuni;
- [`CATALOGO.md`](CATALOGO.md) — procedure disponibili e pianificate;
- [`ROADMAP.md`](ROADMAP.md) — stato dello sviluppo;
- [`COMPATIBILITA.md`](COMPATIBILITA.md) — installazione e uso con gli agenti;
- [`CONTRIBUIRE.md`](CONTRIBUIRE.md) — regole per i contributi.
