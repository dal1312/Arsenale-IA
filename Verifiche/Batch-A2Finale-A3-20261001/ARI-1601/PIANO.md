# Piano ARI-1601
Compito: classificare tre righe di fixture seguendo criteri dichiarati.
Dataset: [{id:A,testo:errore apertura file},{id:B,testo:operazione completata},{id:C,testo:avviso spazio ridotto}].
Istruzioni: assegnare errore/successo/avviso in quell'ordine; restituire esclusivamente JSON con chiave risultati e tre oggetti id,classe. Nessun campo extra, nessuna spiegazione.
Criterio oggettivo: JSON valido, tre id A/B/C unici e classi esatte, nessun campo extra.
Modello: risposta del modello della sessione, non chiamata al runtime llama.cpp. Un solo caso delimitato; nessuna generalizzazione. Autovalutazione non cieca e non indipendente.
