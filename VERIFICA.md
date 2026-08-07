# Standard di verifica operativa

## Scopo

Questo documento definisce quando una procedura Arsenale IA può passare dallo stato **Bozza verificabile** o **In revisione** allo stato **Verificata**.

La conformità di `PROCEDURA.md` e `SKILL.md` dimostra che il materiale è strutturalmente valido. La verifica operativa dimostra invece che il metodo è stato applicato a casi reali e produce risultati utili, tracciabili e ripetibili.

## Principi

1. La procedura viene valutata sul metodo, non sulla qualità del progetto bersaglio.
2. Un progetto bersaglio può avere errori o test falliti: questo non invalida la procedura se il metodo li rileva e li classifica correttamente.
3. Ogni esecuzione deve essere ancorata a una revisione immutabile: commit, tag, versione o altro identificativo equivalente.
4. Devono essere separati fatti osservati, inferenze, limiti e attività non eseguite.
5. La mancata possibilità di eseguire un controllo è ammessa solo se motivata nel rapporto.
6. Una prova autoreferenziale su Arsenale IA non è sufficiente da sola per la promozione a **Verificata**.

## Evidenza minima per lo stato Verificata

Una procedura può essere promossa a **Verificata** quando esistono almeno due rapporti operativi validi che soddisfano tutti i seguenti criteri:

- riguardano la stessa versione metodologica della procedura oppure versioni compatibili senza cambi del comportamento verificato;
- usano almeno due contesti o progetti reali distinti;
- almeno una prova è esterna ad Arsenale IA;
- coprono le fasi sostanziali della procedura;
- registrano ambiente, input, verifiche, output e limiti;
- producono un esito comprensibile e, quando previsto, rilievi prioritizzati;
- non evidenziano contraddizioni irrisolte nel metodo;
- almeno una prova include esecuzione reale di test, build, validatori o controlli equivalenti quando la procedura li prevede.

La promozione viene registrata nella procedura, nel catalogo e nella matrice delle verifiche.

## Stati dell'evidenza

- **Eseguita:** il rapporto descrive un'applicazione reale completata.
- **Valida:** il rapporto è completo e può contribuire alla promozione della procedura.
- **Inconcludente:** l'applicazione non copre abbastanza metodo o mancano evidenze essenziali.
- **Respinta:** il rapporto contiene contraddizioni, dati non tracciabili o non riguarda realmente la procedura dichiarata.

## Rapporto operativo obbligatorio

Ogni file `VER-*.md` deve dichiarare:

- Identificativo
- Procedura
- Versione procedura
- Data
- Progetto
- Revisione
- Tipo prova
- Stato evidenza

Le sezioni obbligatorie sono:

1. `## Ambito`
2. `## Ambiente e accesso`
3. `## Passi esercitati`
4. `## Verifiche osservabili`
5. `## Rilievi prodotti`
6. `## Limiti`
7. `## Esito sul progetto`
8. `## Esito sulla procedura`

## Tipi di prova

- **Interna:** il bersaglio è Arsenale IA o un artefatto creato appositamente per testare la procedura.
- **Indipendente:** il bersaglio è un progetto reale con scopo proprio, non creato per validare Arsenale IA.

Per la promozione serve almeno una prova **Indipendente**.

## Regola sui test del progetto bersaglio

Un test fallito nel progetto bersaglio è un'evidenza da analizzare, non un fallimento automatico della procedura. Il rapporto deve distinguere:

- errore del progetto;
- errore o instabilità dell'ambiente;
- controllo non eseguibile;
- limite del metodo;
- evidenza insufficiente.

## Automazione

La struttura dei rapporti viene controllata da:

```text
py Strumenti/verifica_evidenze.py
```

Su Linux/macOS usare `python3`.

Il validatore controlla struttura e riferimenti; la decisione metodologica resta documentata nei rapporti e nel catalogo.
