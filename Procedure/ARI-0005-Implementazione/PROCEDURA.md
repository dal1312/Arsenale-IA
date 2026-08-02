# ARI-0005 — Implementazione controllata

## Scopo
Realizzare una modifica tecnica in modo incrementale, verificabile e coerente con la specifica approvata.

## Prerequisiti
- requisito o piano approvato;
- criteri di accettazione;
- ambiente funzionante;
- test iniziali noti.

## Procedura
1. Confermare l'ambito e il punto di partenza.
2. Eseguire i test pertinenti prima delle modifiche.
3. Scegliere il più piccolo incremento funzionante.
4. Aggiungere o aggiornare il test che descrive il comportamento.
5. Applicare la modifica minima necessaria.
6. Eseguire il test specifico.
7. Rifattorizzare solo mantenendo i test verdi.
8. Ripetere per l'incremento successivo.
9. Eseguire controlli statici, suite completa e build.
10. Verificare manualmente il flusso principale quando necessario.
11. Aggiornare documentazione e registro delle modifiche.
12. Produrre un riepilogo con file modificati, test ed eventuali limiti.

## Regole
- non ampliare l'ambito senza motivazione;
- non nascondere test falliti;
- non rimuovere controlli per ottenere un esito positivo;
- non introdurre astrazioni senza un confine reale;
- mantenere commit e modifiche comprensibili.

## Condizioni di uscita
Criteri di accettazione soddisfatti, test pertinenti superati, build verificata, documentazione aggiornata e rischi residui dichiarati.