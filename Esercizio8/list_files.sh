#!/bin/bash


# Script: list_files.sh
# Scopo:
#   - Accetta come argomento una directory
#   - Verifica che la directory esista
#   - Entra nella directory
#   - Elenca:
#       * tutti i file regolari
#       * tutte le sottodirectory
#       * tutti i file vuoti


# Controlla che sia stato passato un argomento
if [ -z "$1" ]; then
    echo "Errore: devi specificare una directory come argomento."
    exit 1
fi

# Salva il percorso della directory
DIR="$1"

# Verifica che la directory esista
if [ ! -d "$DIR" ]; then
    echo "Errore: la directory '$DIR' non esiste."
    exit 2
fi

# Entra nella directory
cd "$DIR" || { echo "Errore: impossibile accedere alla directory."; exit 3; }

# Stampa intestazione
echo "Contenuto della directory: $DIR"
echo

# Elenca solo i file regolari
echo "File regolari:"
find . -maxdepth 1 -type f

echo

# Elenca solo le directory
echo "Directory:"
find . -maxdepth 1 -type d ! -name "."

echo

# Elenca solo i file vuoti
echo "File vuoti:"
find . -maxdepth 1 -type f -empty

echo
