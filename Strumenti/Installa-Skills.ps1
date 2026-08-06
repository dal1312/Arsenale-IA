[CmdletBinding()]
param(
    [ValidateSet("Codex", "Claude", "Entrambi", "Personalizzato")]
    [string]$Destinazione = "Entrambi",

    [string]$Percorso,

    [switch]$Forza
)

$ErrorActionPreference = "Stop"

$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$ProcedureRoot = Join-Path $RepoRoot "Procedure"

function Get-SkillName {
    param([Parameter(Mandatory = $true)][string]$SkillFile)

    foreach ($line in Get-Content -LiteralPath $SkillFile -Encoding UTF8) {
        if ($line -match '^name:\s*([a-z0-9]+(?:-[a-z0-9]+)*)\s*$') {
            return $Matches[1]
        }
    }

    throw "Campo 'name' non valido o assente in $SkillFile"
}

function Install-ArsenaleSkills {
    param([Parameter(Mandatory = $true)][string]$Root)

    New-Item -ItemType Directory -Path $Root -Force | Out-Null
    $installate = 0
    $saltate = 0

    foreach ($dir in Get-ChildItem -LiteralPath $ProcedureRoot -Directory | Sort-Object Name) {
        $skillFile = Join-Path $dir.FullName "SKILL.md"
        $procedureFile = Join-Path $dir.FullName "PROCEDURA.md"

        if (-not (Test-Path -LiteralPath $skillFile)) {
            continue
        }

        if (-not (Test-Path -LiteralPath $procedureFile)) {
            throw "Manca PROCEDURA.md in $($dir.FullName)"
        }

        $name = Get-SkillName -SkillFile $skillFile
        $dest = Join-Path $Root $name

        if ((Test-Path -LiteralPath $dest) -and -not $Forza) {
            Write-Warning "Esiste già: $dest. Usa -Forza per riallinearla."
            $saltate++
            continue
        }

        New-Item -ItemType Directory -Path $dest -Force | Out-Null
        Copy-Item -LiteralPath $skillFile -Destination (Join-Path $dest "SKILL.md") -Force
        Copy-Item -LiteralPath $procedureFile -Destination (Join-Path $dest "PROCEDURA.md") -Force

        Write-Host "Installata: $name -> $dest"
        $installate++
    }

    Write-Host ""
    Write-Host "Destinazione: $Root"
    Write-Host "Installate: $installate"
    Write-Host "Saltate:    $saltate"
}

$targets = @()

switch ($Destinazione) {
    "Codex" {
        $targets += (Join-Path $HOME ".agents\skills")
    }
    "Claude" {
        $targets += (Join-Path $HOME ".claude\skills")
    }
    "Entrambi" {
        $targets += (Join-Path $HOME ".agents\skills")
        $targets += (Join-Path $HOME ".claude\skills")
    }
    "Personalizzato" {
        if ([string]::IsNullOrWhiteSpace($Percorso)) {
            throw "Con -Destinazione Personalizzato devi specificare -Percorso."
        }
        $targets += $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($Percorso)
    }
}

foreach ($target in ($targets | Select-Object -Unique)) {
    Install-ArsenaleSkills -Root $target
}
