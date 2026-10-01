[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)][string]$TestoFile,
    [ValidateSet('Nicola','Sara','Paola','Diego','Giuseppe','Elsa','Isabella')]
    [string]$Voce = 'Nicola',
    [ValidateRange(-50,100)][int]$VelocitaPercento = -5,
    [string]$CartellaOutput,
    [string]$RuntimeRoot,
    [string]$KokoroModelli = 'D:\DOWNLOAD\PROGRAMMI\TESTO\AI Ebook to Audio Converter 1.1.29\App\AI Ebook to Audio Converter\_internal\kokoro-tts',
    [string]$PiperModello = 'C:\Users\[UTENTE]\AppData\Local\calibre-cache\piper-voices\it_IT-paola-medium.onnx'
)
$ErrorActionPreference = 'Stop'
$inputPath = (Resolve-Path -LiteralPath $TestoFile).Path
$utf8 = New-Object System.Text.UTF8Encoding($false, $true)
$testo = $utf8.GetString([System.IO.File]::ReadAllBytes($inputPath))
if ([string]::IsNullOrWhiteSpace($testo.Trim([char]0xFEFF))) { throw 'Testo vuoto' }
$rate = if ($VelocitaPercento -ge 0) { "+$VelocitaPercento%" } else { "$VelocitaPercento%" }
$edgeVoci = @{ Diego='it-IT-DiegoNeural'; Giuseppe='it-IT-GiuseppeMultilingualNeural'; Elsa='it-IT-ElsaNeural'; Isabella='it-IT-IsabellaNeural' }
if ($edgeVoci.ContainsKey($Voce)) {
    & (Join-Path $PSScriptRoot 'Genera-Audio-Edge.ps1') -TestoFile $inputPath -Voce $edgeVoci[$Voce] -Velocita $rate -CartellaOutput $CartellaOutput
    return
}
if (-not $CartellaOutput) { $CartellaOutput = [Environment]::GetFolderPath('Desktop') }
if (-not $CartellaOutput -or -not (Test-Path -LiteralPath $CartellaOutput -PathType Container)) { throw 'Cartella output non disponibile' }
foreach ($comando in @('ffmpeg','ffprobe')) {
    if (-not (Get-Command $comando -ErrorAction SilentlyContinue)) { throw "Comando mancante: $comando" }
}
if (-not $RuntimeRoot) {
    $candidati = @(
        (Join-Path $env:LOCALAPPDATA 'Arsenale-IA\TTS'),
        (Join-Path $env:USERPROFILE 'AppData\Local\Packages\OpenAI.Codex_2p2nqsd0c76g0\LocalCache\Local\Arsenale-IA\TTS')
    )
    $RuntimeRoot = $candidati | Where-Object { Test-Path -LiteralPath $_ -PathType Container } | Select-Object -First 1
}
if (-not $RuntimeRoot) { throw 'Runtime non trovato: specificare -RuntimeRoot' }
$motore = if ($Voce -eq 'Paola') { 'piper' } else { 'kokoro' }
$python = Join-Path $RuntimeRoot "$motore-env\Scripts\python.exe"
if (-not (Test-Path -LiteralPath $python -PathType Leaf)) { throw "Interprete mancante: $python" }
$modello = if ($motore -eq 'piper') { $PiperModello } else { Join-Path $KokoroModelli 'kokoro-v1.0.onnx' }
if (-not (Test-Path -LiteralPath $modello -PathType Leaf)) { throw "Modello mancante: $modello" }
$voci = Join-Path $KokoroModelli 'voices-v1.0.bin'
if ($motore -eq 'kokoro' -and -not (Test-Path -LiteralPath $voci -PathType Leaf)) { throw 'Pacchetto Kokoro mancante' }
if ($motore -eq 'piper' -and -not (Test-Path -LiteralPath ($modello + '.json') -PathType Leaf)) { throw 'Configurazione Piper mancante' }
$runDir = Join-Path (Resolve-Path -LiteralPath $CartellaOutput).Path ('audio-' + $Voce.ToLowerInvariant() + '-' + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $runDir | Out-Null
$wav = Join-Path $runDir 'master.wav'
$mp3 = Join-Path $runDir 'audio.mp3'
$voceId = @{ Nicola='im_nicola'; Sara='if_sara'; Paola='paola' }[$Voce]
$speed = (1 + $VelocitaPercento / 100.0).ToString([Globalization.CultureInfo]::InvariantCulture)
$argomenti = @('-B',(Join-Path $PSScriptRoot 'sintesi_audio_locale.py'),'--engine',$motore,'--input',$inputPath,'--output',$wav,'--model',$modello,'--voice',$voceId,'--speed',$speed)
if ($motore -eq 'kokoro') { $argomenti += @('--voices',$voci) }
& $python @argomenti 2> (Join-Path $runDir 'sintesi.log')
if ($LASTEXITCODE -ne 0) { throw "Sintesi fallita: $runDir" }
& ffmpeg -v error -n -i $wav -c:a libmp3lame -q:a 2 $mp3 2> (Join-Path $runDir 'conversione.log')
if ($LASTEXITCODE -ne 0) { throw 'Conversione MP3 fallita' }
$probe = & ffprobe -v error -show_format -show_streams -of json $mp3
if ($LASTEXITCODE -ne 0) { throw 'FFprobe fallito' }
$dati = ($probe -join "`n") | ConvertFrom-Json
$durata = [double]::Parse($dati.format.duration,[Globalization.CultureInfo]::InvariantCulture)
if ($durata -le 0 -or [double]::IsNaN($durata) -or [double]::IsInfinity($durata)) { throw 'Durata non valida' }
& ffmpeg -v error -xerror -i $mp3 -map 0:a:0 -f null - 2> (Join-Path $runDir 'decodifica.log')
if ($LASTEXITCODE -ne 0) { throw 'Decodifica fallita' }
$manifest = [ordered]@{
    motore=$motore; voce=$voceId; online=$false; velocita_percento=$VelocitaPercento
    modello=$modello; input=$inputPath; output=$mp3; master=$wav; durata_secondi=$durata
    input_sha256=(Get-FileHash -LiteralPath $inputPath -Algorithm SHA256).Hash
    output_sha256=(Get-FileHash -LiteralPath $mp3 -Algorithm SHA256).Hash
    decodifica='superata'; revisione_percettiva='da svolgere'
}
[System.IO.File]::WriteAllText((Join-Path $runDir 'manifest.json'),($manifest | ConvertTo-Json),(New-Object System.Text.UTF8Encoding($false)))
[pscustomobject]$manifest
