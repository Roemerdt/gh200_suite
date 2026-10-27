#!/bin/bash
# Copies the committed tree (without results/) to a cluster
# usage: bash harness/sync.sh <host>:<path>
set -e
cd "$(dirname "$0")/.."
DEST=$1
[ -n "$DEST" ] || { echo "usage: sync.sh <host>:<path>" >&2; exit 2; }
if [ -n "$(git status --porcelain --untracked-files=no)" ]; then
  echo "tracked files have uncommitted changes; commit first" >&2; exit 1
fi
rsync -a --exclude results --exclude .venv --exclude .git --exclude bin --exclude 'core.*' --exclude __pycache__ --exclude docs ./ "$DEST/"
echo "synced to $DEST"
