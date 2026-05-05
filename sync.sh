#!/bin/bash
# YOUR REAL PATH from find command above
cp ~/storage/shared/"CODES AND PROGRAMS"/"Programs or Code"/"File-Handling"/GuessTheNumber.py . 2>/dev/null || echo "File not found"
git add GuessTheNumber.py
git commit -m "Auto-sync from Pydroid 3" || echo "No changes"
git push
echo "✅ Synced to GitHub!"
