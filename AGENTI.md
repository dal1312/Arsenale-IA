# Agenti Arsenale IA

Questo documento e il sistema di instradamento operativo sopra `CATALOGO.md`.

`CATALOGO.md` definisce le procedure disponibili. `AGENTI.md` aiuta a scegliere quale gruppo usare quando l'utente descrive un obiettivo in linguaggio naturale.

## Regola di uso

Quando l'utente formula una richiesta, identificare prima il macro-agente piu adatto, poi selezionare una o piu procedure ARI collegate.

Formato consigliato:

```text
Usa [macro-agente] per [obiettivo concreto].
```

Esempio:

```text
Usa Agente Web/App/Grafica per creare una app Windows con interfaccia stile iOS/macOS.
```

## Macro-agenti

## Agente Nucleo

Scopo: analisi iniziale, comprensione repository, diagnosi problemi e pianificazione tecnica.

Usare quando l'utente chiede:

- analizzare un progetto
- capire struttura e stato del repository
- diagnosticare errori
- preparare un piano tecnico
- decidere priorita di intervento

Procedure collegate:

- `ARI-0001` = Revisione repository
- `ARI-0003` = Diagnosi errori
- `ARI-0004` = Pianificazione tecnica

Esempi routing:

- "analizza questo progetto" -> `ARI-0001`
- "trova perche non funziona" -> `ARI-0003`
- "fammi un piano di lavoro" -> `ARI-0004`

Output atteso: stato del progetto, problemi prioritizzati, ipotesi tecniche, piano operativo.

## Agente Codice

Scopo: revisione, implementazione e rifattorizzazione del codice.

Usare quando l'utente chiede:

- correggere o migliorare codice
- implementare una feature
- fare rifattorizzazione
- revisionare codice Python, C#, C++, JavaScript, TypeScript o database
- ridurre debito tecnico

Procedure collegate:

- `ARI-0002` = Revisione codice
- `ARI-0005` = Implementazione controllata
- `ARI-0006` = Refactoring controllato
- `ARI-0101` = Revisione Python
- `ARI-0201` = Revisione C#
- `ARI-0301` = Revisione C++
- `ARI-0401` = Revisione JavaScript e TypeScript
- `ARI-0501` = Revisione database

Esempi routing:

- "sistema questo bug nel codice" -> `ARI-0003` + `ARI-0005`
- "revisiona questo file Python" -> `ARI-0101`
- "rifattorizza senza rompere niente" -> `ARI-0006`
- "controlla query e schema" -> `ARI-0501`

Output atteso: patch mirata, motivazione tecnica, rischi residui, verifiche consigliate o svolte.

## Agente Sistema

Scopo: operazioni su Git, Docker, Windows e Linux.

Usare quando l'utente chiede:

- gestire branch, diff, commit o release Git
- diagnosticare container Docker
- risolvere problemi Windows o PowerShell
- risolvere problemi Linux o shell
- controllare ambiente locale

Procedure collegate:

- `ARI-0601` = Revisione Git
- `ARI-0701` = Revisione Docker
- `ARI-0801` = Diagnostica Windows
- `ARI-0901` = Diagnostica Linux

Esempi routing:

- "controlla cosa e cambiato nel repo" -> `ARI-0601`
- "Docker non parte" -> `ARI-0701`
- "PowerShell da errore" -> `ARI-0801`
- "sistema uno script Bash" -> `ARI-0901`

Output atteso: diagnosi ambiente, comando sicuro, correzione configurazione, rischio operativo.

## Agente Documentazione

Scopo: produrre documentazione tecnica, manuali utente e glossari coerenti in italiano.

Usare quando l'utente chiede:

- scrivere o riorganizzare documentazione tecnica
- creare manuali utente locali
- uniformare termini italiani e glossario
- correggere o riscrivere testi proposti dall'utente
- spiegare uso, installazione o manutenzione del progetto

Procedure collegate:

- `ARI-1101` = Documentazione tecnica progetto
- `ARI-1102` = Manuale utente locale
- `ARI-1103` = Glossario italiano tecnico
- `ARI-1104` = Revisione e correzione testi

Esempi routing:

- "scrivi documentazione del progetto" -> `ARI-1101`
- "fammi un manuale utente" -> `ARI-1102`
- "sistema i termini inglesi" -> `ARI-1103`
- "correggi questo testo" -> `ARI-1104`
- "rendi questa frase piu tecnica" -> `ARI-1104`

Output atteso: documento chiaro, struttura navigabile, termini coerenti, esempi pratici.

## Agente Automazione

Scopo: creare automazioni locali ripetibili, controllabili e documentate.

Usare quando l'utente chiede:

- creare script PowerShell
- creare strumenti Python da riga di comando
- rendere ripetibile un flusso operativo locale
- ridurre passaggi manuali senza perdere controllo

