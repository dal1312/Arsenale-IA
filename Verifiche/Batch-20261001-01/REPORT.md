# Campagna batch 2026-10-01 — esiti

| ARI | Test | Esito | Evidenza | Classificazione | Stato finale |
|---|---|---|---|---|---|
| ARI-1103 | Glossario applicato a un estratto reale del README | PASS | VER-ARI-1103-20261001-01 | Valida | Bozza verificabile |
| ARI-1104 | Correzione di una richiesta reale dell’utente | PASS | VER-ARI-1104-20261001-01 | Valida | Bozza verificabile |
| ARI-1203 | Scenario di ripetibilità normalizzazione → gzip → rilettura | PASS | VER-ARI-1203-20261001-01 | Valida | Bozza verificabile |
| ARI-1301 | Pulizia reversibile: quarantena di un temporaneo in fixture isolata | PASS | VER-ARI-1301-20261001-01 | Valida | Bozza verificabile |
| ARI-1702 | Persistenza e caricamento della memoria di un agente di prova | PASS | VER-ARI-1702-20261001-01 | Valida | Bozza verificabile |
| ARI-1804 | PermissionError: [WinError 5] Accesso negato: 'C:\\Users\\[UTENTE]\\AppData\\Local\\Microsoft\\WinGet\\Packages\\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\\ffmpeg-8.1.2-full_build\\bin\\ffmpeg.exe' | FAIL | Nessuna nuova evidenza canonica | Non applicabile | Bozza verificabile |
| ARI-1805 | Sorgente dal test ARI-1804 non disponibile | SKIPPED | Nessuna nuova evidenza canonica | Non applicabile | Bozza verificabile |

Tutte le candidature Da verificare sono state lette; criteri di selezione/esclusione in selezione.json. Cinque candidate già provate sono escluse esplicitamente. Le altre non selezionate non sono conteggiate come tentativi SKIPPED del batch.

Nessuna prova indipendente, nessuna promozione. Catalogo aggiornato solo nei cinque conteggi delle nuove evidenze valide.

Problemi: ARI-1804, PermissionError WinError 5 sul binario FFmpeg rilevato. Il sandbox ne impedisce l’esecuzione prima della generazione; nessuna conclusione sul funzionamento reale di FFmpeg. Nessuna correzione o ripetizione. ARI-1805, sorgente assente per effetto dell’impedimento precedente.

Backup catalogo: CATALOGO-prima-20261001.md.bak, SHA-256 084b1c103bd409c27037669d0289d592cd791fe46be313553a76dfc96bad1535.

I risultati FAIL/SKIPPED sono conservati in batch.json e nelle directory individuali. Non si è avviato un secondo batch.
