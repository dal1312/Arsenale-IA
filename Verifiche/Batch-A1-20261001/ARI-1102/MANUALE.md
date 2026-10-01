# Manuale: copia portabile per consultazione offline

1. Individuare la cartella sorgente ARI-1705 contenente PROCEDURA.md e SKILL.md.
2. Scegliere una destinazione nuova, fuori da profili runtime.
3. Eseguire `pwsh -NoProfile -File passi.ps1 -Sorgente <cartella> -Destinazione <cartella nuova>`.
4. Attendere COPIA-PORTABILE-OK e aprire PROCEDURA.md per il metodo, SKILL.md per l’adattatore.

Lo script rifiuta una destinazione esistente e controlla SHA-256 di entrambi i file. Non installa né attiva skill. Serve PowerShell 7 già disponibile. Nessuna rete o configurazione richiesta.
