param([string]$Sorgente,[string]$Destinazione)
$ErrorActionPreference='Stop'
if(Test-Path -LiteralPath $Destinazione){throw 'Destinazione già presente'}
New-Item -ItemType Directory -Path $Destinazione | Out-Null
foreach($nome in @('PROCEDURA.md','SKILL.md')) { Copy-Item -LiteralPath (Join-Path $Sorgente $nome) -Destination (Join-Path $Destinazione $nome); if((Get-FileHash -LiteralPath (Join-Path $Sorgente $nome)).Hash -ne (Get-FileHash -LiteralPath (Join-Path $Destinazione $nome)).Hash){throw 'Hash differente'} }
Write-Output 'COPIA-PORTABILE-OK'
