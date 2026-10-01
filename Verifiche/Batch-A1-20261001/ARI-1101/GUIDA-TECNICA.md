# Documentazione tecnica: verifica_evidenze.py

Destinatario: manutentore dei rapporti operativi. Fonte: Strumenti/verifica_evidenze.py, sola lettura.

## Flusso

metadata estrae campi Markdown; section_body delimita sezioni; declared_versions_from_text legge la cronologia; placeholder_hits rileva marcatori incompleti; validate_reports controlla metadati, sezioni, identificativi e versioni. ROOT risolve il repository dal percorso dello script; EVIDENCE_ROOT e PROCEDURE_ROOT identificano le sorgenti. Dipendenze: re, sys, pathlib, tutte standard.

## Limiti e manutenzione

Il validatore verifica struttura, non qualità metodologica o reale indipendenza. Non modificare soglie per superare controlli. Gli errori sono associati ai rapporti; prima di integrare modifiche usare i test dedicati. Nessun validator viene eseguito come test di questa guida.