Procedure collegate:

- `ARI-1201` = Automazione PowerShell
- `ARI-1202` = Automazione Python riga di comando
- `ARI-1203` = Flusso locale ripetibile

Esempi routing:

- "automatizza questa operazione in PowerShell" -> `ARI-1201`
- "crea uno strumento Python da terminale" -> `ARI-1202`
- "rendimi questo processo ripetibile" -> `ARI-1203`

Output atteso: script locale, parametri chiari, controlli di sicurezza, istruzioni d'uso.

## Agente Gestione Locale

Scopo: mantenere ordinato, recuperabile e verificabile il progetto locale.

Usare quando l'utente chiede:

- pulire cartelle di progetto
- creare o verificare backup locali
- fare inventario di file, moduli e risorse
- ripristinare una versione locale in modo controllato

Procedure collegate:

- `ARI-1301` = Pulizia progetto locale
- `ARI-1302` = Gestione backup locali
- `ARI-1303` = Inventario progetto locale
- `ARI-1304` = Ripristino controllato locale

Esempi routing:

- "pulisci il progetto senza perdere file" -> `ARI-1301`
- "fai backup prima di modificare" -> `ARI-1302`
- "dimmi cosa contiene questa cartella" -> `ARI-1303`
- "ripristina una copia precedente" -> `ARI-1304`

Output atteso: inventario, piano reversibile, backup verificato, azioni locali tracciabili.

## Agente Desktop Windows

Scopo: preparare applicazioni Windows locali, installatori, icone e metadati.

Usare quando l'utente chiede:

- confezionare una app Windows
- creare un installatore locale
- impostare icone, nome, versione e metadati
- adattare una interfaccia web/app a esperienza desktop Windows

Procedure collegate:

- `ARI-1401` = Confezionamento app Windows
- `ARI-1402` = Installatore Windows locale
- `ARI-1403` = Icone e metadati app
- `ARI-2107` = App Windows con interfaccia stile iOS/macOS

Esempi routing:

- "crea programma Windows da questa app" -> `ARI-1401`
- "fammi un installatore" -> `ARI-1402`
- "sistema icona e nome applicazione" -> `ARI-1403`
- "Windows ma stile iOS/macOS" -> `ARI-2107` + `ARI-1401`

Output atteso: pacchetto locale, istruzioni installazione, metadati coerenti, limiti verificati.

## Agente IA

Scopo: valutazione, ottimizzazione e progettazione di modelli, agenti, memoria e strumenti IA locali.

Usare quando l'utente chiede:

- scegliere un modello locale
- confrontare LLM, embedding o modelli multimodali
- valutare Ollama, llama.cpp, LM Studio, vLLM o ambienti equivalenti
- misurare qualita, latenza, memoria e stabilita
- ottimizzare inferenza locale
- progettare agenti, memoria o strumenti per agenti
- creare, correggere o migliorare prompt per agenti

Procedure collegate:

- `ARI-1501` = Valutazione modelli locali
- `ARI-1502` = Ottimizzazione inferenza locale
- `ARI-1601` = Revisione modelli linguistici
- `ARI-1701` = Revisione agenti IA
- `ARI-1702` = Progettazione memoria agente
- `ARI-1703` = Valutazione strumenti agente
- `ARI-1704` = Orchestrazione multi-agente locale
- `ARI-1705` = Progettazione prompt per agenti

Esempi routing:

- "quale modello locale uso per coding?" -> `ARI-1501`
- "confronta questi LLM sul mio PC" -> `ARI-1501`
- "misura memoria e velocita" -> `ARI-1501`
- "ottimizza tempi e memoria del modello" -> `ARI-1502`
- "progetta memoria per un agente" -> `ARI-1702`
- "valuta strumenti disponibili per un agente" -> `ARI-1703`
- "crea un prompt per un agente" -> `ARI-1705`
- "migliora questo prompt agente" -> `ARI-1705`

Output atteso: confronto ripetibile, risultati misurati, limiti, architettura agente, raccomandazione motivata.

## Agente Web/App/Grafica

Scopo: creazione e revisione di siti, applicazioni web, interfacce, risorse visive, repliche funzionali legali e app Windows con estetica iOS/macOS.

Usare quando l'utente chiede:

- creare siti web
- creare applicazioni web o pannelli di controllo
- fare grafica, interfacce o sistemi di progettazione
- trovare risorse visive migliori
- replicare legalmente un sito
- creare programmi Windows con grafica iOS/macOS
- migliorare esperienza utente, accessibilita o conversione

Procedure collegate:

