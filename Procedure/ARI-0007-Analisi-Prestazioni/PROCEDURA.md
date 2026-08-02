# ARI-0007 — Analisi delle prestazioni

## Scopo
Individuare colli di bottiglia reali e proporre interventi basati su misurazioni.

## Principio
Non ottimizzare ciò che non è stato misurato.

## Input
- scenario lento o costoso;
- ambiente riproducibile;
- metriche disponibili;
- obiettivo prestazionale.

## Output
- linea di base;
- profilo dei colli di bottiglia;
- cause probabili;
- piano di ottimizzazione prioritizzato;
- verifica prima/dopo.

## Procedura
1. Definire lo scenario e la soglia attesa.
2. Stabilire dati, carico e ambiente di prova.
3. Misurare tempo, CPU, memoria, I/O e rete quando pertinenti.
4. Ripetere le prove per eliminare risultati casuali.
5. Profilare il percorso critico.
6. Separare sintomi, cause e ipotesi.
7. Stimare impatto e costo degli interventi.
8. Applicare una modifica per volta.
9. Ripetere esattamente la stessa prova.
10. Documentare miglioramento e regressioni.

## Controlli
- complessità algoritmica;
- chiamate ripetute;
- query duplicate;
- operazioni bloccanti;
- allocazioni e copie inutili;
- caricamento completo di dati grandi;
- assenza di timeout, paginazione o limiti;
- concorrenza e lock;
- cache non necessarie o mancanti.

## Errori frequenti
- usare impressioni al posto delle metriche;
- confrontare ambienti diversi;
- ottimizzare un percorso non critico;
- introdurre cache senza strategia di invalidazione;
- sacrificare correttezza e leggibilità per guadagni irrilevanti.

## Condizioni di uscita
- [ ] linea di base registrata;
- [ ] collo di bottiglia dimostrato;
- [ ] intervento misurato con prova equivalente;
- [ ] correttezza verificata;
- [ ] risultato e limiti documentati.

## Rapporto finale
Riportare scenario, ambiente, strumenti, metriche iniziali, causa, interventi proposti, risultati finali e rischi residui.
