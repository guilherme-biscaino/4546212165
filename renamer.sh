for file in *; do uuid=$(uuidgen); mv "$file" "$uuid.jpg"; done
