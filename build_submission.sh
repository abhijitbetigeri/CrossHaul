#!/usr/bin/env bash
# Build the submission ZIP. Excludes anything the form forbids: secrets, .env, node_modules,
# large datasets, git internals.
set -euo pipefail
OUT=~/Desktop/CrossHaul_CrossHaul_Submission.zip
rm -f "$OUT"
cd ~/projects/mise
zip -rq "$OUT" . \
  -x '.git/*' -x '*/.git/*' \
  -x '.env' -x '*/.env' -x '.env.local' -x '*/.env.local' \
  -x '.env.production' -x '*/.env.production' \
  -x '*/.insforge/*' -x '.insforge/*' \
  -x '*/node_modules/*' -x 'node_modules/*' \
  -x '*/__pycache__/*' -x '*.pyc' \
  -x '*/.venv/*' -x '*/venv/*' \
  -x '.DS_Store' -x '*/.DS_Store' \
  -x 'build_submission.sh'
echo "built: $OUT  ($(du -h "$OUT" | cut -f1))"
