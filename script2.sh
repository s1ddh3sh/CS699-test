#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 /path/to/file"
  exit 1
fi

FILE="$1"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP="${FILE}_backup_$TIMESTAMP"

cp "$FILE" "$BACKUP"
echo "Backup created: $BACKUP"