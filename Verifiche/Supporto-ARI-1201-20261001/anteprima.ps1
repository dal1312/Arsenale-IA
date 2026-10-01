param(
    [Parameter(Mandatory=$true)][string]$Sorgente,
    [Parameter(Mandatory=$true)][string]$Destinazione
)
$ErrorActionPreference = 'Stop'
$sourcePath = (Resolve-Path -LiteralPath $Sorgente).Path
if (Test-Path -LiteralPath $Destinazione) { throw 'Destinazione esistente: arresto' }
$utf8 = New-Object System.Text.UTF8Encoding($false, $true)
$text = [IO.File]::ReadAllText($sourcePath, $utf8)
$hashBefore = (Get-FileHash -LiteralPath $sourcePath -Algorithm SHA256).Hash
$escaped = [System.Net.WebUtility]::HtmlEncode($text)
$html = '<!DOCTYPE html><html lang="it"><head><meta charset="utf-8"/><title>Anteprima locale README</title></head><body><pre>' + $escaped + '</pre></body></html>'
$bytes = $utf8.GetBytes($html)
$stream = [IO.File]::Open($Destinazione, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write)
try { $stream.Write($bytes, 0, $bytes.Length) } finally { $stream.Dispose() }
$saved = [IO.File]::ReadAllText($Destinazione, $utf8)
$match = [regex]::Match($saved, '<pre>([\s\S]*)</pre>')
if (-not $match.Success -or [System.Net.WebUtility]::HtmlDecode($match.Groups[1].Value) -cne $text) { throw 'Contenuto non corrispondente' }
if ((Get-FileHash -LiteralPath $sourcePath -Algorithm SHA256).Hash -ne $hashBefore) { throw 'Sorgente modificata' }
$result = [ordered]@{
    esito='PASS'; sorgente=$sourcePath; output=$Destinazione
    sorgente_sha256=$hashBefore; output_sha256=(Get-FileHash -LiteralPath $Destinazione -Algorithm SHA256).Hash
    caratteri_sorgente=$text.Length; bytes_output=$bytes.Length
    roundtrip_testo=$true; sorgente_invariata=$true
    powershell=$PSVersionTable.PSVersion.ToString()
    criterio='HTML UTF-8 nuovo, contenuto README completo e protetto tramite HtmlEncode; rilettura e HtmlDecode identiche al sorgente; hash sorgente invariato. Nessuna risorsa esterna o esecuzione del testo.'
}
$result | ConvertTo-Json