- `ARI-2101` = Revisione siti web statici
- `ARI-2102` = Revisione applicazioni web complete e a pagina singola
- `ARI-2103` = Design e accessibilita interfaccia
- `ARI-2104` = Prestazioni esperienza utente e interfaccia web/app
- `ARI-2105` = Ricerca e selezione risorse visive
- `ARI-2106` = Replica funzionale legale di un sito
- `ARI-2107` = App Windows con interfaccia stile iOS/macOS
- `ARI-2108` = Esperienza utente, accessibilita e conversione

Esempi routing:

- "crea una pagina promozionale moderna" -> `ARI-2101` + `ARI-2103`
- "crea una applicazione web gestionale" -> `ARI-2102` + `ARI-2103`
- "trova font, icone e immagini migliori" -> `ARI-2105`
- "rifai questo sito senza copiare asset" -> `ARI-2106` + `ARI-2105`
- "fammi una app Windows stile iOS/macOS" -> `ARI-2107` + `ARI-2103`
- "migliora conversione pagina" -> `ARI-2108`
- "ottimizza interfaccia lenta" -> `ARI-2104`

Output atteso: progetto interfaccia, codice o revisione, risorse selezionate, limiti legali, controlli adattivi e accessibilita.

## Agente Sicurezza

Scopo: controllare sicurezza applicativa, segreti, privacy, licenze e dipendenze.

Usare quando l'utente chiede:

- verificare rischi di sicurezza in web o app
- controllare chiavi, token e segreti locali
- valutare privacy e dati personali
- controllare licenze di risorse e librerie

Procedure collegate:

- `ARI-2201` = Revisione sicurezza web e app
- `ARI-2202` = Gestione segreti locali
- `ARI-2203` = Privacy e dati personali
- `ARI-2204` = Licenze risorse e dipendenze

Esempi routing:

- "controlla sicurezza applicazione" -> `ARI-2201`
- "verifica se ci sono segreti nel progetto" -> `ARI-2202`
- "controlla privacy e dati personali" -> `ARI-2203`
- "controlla licenze asset e librerie" -> `ARI-2204`

Output atteso: rischi classificati, file coinvolti, azioni correttive, limiti legali o operativi.

## Agente Browser/Test

Scopo: automatizzare browser, testare interfacce e verificare schermate adattive.

Usare quando l'utente chiede:

- controllare un flusso dentro browser
- eseguire prove end-to-end di interfaccia
- catturare o confrontare schermate
- verificare layout su desktop, tablet o telefono

Procedure collegate:

- `ARI-2501` = Automazione browser controllata
- `ARI-2502` = Test end-to-end interfaccia
- `ARI-2503` = Audit schermate adattive

Esempi routing:

- "apri browser e verifica questo flusso" -> `ARI-2501`
- "testa login e navigazione" -> `ARI-2502`
- "controlla versione mobile e desktop" -> `ARI-2503`

Output atteso: passaggi ripetibili, schermate o evidenze, problemi visivi, raccomandazioni correttive.

## Agente Rilascio

Scopo: preparare rilascio, pacchetti, checklist e controlli finali.

Usare quando l'utente chiede:

- preparare una release
- controllare readiness di rilascio
- generare checklist finale
- verificare registro modifiche, versioni, pacchetti o flussi operativi

Procedure collegate:

- `ARI-0010` = Preparazione rilascio
- `ARI-0009` = Verifica test
- `ARI-0601` = Revisione Git

Esempi routing:

- "prepara il rilascio" -> `ARI-0010`
- "controlla se siamo pronti a pubblicare" -> `ARI-0010` + `ARI-0009`
- "verifica tag e changelog" -> `ARI-0010` + `ARI-0601`

Output atteso: checklist release, rischi bloccanti, controlli superati, azioni residue.

## Agente Verifica

Scopo: verifiche operative, test, evidenze, promozioni e stato procedura.

Usare quando l'utente chiede:

- verificare procedure
- controllare report in `Verifiche/`
- promuovere una procedura a verificata
- controllare test ed evidenze
- validare coerenza tra catalogo, procedure e competenze

Procedure collegate:

- `ARI-0009` = Verifica test
- `VERIFICA.md` = regole di evidenza operativa
- `Strumenti/verifica_procedure.py`
- `Strumenti/verifica_skills.py`
- `Strumenti/verifica_evidenze.py`
- `Strumenti/verifica_promozioni.py`

Esempi routing:

- "verifica la cartella" -> `ARI-0009`
- "controlla se le competenze funzionano" -> `ARI-0009`
- "promuovi una procedura" -> `ARI-0009` + `VERIFICA.md`
- "controlla report e placeholder" -> `Strumenti/verifica_evidenze.py`

Output atteso: esito verificabile, errori concreti, file coinvolti, stato promozione.

## Router rapido

