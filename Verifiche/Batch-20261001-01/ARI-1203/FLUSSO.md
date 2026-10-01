# Flusso locale

Input README UTF-8 → normalizzazione terminatori LF → gzip con mtime=0 → rilettura/decompressione → confronto byte. Due esecuzioni isolate sono le due osservazioni dello stesso test di ripetibilità, non due evidenze.
