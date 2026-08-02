# ARI-0901 — Diagnostica Linux

## Scopo
Analizzare problemi di servizi, prestazioni, dipendenze e configurazione su sistemi Linux con un metodo documentato e reversibile.

## Procedura
1. Identificare distribuzione, versione del kernel, ambiente e sintomo osservato.
2. Riprodurre il problema e registrare il contesto operativo.
3. Esaminare i registri di sistema e dell'applicazione pertinenti.
4. Verificare uso di processore, memoria, spazio, rete e permessi.
5. Controllare pacchetti, dipendenze e configurazioni recentemente modificate.
6. Ridurre il problema al componente minimo coinvolto.
7. Valutare un'ipotesi alla volta con verifiche non distruttive.
8. Applicare la correzione minima e documentare la procedura di ripristino.

## Regole
- evitare modifiche irreversibili;
- non ampliare permessi senza una causa dimostrata;
- non disattivare protezioni per aggirare il problema;
- conservare le evidenze utili alla diagnosi.

## Output
Rapporto con causa confermata o probabile, evidenze, correzione proposta, ripristino e verifica finale.