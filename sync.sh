#!/bin/bash
cp /storage/emulated/0/"CODES AND PROGRAMS"/"Programs or Code"/"File Handling"/GuessTheNumber.py . 2>/dev/null || echo "❌ Not found"
git add GuessTheNumber.py
if git diff --staged -- GuessTheNumber.py >/dev/null; then
  git commit -m "🔄 Pydroid sync $(date)"
  git push
  echo "✅ Synced to GitHub!"
else
  echo "ℹ️ No changes"
fi
