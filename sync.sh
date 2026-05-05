#!/bin/bash
cp ~/storage/shared/"CODES AND PROGRAMS"/"Programs or Code"/"File-Handling"/GuessTheNumber.py . 2>/dev/null || echo "❌ GuessTheNumber.py not found"
git add GuessTheNumber.py
if git diff --staged -- GuessTheNumber.py; then
  git commit -m "🔄 Auto-sync latest Pydroid changes"
  git push
  echo "✅ Synced to GitHub!"
else
  echo "ℹ️ No changes detected"
fi
