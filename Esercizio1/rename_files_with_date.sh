#!/bin/bash

# ----------------------------------------------
# Script: rename_files_with_date.sh
# Purpose:
#   - Create dummy files using a for loop
#   - Collect all files (excluding directories) into an array
#   - Check if the array is empty and display files if not
#   - Rename all files by prefixing them with today's date (YYYY-MM-DD)
# Author: OpenAI ChatGPT
# ----------------------------------------------

# Step 1: Create dummy files
echo "Creating dummy files..."
for i in {1..5}; do
    touch "dummy_file_$i.txt"
done

# Step 2: Create array of all files (excluding directories)
file_array=()
for item in *.txt *.jpg; do
    if [[ -f "$item" ]]; then
        file_array+=("$item")
    fi
done


# Step 3: Check if the array is empty
if [ ${#file_array[@]} -eq 0 ]; then
    echo "No files found in the current directory."
else
    echo "Files found in the current directory:"
    for file in "${file_array[@]}"; do
        echo "  $file"
    done
fi

# Step 4: Get today's date in YYYY-MM-DD format
today=$(date +%F)

# Step 5: Rename files to begin with today's date
echo "Renaming files..."
for file in "${file_array[@]}"; do
    # Check if file already has the date prefix to avoid duplicate renaming
    if [[ "$file" != "$today-"* ]]; then
        mv "$file" "$today-$file"
        echo "Renamed '$file' to '$today-$file'"
    else
        echo "Skipping '$file' (already renamed)"
    fi
done

echo "Done!"
