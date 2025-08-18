#!/bin/bash

if [ $# -ne 2 ]; then
  echo "Incorrect number of arguments."
  exit 1
fi

FOLDER_PATH="$1"
REMOTE_URL="$2"

# Check if folder exists
if [ ! -d "$FOLDER_PATH" ]; then
  echo "Error: Folder '$FOLDER_PATH' does not exist."
  exit 1
fi

# Navigate to the folder
cd "$FOLDER_PATH" || exit

# Initialize Git if not already a repo
if [ ! -d .git ]; then
  git init
fi

# Add all files, commit, set remote, and push
git add .
git commit -m "Automated commit"
git branch -M main
git remote add origin "$REMOTE_URL"
git push -u origin main

echo "Folder '$FOLDER_PATH' uploaded to GitHub repo: $REMOTE_URL"