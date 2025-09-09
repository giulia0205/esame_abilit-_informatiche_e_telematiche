#!/bin/bash


# Script: rename_files_with_date.sh
# Scopo:
#   - Crea dummy files attraverso un loop for
#   - Raccoglie tutti i files (escluse le directories) in un array
#   - Controlla che l'array non sia vuoto e se non lo è stampa i files
#   - Rinomina tutti i files con la data corrente

# Creazione dummy files
echo "Creating dummy files..."
for i in {1..5}; do
    touch "dummy_file_$i.txt"
done

# Creazione array di tutti i files (escludendo le directories)
file_array=()
for item in *.txt *.jpg; do
    if [[ -f "$item" ]]; then
        file_array+=("$item")
    fi
done


# Controllo se l'array è vuoto
if [ ${#file_array[@]} -eq 0 ]; then
    echo "No files found in the current directory."
else
    echo "Files found in the current directory:"
    for file in "${file_array[@]}"; do
        echo "  $file"
    done
fi

# Data nel formato YYYY-MM-DD
today=$(date +%F)

# I file vengono rinominati con la data
echo "Renaming files..."
for file in "${file_array[@]}"; do
    # Controllo se il file ha già il prefisso-data in modo da non duplicare la rinominazione
    if [[ "$file" != "$today-"* ]]; then
        mv "$file" "$today-$file"
        echo "Renamed '$file' to '$today-$file'"
    else
        echo "Skipping '$file' (already renamed)"
    fi
done

echo "Done!"
