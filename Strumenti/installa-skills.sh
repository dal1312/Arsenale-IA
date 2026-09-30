#!/usr/bin/env sh
set -eu

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
procedure_root="$repo_root/Procedure"
mode="${1:-both}"
custom_path="${2:-}"
force=0

if [ "${3:-}" = "--force" ]; then
    force=1
elif [ "$mode" = "--force" ]; then
    echo "Uso: $0 [codex|claude|both|custom] [percorso-custom] [--force]" >&2
    exit 2
fi

install_to() {
    root="$1"
    mkdir -p "$root"
    installed=0

    for dir in "$procedure_root"/*; do
        [ -d "$dir" ] || continue
        [ -f "$dir/SKILL.md" ] || continue

        if [ ! -f "$dir/PROCEDURA.md" ]; then
            echo "Errore: manca PROCEDURA.md in $dir" >&2
            exit 1
        fi

        name=$(sed -n 's/^name:[[:space:]]*//p' "$dir/SKILL.md" | head -n 1 | tr -d '\r')
        if [ -z "$name" ]; then
            echo "Errore: campo name assente in $dir/SKILL.md" >&2
            exit 1
        fi

        dest="$root/$name"
        if [ -e "$dest" ] && [ "$force" -ne 1 ]; then
            printf 'Saltata (esiste già): %s. Usa --force per sovrascrivere.\n' "$dest"
            continue
        fi

        mkdir -p "$dest"
        cp "$dir/SKILL.md" "$dest/SKILL.md"
        cp "$dir/PROCEDURA.md" "$dest/PROCEDURA.md"

        printf 'Installata: %s -> %s\n' "$name" "$dest"
        installed=$((installed + 1))
    done

    printf '\nDestinazione: %s\nInstallate: %s\n' "$root" "$installed"
}

case "$mode" in
    codex)
        install_to "$HOME/.agents/skills"
        ;;
    claude)
        install_to "$HOME/.claude/skills"
        ;;
    both)
        install_to "$HOME/.agents/skills"
        install_to "$HOME/.claude/skills"
        ;;
    custom)
        if [ -z "$custom_path" ]; then
            echo "Uso: $0 custom /percorso/skills [--force]" >&2
            exit 2
        fi
        install_to "$custom_path"
        ;;
    *)
        echo "Uso: $0 [codex|claude|both|custom] [percorso-custom] [--force]" >&2
        exit 2
        ;;
esac
