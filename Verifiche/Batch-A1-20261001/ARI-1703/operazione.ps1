param([string]$Cartella)
$ErrorActionPreference='Stop'
$p=Join-Path $Cartella 'dato[1].txt'
$t=Get-Content -LiteralPath $p -Raw
$h=(Get-FileHash -LiteralPath $p -Algorithm SHA256).Hash
$errore=$false
try { Get-Content -LiteralPath (Join-Path $Cartella 'assente.txt') -ErrorAction Stop | Out-Null } catch { $errore=$true }
@{testo=$t;sha256=$h;errore_assente=$errore;file_count=@(Get-ChildItem -LiteralPath $Cartella -File).Count}|ConvertTo-Json
