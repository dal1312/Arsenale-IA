# Preparazione alla pubblicazione

## Perimetro

Preparazione del working tree senza staging, commit, push o operazioni remote. Nessun audio rigenerato e nessuna modifica a procedure, soglie o classificazioni operative.

## Backup

Originali conservati fuori dal repository in Documents, nella directory `Arsenale-IA-Backup-Pubblicazione-20261001-234053-611189`: 338 file, manifest con percorso originale, dimensione e SHA-256, copie verificate prima della redazione/esclusione. Il manifest completo resta locale perché contiene percorsi personali. Nessun originale escluso è stato cancellato dal repository.

## Evidenze redatte

65 file preesistenti preparati: due script parametrizzati, documentazione con placeholder, supporti redatti e note editoriali nei rapporti della campagna corrente. Hash attestati, risultati e metadati di classificazione conservati. Leggere [le note probatorie](Verifiche/LEGGIMI-PUBBLICAZIONE.md) prima di confrontare checksum o usare supporti storici.

## Classificazione degli artefatti

| Gruppo | Decisione | Motivo |
|---|---|---|
| Evidenze canoniche, snapshot e risultati necessari | MANTENERE SOLO COME EVIDENZA REDATTA quando contengono dati locali | Conservazione del significato probatorio; limiti pubblici espliciti |
| 13 backup .bak non tracciati | IGNORARE | Conservati localmente e nel backup esterno |
| 13 backup .bak-* già tracciati | DA VALUTARE MANUALMENTE | .gitignore non modifica il tracking; occorre un intervento Git distinto e autorizzato |
| 51 log temporanei | IGNORARE | Diagnostica storica conservata localmente |
| bin/obj, PDB, DLL, EXE e cache di build | IGNORARE | Output generati, non sorgenti |
| dotnet-home | IGNORARE | Stato locale del toolchain |
| Due SQLite e input.bin | IGNORARE | Fixture temporanee; risultati sintetici già documentati |
| Due piccoli archivi gzip | PUBBLICARE | Fixture sintetiche del test di compressione, con utilità probatoria |
| Fixture .env ARI-2202 | PUBBLICARE | Solo FITTIZIO_* o [OMESSO], contesto sintetico esplicito |
| Baseline, backup.json, inventario Hermes e runner batch | IGNORARE | Diagnostica e stato locale, non interfacce operative pubbliche |
| Copie runtime duplicate, backup documenti e ripristino isolato | IGNORARE | Duplicati generati nei test |
| Program.cs e OmegaFL.Launcher.csproj copiati dal progetto esterno | DA VALUTARE MANUALMENTE | Confermare destinazione pubblicabile dei sorgenti esterni |
| Altri documenti e skill canoniche | PUBBLICARE | Nessuna esclusione indiscriminata delle fonti canoniche |

## Staging simulato

L'elenco esatto è in [PUBBLICAZIONE-file.json](PUBBLICAZIONE-file.json): separa tutti i file pubblicabili, i soli candidati al prossimo commit, gli ignorati e quelli da valutare. Nessun git add eseguito. Non usare git add indiscriminato.

I 13 backup già tracciati restano parte del repository fino a un intervento autorizzato sull'indice: non sono esclusi retroattivamente dalla storia. Questa limitazione corregge il precedente riepilogo, che non aveva incluso i nomi con suffisso .bak-* fra gli artefatti storici.

## Controlli conclusivi

La scansione dei candidati pubblicabili, il parser PowerShell, i validatori, gli unittest e git diff --check vengono eseguiti una sola volta dopo la preparazione. Gli esiti osservati sono comunicati nel rapporto finale di sessione; questa nota non presume il loro successo.

## Decisione finale sui 15 elementi

Tutti i 15 elementi sospesi sono ESCLUDERE: 13 backup operativi (classe B) da rimuovere soltanto dal tracking e due sorgenti esterni non redistribuibili. Nessuna decisione utente residua. Le decisioni precedenti riportate sopra descrivono la preparazione iniziale; questa sezione e l'elenco JSON aggiornato definiscono la selezione finale.

I backup sono citati negli inventari e nelle baseline storiche come file osservati: non sono ingressi necessari per procedure o test. La rimozione dall'indice non cancella le copie locali, non cambia gli inventari storici e non riscrive la cronologia.

Program.cs e OmegaFL.Launcher.csproj corrispondono byte per byte alle sorgenti locali omega-fl-pilot/tools/windows-launcher. Il remote documentato nel relativo clone locale è dal1312/omega-fl-pilot; non è stato interrogato GitHub. Il titolare del copyright non è identificato nella licenza locale. La licenza Omega FL Internal Pilot vieta redistribuzione e pubblicazione senza autorizzazione scritta separata; non è compatibile con la pubblicazione qui prevista. I sorgenti servivano al test storico C#, non al funzionamento delle procedure Arsenale.

Anche README.md della copia del launcher è materiale dello stesso progetto: escluso dalla lista precedentemente approvata per il medesimo vincolo, senza cancellazione. Le tre esclusioni sono esplicite in .gitignore. Risultati e hash del test storico rimangono documentati.

Lista definitiva: 252 candidati da aggiungere selettivamente e 13 rimozioni dal tracking. Nessuno staging indiscriminato, commit o push autorizzato. Lo stato osservato dell'indice e l'audit conclusivo vengono riportati nella sessione.
