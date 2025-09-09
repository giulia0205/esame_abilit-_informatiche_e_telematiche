#!/bin/bash


# Script: sum_numbers.sh
# Scopo:
#   - Crea un file vuoto
#   - Scrive i numeri interi da 1 a 10 in colonna
#   - Calcola la somma totale usando AWK
#   - Stampa la somma sul terminale


# Nome del file da usare
FILE="numbers.txt"

# Creazione di un file vuoto (lo sovrascrive se esiste già)
> "$FILE"

# Scrittura dei numeri da 1 a 10 nel file attraverso un loop for
for i in {1..10}; do
    echo "$i" >> "$FILE"
done

# Calcolo della somma usando awk
SUM=$(awk '{ sum += $1 } END { print sum }' "$FILE")

# Output della somma calcolata
echo "La somma dei numeri da 1 a 10 è: $SUM"
