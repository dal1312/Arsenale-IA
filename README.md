# Arsenale IA

Biblioteca italiana di procedure operative per l'Intelligenza Artificiale.

## Obiettivo

Arsenale IA raccoglie procedure tecniche in italiano, riutilizzabili da persone, team e agenti IA.

## Principio guida

**Metodo prima dell'automazione.**

## Stato

- compatibilità Agent Skills v0.3 completata;
- standardizzazione v0.4 completata;
- 19 procedure disponibili;
- 19/19 procedure con `PROCEDURA.md` conforme e `SKILL.md`;
- utilizzo locale senza dipendenza runtime da GitHub;
- CI Windows/Linux per procedure, adattatori e installatori.

La fase successiva è la verifica operativa v0.5 su progetti reali prima della promozione delle procedure allo stato **Verificata**.

## Struttura

```text
Procedure/
  ARI-xxxx-Nome/
    PROCEDURA.md
    SKILL.md
Modelli/
Strumenti/
```

`PROCEDURA.md` è la fonte canonica. `SKILL.md` è l'adattatore per gli agenti compatibili.

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

Per installazione ed esempi con Codex, Claude Code e altri agenti vedere `COMPATIBILITA.md`.
