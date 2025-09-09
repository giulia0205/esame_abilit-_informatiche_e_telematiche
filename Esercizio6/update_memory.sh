#!/bin/bash


# Script: update_memory.sh
# Scopo:
#   - Crea un file di configurazione con dati fittizi sulla memoria
#   - Usa awk per modificare il valore di MaxMem da 512 a 1024 direttamente sullo stesso file



# Nome del file di configurazione
CONFIG_FILE="memory_config.txt"

# Creazione del file con il contenuto specificato
cat << EOF > "$CONFIG_FILE"
# c o n t r o l o f memory r e q u i r e m e n t s
BoundaryLayerFactor 3 . 0
MaxMem 512
MaxMemPerParticle 240
PredPeakFactor 0 . 8
EOF

# Modifica del valore MaxMem usando awk (salva l'output modificato in un file temporaneo, poi sovrascrive il file originale)
awk '{
    if ($1 == "MaxMem") {
        $2 = "1024"
    }
    print
}' "$CONFIG_FILE" > tmpfile && mv tmpfile "$CONFIG_FILE"

# Messaggio di conferma
echo "Valore di MaxMem aggiornato a 1024 nel file '$CONFIG_FILE'"
