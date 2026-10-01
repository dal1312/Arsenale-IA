$ErrorActionPreference = 'Stop'
$base = Split-Path $PSScriptRoot -Parent
$ffmpeg = (Get-Command ffmpeg -ErrorAction Stop).Source
$ffprobe = (Get-Command ffprobe -ErrorAction Stop).Source
$results = [ordered]@{
    data = (Get-Date).ToString('o')
    criteri = 'MP3: un solo stream audio, mono, frequenza positiva, durata entro 0.001 s dal manifest; clipping: picco campione inferiore a 0 dBFS e zero campioni a fondo scala; silenzi descrittivi: soglia -50 dB, durata minima 0.5 s. Nessuna soglia di qualità o loudness retroattiva.'
    ffmpeg = $ffmpeg
    ffprobe = $ffprobe
    ffmpeg_versione_attuale = (& $ffmpeg -version | Select-Object -First 1)
    ffprobe_versione_attuale = (& $ffprobe -version | Select-Object -First 1)
    voci = @()
}
foreach ($voice in @('im_nicola', 'if_sara', 'paola')) {
    $manifestPath = Join-Path $base "Supporto-Audio-20261001\$voice.json"
    $m = Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json
    $audio = $m.output
    $probe = & $ffprobe -v error -show_format -show_streams -of json $audio
    if ($LASTEXITCODE -ne 0) { throw "Analisi metadati fallita: $voice" }
    $probePath = Join-Path $PSScriptRoot "$voice-probe.json"
    if (Test-Path -LiteralPath $probePath) { throw 'Output esistente' }
    [IO.File]::WriteAllText($probePath, ($probe -join "`n"), (New-Object Text.UTF8Encoding($false)))
    $p = ($probe -join "`n") | ConvertFrom-Json
    $log = Join-Path $PSScriptRoot "$voice-misure.log"
    if (Test-Path -LiteralPath $log) { throw 'Log esistente' }
    & $ffmpeg -hide_banner -nostdin -v info -i $audio -map 0:a:0 -af 'astats=metadata=0:reset=0,silencedetect=noise=-50dB:d=0.5' -f null - 2> $log
    $exitCode = $LASTEXITCODE
    if ($exitCode -ne 0) { throw "Misure fallite: $voice" }
    $s = @($p.streams)
    $results.voci += [ordered]@{
        voce = $voice; audio = $audio; bytes = (Get-Item -LiteralPath $audio).Length
        metadati = $s; durata = $p.format.duration
        profilo_tecnico = ($s.Count -eq 1 -and $s[0].codec_type -eq 'audio' -and $s[0].codec_name -eq 'mp3' -and $s[0].channels -eq 1 -and [int]$s[0].sample_rate -gt 0 -and [Math]::Abs([double]$p.format.duration - [double]$m.durata_secondi) -le 0.001)
        exit_code_misure = $exitCode; log = $log
        hash_audio = (Get-FileHash -LiteralPath $audio -Algorithm SHA256).Hash
        hash_coincidente = ((Get-FileHash -LiteralPath $audio -Algorithm SHA256).Hash -eq $m.output_sha256)
    }
}
$out = Join-Path $PSScriptRoot 'risultati.json'
if (Test-Path -LiteralPath $out) { throw 'Risultati esistenti' }
[IO.File]::WriteAllText($out, ($results | ConvertTo-Json -Depth 12), (New-Object Text.UTF8Encoding($false)))
$results.voci | Select-Object voce,durata,profilo_tecnico,hash_coincidente,exit_code_misure | Format-Table