```text
analizza progetto                  -> Agente Nucleo / ARI-0001
diagnostica errore                 -> Agente Nucleo / ARI-0003
fai piano                          -> Agente Nucleo / ARI-0004
revisiona codice                   -> Agente Codice / ARI-0002
implementa modifica                -> Agente Codice / ARI-0005
rifattorizzazione                  -> Agente Codice / ARI-0006
controlla prestazioni              -> Agente Nucleo / ARI-0007 oppure Agente Web/App/Grafica / ARI-2104
controlla sicurezza                -> Agente Nucleo / ARI-0008
verifica test                      -> Agente Verifica / ARI-0009
prepara rilascio                   -> Agente Rilascio / ARI-0010
Python                             -> Agente Codice / ARI-0101
C#                                 -> Agente Codice / ARI-0201
C++                                -> Agente Codice / ARI-0301
JavaScript o TypeScript            -> Agente Codice / ARI-0401
database                           -> Agente Codice / ARI-0501
Git                                -> Agente Sistema / ARI-0601
Docker                             -> Agente Sistema / ARI-0701
Windows                            -> Agente Sistema / ARI-0801
Linux                              -> Agente Sistema / ARI-0901
modelli IA locali                  -> Agente IA / ARI-1501
ottimizzazione inferenza locale    -> Agente IA / ARI-1502
revisione agente IA                -> Agente IA / ARI-1701
memoria agente                     -> Agente IA / ARI-1702
strumenti agente                   -> Agente IA / ARI-1703
orchestrazione agenti locali       -> Agente IA / ARI-1704
prompt per agenti                  -> Agente IA / ARI-1705
documentazione progetto            -> Agente Documentazione / ARI-1101
manuale utente locale              -> Agente Documentazione / ARI-1102
glossario italiano tecnico         -> Agente Documentazione / ARI-1103
correzione o riscrittura testi     -> Agente Documentazione / ARI-1104
automazione PowerShell             -> Agente Automazione / ARI-1201
strumento Python da terminale      -> Agente Automazione / ARI-1202
flusso locale ripetibile           -> Agente Automazione / ARI-1203
pulizia progetto locale            -> Agente Gestione Locale / ARI-1301
backup locale                      -> Agente Gestione Locale / ARI-1302
inventario progetto                -> Agente Gestione Locale / ARI-1303
ripristino locale                  -> Agente Gestione Locale / ARI-1304
confezionamento app Windows        -> Agente Desktop Windows / ARI-1401
installatore Windows               -> Agente Desktop Windows / ARI-1402
icone e metadati app               -> Agente Desktop Windows / ARI-1403
sito statico                       -> Agente Web/App/Grafica / ARI-2101
applicazione web o pannello        -> Agente Web/App/Grafica / ARI-2102
design interfaccia stile iOS/macOS -> Agente Web/App/Grafica / ARI-2103
prestazioni interfaccia            -> Agente Web/App/Grafica / ARI-2104
risorse, font, icone, immagini     -> Agente Web/App/Grafica / ARI-2105
replica legale sito                -> Agente Web/App/Grafica / ARI-2106
app Windows stile iOS/macOS        -> Agente Web/App/Grafica / ARI-2107
esperienza utente e conversione    -> Agente Web/App/Grafica / ARI-2108
sicurezza web e app                -> Agente Sicurezza / ARI-2201
segreti locali                     -> Agente Sicurezza / ARI-2202
privacy e dati personali           -> Agente Sicurezza / ARI-2203
licenze risorse e dipendenze       -> Agente Sicurezza / ARI-2204
automazione browser                -> Agente Browser/Test / ARI-2501
test interfaccia end-to-end        -> Agente Browser/Test / ARI-2502
schermate adattive                 -> Agente Browser/Test / ARI-2503
```

## Criterio di scelta multipla

Se una richiesta attraversa piu aree, usare prima la procedura che definisce il rischio principale.

Esempi:

- creare app Windows stile iOS con risorse esterne -> `ARI-2107` + `ARI-2105` + `ARI-2103`
- confezionare app Windows stile iOS/macOS -> `ARI-2107` + `ARI-1401` + `ARI-1403`
- creare documentazione e manuale progetto -> `ARI-1101` + `ARI-1102` + `ARI-1103`
- correggere testo e trasformarlo in prompt agente -> `ARI-1104` + `ARI-1705`
- automatizzare backup locale -> `ARI-1201` + `ARI-1302`
- clonare legalmente una pagina promozionale e migliorarne conversione -> `ARI-2106` + `ARI-2108`
- creare applicazione web e prepararla al rilascio -> `ARI-2102` + `ARI-0010`
- correggere bug di interfaccia lenta -> `ARI-0003` + `ARI-2104` + `ARI-0005`
- testare una app web con schermate -> `ARI-2501` + `ARI-2502` + `ARI-2503`

## Regola finale

Il codice ARI non deve essere ricordato a memoria. Deve essere risolto tramite questo instradamento, `CATALOGO.md` e lo `SKILL.md` della procedura scelta.

