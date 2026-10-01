[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)][string]$TestoFile,
    [ValidateSet('it-IT-DiegoNeural', 'it-IT-GiuseppeMultilingualNeural', 'it-IT-ElsaNeural', 'it-IT-IsabellaNeural')]
    [string]$Voce = 'it-IT-DiegoNeural',
    [ValidatePattern('^[+-][0-9]+%$')][string]$Velocita = '-5%',
    [string]$CartellaOutput,
    [string]$Interprete = 'py'
)

$ErrorActionPreference = 'Stop'
$inputPath = (Resolve-Path -LiteralPath $TestoFile).Path
$utf8 = New-Object System.Text.UTF8Encoding($false, $true)
$testo = $utf8.GetString([System.IO.File]::ReadAllBytes($inputPath))
if ([string]::IsNullOrWhiteSpace($testo.Trim([char]0xFEFF))) { throw 'Testo vuoto' }
if (-not $CartellaOutput) { $CartellaOutput = [Environment]::GetFolderPath('Desktop') }
if (-not $CartellaOutput -or -not (Test-Path -LiteralPath $CartellaOutput -PathType Container)) {
    throw 'Specificare una cartella output esistente'
}
$basePath = (Resolve-Path -LiteralPath $CartellaOutput).Path
foreach ($comando in @($Interprete, 'ffmpeg', 'ffprobe')) {
    if (-not (Get-Command $comando -ErrorAction SilentlyContinue)) { throw "Comando mancante: $comando" }
}
$versione = & $Interprete -m edge_tts --version
if ($LASTEXITCODE -ne 0) { throw 'edge-tts non disponibile con interprete scelto' }
$voci = & $Interprete -m edge_tts --list-voices
if ($LASTEXITCODE -ne 0) { throw 'Catalogo voci non disponibile' }
if (-not ($voci -match ('^' + [regex]::Escape($Voce) + '\s'))) { throw "Voce non disponibile: $Voce" }

$runDir = Join-Path $basePath ('audio-edge-' + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $runDir | Out-Null
$mp3 = Join-Path $runDir 'audio.mp3'
$log = Join-Path $runDir 'sintesi.log'
Write-Host 'Sintesi online: il testo viene inviato al servizio Microsoft Edge.'
& $Interprete -m edge_tts --voice $Voce "--rate=$Velocita" --file $inputPath --write-media $mp3 2> $log
if ($LASTEXITCODE -ne 0) { throw "Sintesi fallita. Log: $log" }
if (-not (Test-Path -LiteralPath $mp3) -or (Get-Item -LiteralPath $mp3).Length -le 0) { throw 'Audio assente o vuoto' }
$probe = & ffprobe -v error -show_format -show_streams -of json $mp3 2> (Join-Path $runDir 'ffprobe.log')
if ($LASTEXITCODE -ne 0) { throw 'FFprobe fallito' }
$dati = ($probe -join "`n") | ConvertFrom-Json
$audio = @($dati.streams | Where-Object { $_.codec_type -eq 'audio' })
if ($audio.Count -ne 1 -or $audio[0].codec_name -ne 'mp3') { throw 'Stream MP3 inatteso' }
$durata = [double]::Parse($dati.format.duration, [Globalization.CultureInfo]::InvariantCulture)
if ($durata -le 0 -or [double]::IsNaN($durata) -or [double]::IsInfinity($durata)) { throw 'Durata non valida' }
& ffmpeg -v error -xerror -i $mp3 -map 0:a:0 -f null - 2> (Join-Path $runDir 'decodifica.log')
if ($LASTEXITCODE -ne 0) { throw 'Decodifica MP3 fallita' }
$manifest = [ordered]@{
    motore = 'edge-tts'; versione = ($versione -join ' '); online = $true
    voce = $Voce; velocita = $Velocita; input = $inputPath; output = $mp3
    durata_secondi = $durata; codec = $audio[0].codec_name
    frequenza_hz = [int]$audio[0].sample_rate; canali = [int]$audio[0].channels
    input_sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $inputPath).Hash
    output_sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $mp3).Hash
    decodifica = 'superata'; revisione_percettiva = 'da svolgere'
}
[System.IO.File]::WriteAllText((Join-Path $runDir 'manifest.json'), ($manifest | ConvertTo-Json), (New-Object System.Text.UTF8Encoding($false)))
[pscustomobject]$manifest
