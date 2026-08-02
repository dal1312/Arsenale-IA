# ARI-0008 — Analisi della sicurezza

## Scopo
Valutare i rischi di sicurezza di un progetto e produrre interventi prioritizzati senza confondere ipotesi e vulnerabilità confermate.

## Input
- codice e configurazioni;
- modello di utilizzo;
- dati trattati;
- superfici esposte;
- dipendenze e infrastruttura.

## Output
- mappa delle superfici d'attacco;
- problemi classificati;
- evidenze riproducibili;
- piano di mitigazione;
- test di sicurezza richiesti.

## Procedura
1. Identificare beni, utenti, confini di fiducia e dati sensibili.
2. Elencare punti di ingresso, servizi, file, rete e dipendenze.
3. Verificare autenticazione, autorizzazione e separazione dei ruoli.
4. Controllare validazione degli input e codifica degli output.
5. Cercare segreti, credenziali, token e dati sensibili esposti.
6. Analizzare gestione sessioni, errori, log e configurazioni predefinite.
7. Verificare rischi di injection, traversal, esecuzione comandi, caricamento file e deserializzazione.
8. Controllare crittografia, firme, nonce, timestamp e protezione dai replay quando pertinenti.
9. Valutare dipendenze e immagini di distribuzione.
10. Classificare gravità, probabilità, impatto e costo di correzione.

## Classificazione
- confermata;
- altamente probabile;
- da verificare;
- miglioramento difensivo.

## Errori frequenti
- dichiarare vulnerabilità senza prova;
- affidarsi solo a uno scanner automatico;
- ignorare configurazione e distribuzione;
- correggere il sintomo senza eliminare la causa;
- pubblicare dettagli sensibili nel rapporto.

## Condizioni di uscita
- [ ] superfici d'attacco identificate;
- [ ] evidenze raccolte in modo sicuro;
- [ ] priorità assegnate;
- [ ] mitigazioni e test definiti;
- [ ] nessun segreto riportato in chiaro;
- [ ] rischi residui documentati.

## Rapporto finale
Per ogni elemento indicare: identificativo, categoria, evidenza, scenario di rischio, impatto, probabilità, priorità, mitigazione, verifica e rischio residuo.
