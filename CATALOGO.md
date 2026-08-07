# Catalogo ufficiale

Legenda: **Disponibile** = procedura presente; **Pianificata** = codice riservato.

## Nucleo

- **ARI-0001 — Revisione repository** — Disponibile
- **ARI-0002 — Revisione codice** — Disponibile
- **ARI-0003 — Diagnosi errori** — Disponibile
- **ARI-0004 — Pianificazione tecnica** — Disponibile
- **ARI-0005 — Implementazione controllata** — Disponibile
- **ARI-0006 — Refactoring controllato** — Disponibile
- **ARI-0007 — Analisi prestazioni** — Disponibile
- **ARI-0008 — Analisi sicurezza** — Disponibile
- **ARI-0009 — Verifica test** — Disponibile
- **ARI-0010 — Preparazione rilascio** — Disponibile

## Sistemi e sviluppo

- **ARI-0101 — Revisione Python** — Disponibile
- **ARI-0201 — Revisione C#** — Disponibile
- **ARI-0301 — Revisione C++** — Disponibile
- **ARI-0401 — Revisione JavaScript e TypeScript** — Disponibile
- **ARI-0501 — Revisione database** — Disponibile
- **ARI-0601 — Revisione Git** — Disponibile
- **ARI-0701 — Revisione Docker** — Disponibile
- **ARI-0801 — Diagnostica Windows** — Disponibile
- **ARI-0901 — Diagnostica Linux** — Disponibile

## Intelligenza artificiale

- ARI-1501 — Valutazione modelli locali — Pianificata
- ARI-1502 — Ottimizzazione inferenza locale — Pianificata
- ARI-1601 — Revisione modelli linguistici — Pianificata
- ARI-1701 — Revisione agenti IA — Pianificata
- ARI-1702 — Progettazione memoria agente — Pianificata
- ARI-1703 — Valutazione strumenti agente — Pianificata

## Multimedia e applicazioni specialistiche

- ARI-1801 — Revisione pipeline audio — Pianificata
- ARI-1802 — Revisione pipeline video — Pianificata
- ARI-1901 — Revisione visione artificiale — Pianificata
- ARI-2001 — Revisione software di stampa 3D — Pianificata

## Stato di conformità

- procedure disponibili: **19**;
- conformi alla struttura canonica di `STANDARD.md`: **19/19**;
- procedure disponibili con adattatore `SKILL.md`: **19/19**;
- fonte canonica: `PROCEDURA.md`;
- formato adattatori: Agent Skills;
- utilizzo locale: supportato senza dipendenza runtime da GitHub.

## Verifica operativa

| Procedura | Stato | Evidenze valide | Prova indipendente |
| --- | --- | ---: | --- |
| ARI-0001 — Revisione repository | **Verificata** | 2 | Sì |
| ARI-0002 — Revisione codice | **Verificata** | 2 | Sì |
| ARI-0003 — Diagnosi errori | **Verificata** | 2 | Sì |
| ARI-0004 — Pianificazione tecnica | **Verificata** | 2 | Sì |
| ARI-0005 — Implementazione controllata | **Verificata** | 2 | Sì |
| ARI-0006 — Refactoring controllato | Da verificare | 0 | No |
| ARI-0007 — Analisi prestazioni | Da verificare | 0 | No |
| ARI-0008 — Analisi sicurezza | Da verificare | 0 | No |
| ARI-0009 — Verifica test | **Verificata** | 2 | Sì |
| ARI-0010 — Preparazione rilascio | Da verificare | 0 | No |

Le evidenze sono archiviate in `Verifiche/` e seguono `VERIFICA.md`. Lo stato **Verificata** non è assegnato dalla sola conformità automatica.

La conformità strutturale viene verificata da `Strumenti/verifica_procedure.py`; la compatibilità agente da `Strumenti/verifica_skills.py`; i rapporti operativi da `Strumenti/verifica_evidenze.py`; la soglia conteggiabile delle promozioni da `Strumenti/verifica_promozioni.py`.

Le procedure pianificate ricevono `PROCEDURA.md` e `SKILL.md` conformi prima di passare allo stato **Disponibile**.

Per installazione locale, percorsi ed esempi vedere `COMPATIBILITA.md`.

I codici assegnati sono permanenti. Il catalogo viene aggiornato quando una procedura passa da pianificata a disponibile o cambia stato di verifica.
