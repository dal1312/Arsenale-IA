# Arsenale IA

Biblioteca italiana di procedure operative per l'Intelligenza Artificiale.

## Obiettivo

Arsenale IA raccoglie procedure tecniche in italiano, riutilizzabili da persone, team e agenti IA.

## Principio guida

**Metodo prima dell'automazione.**

## Stato

- compatibilità Agent Skills v0.3 completata;
- standardizzazione v0.4 completata;
- verifica operativa v0.5 in corso;
- 20 procedure disponibili;
- 20/20 procedure con `PROCEDURA.md` conforme e `SKILL.md`;
- ARI-0001…ARI-0005 e ARI-0009 verificate con due prove operative ciascuna, inclusa una prova indipendente;
- piano operativo v0.5 disponibile in `Piani/VERIFICA-OPERATIVA-V0.5.md`;
- soglia minima delle promozioni verificata automaticamente;
- utilizzo locale senza dipendenza runtime da GitHub;
- CI Windows/Linux per procedure, adattatori, evidenze, promozioni, test dei validatori e installatori.

## Struttura

```text
Procedure/
  ARI-xxxx-Nome/
    PROCEDURA.md
    SKILL.md
Piani/
Verifiche/
  ARI-xxxx/
    VER-ARI-xxxx-AAAAMMGG-NN.md
Modelli/
Strumenti/
```

`PROCEDURA.md` è la fonte canonica. `SKILL.md` è l'adattatore per gli agenti compatibili. `VERIFICA.md` definisce le evidenze richieste per lo stato **Verificata**.

## Verifica locale

Windows:

```powershell
py Strumenti/verifica_procedure.py
py Strumenti/verifica_skills.py
py Strumenti/verifica_evidenze.py
py Strumenti/verifica_promozioni.py
py -m unittest Strumenti.test_verifica_evidenze Strumenti.test_verifica_promozioni
```

Linux/macOS:

```bash
python3 Strumenti/verifica_procedure.py
python3 Strumenti/verifica_skills.py
python3 Strumenti/verifica_evidenze.py
python3 Strumenti/verifica_promozioni.py
python3 -m unittest Strumenti.test_verifica_evidenze Strumenti.test_verifica_promozioni
```

Per installazione ed esempi con Codex, Claude Code e altri agenti vedere `COMPATIBILITA.md`.
