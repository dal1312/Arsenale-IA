# Comandi rapidi — usa Arsenale IA in linguaggio naturale

Non devi conoscere o ricordare i codici ARI. Descrivi il risultato che vuoi ottenere, indica il progetto o il materiale coinvolto e specifica i vincoli importanti. Il router interno seleziona la procedura più adatta consultando `AGENTI.md`, `CATALOGO.md` e lo `SKILL.md` della procedura.

## Frasi da usare

### Capire un progetto o risolvere un problema

- «Analizza questo progetto e dimmi com’è organizzato.»
- «Trova perché questa applicazione non parte e indicami la causa.»
- «Fammi un piano tecnico per aggiungere questa funzione.»
- «Correggi questo bug, spiegami cosa hai cambiato e verifica il flusso coinvolto.»
- «Revisiona questo codice Python/C#/C++/JavaScript e segnala i problemi concreti.»
- «Controlla se il progetto è pronto per il rilascio e cosa manca.»

### Scrivere e correggere testi

- «Correggi questo testo e rendilo più chiaro e professionale: …»
- «Riscrivi questa spiegazione in italiano tecnico, mantenendo il significato.»
- «Scrivi la documentazione tecnica per questo progetto.»
- «Prepara un manuale locale per chi usa questa applicazione.»
- «Crea un prompt per un agente che deve …»
- «Migliora questo prompt e rendi verificabile il risultato richiesto.»

### Creare siti, interfacce e applicazioni

- «Crea un sito moderno per …»
- «Crea un’applicazione web per gestire …»
- «Progetta un’interfaccia accessibile e semplice da usare per …»
- «Crea un’app Windows con grafica ispirata a iOS/macOS.»
- «Prepara questa app come programma Windows installabile.»
- «Trova immagini, font e icone adatti a questo progetto.»
- «Analizza questo sito e progettane una replica funzionale originale, senza copiarne codice, marchi o risorse.»
- «Migliora la pagina per rendere più chiara l’azione principale e aumentare le conversioni.»

### IA e agenti

- «Confronta questi modelli locali per il mio computer e il mio uso.»
- «Valuta se questo agente ha strumenti e memoria adeguati al compito.»
- «Progetta una memoria per un agente che deve …»
- «Crea un prompt per un agente che revisiona codice Python.»
- «Organizza questi agenti in un flusso di lavoro verificabile.»

### Windows, Linux e automazione

- «Diagnostica questo problema di Windows e indicami controlli sicuri.»
- «Spiegami perché questo container Docker non si avvia.»
- «Crea uno script PowerShell per ripetere questa operazione.»
- «Automatizza questo flusso locale mantenendo un controllo prima delle modifiche.»
- «Fai l’inventario di questa cartella e dimmi cosa contiene.»
- «Fai un backup locale verificabile prima di modificare il progetto.»
- «Pulisci questa cartella senza eliminare file senza averli identificati.»
- «Ripristina questa copia locale e verifica i file recuperati.»

### Verifiche e test

- «Verifica i test esistenti e dimmi quali sono passati o falliti.»
- «Apri il flusso nel browser e controlla i passaggi indicati.»
- «Prova l’interfaccia e segnala gli errori riproducibili.»
- «Controlla come si presenta su schermi desktop e mobili.»
- «Controlla sicurezza, segreti, privacy e licenze di questo progetto.»

## Se una richiesta coinvolge più attività

Descrivi comunque il risultato complessivo. Il router combina le procedure necessarie e dà precedenza a quella che governa il rischio principale. Per esempio:

- «Crea un’app Windows stile iOS e prepara anche l’installazione.»
- «Correggi il testo di questo prompt e poi trasformalo in istruzioni per un agente.»
- «Crea una pagina promozionale, scegli immagini con licenza e verifica la versione mobile.»
- «Automatizza il backup e controlla che i file salvati siano leggibili.»

Se manca un’informazione che cambia la soluzione o il rischio, l’assistente chiede un chiarimento mirato. La richiesta in linguaggio naturale non sostituisce eventuali vincoli espliciti: specifica «solo analisi», «read-only», «non modificare file» o «fermati prima di installare» quando vuoi limitare l’operazione.

## Riferimenti interni

<details>
<summary>Apri solo per manutenzione del router</summary>

I codici sono riferimenti del catalogo e non vanno inseriti nei prompt ordinari. Per scegliere e combinare le procedure si consultano `AGENTI.md` e `CATALOGO.md`; per il metodo completo si apre il relativo `SKILL.md` e, quando necessario, `PROCEDURA.md`.

</details>

## Regola pratica

Scrivi cosa vuoi ottenere, su quale progetto o file e con quali limiti. **Non serve chiedere «usa ARI-xxxx».**
