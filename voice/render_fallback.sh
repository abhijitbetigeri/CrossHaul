#!/usr/bin/env bash
# Render the stage fallback clip via the ElevenLabs TTS API.
#
# Why this exists: the live agent is the real artifact, but Frontier Tower wifi at 5:10pm with a
# full room is exactly when a network call picks its moment. This produces a file that plays from
# disk, identical every rehearsal, immune to the venue.
#
#   export ELEVENLABS_API_KEY=...
#   ./voice/render_fallback.sh [voice_id]
#
# Voice id: find one at https://elevenlabs.io/app/voice-library, or leave the default.
# Creator plan includes the commercial licence, so the clip is safe to put in a public demo video.

set -euo pipefail

: "${ELEVENLABS_API_KEY:?Set ELEVENLABS_API_KEY first (elevenlabs.io -> profile -> API keys)}"

VOICE_ID="${1:-JBFqnCBsd6RMkjVDRZzb}"   # "George" — calm, low-affect, reads as infrastructure
OUT="voice/crosshaul-approval.mp3"

LINE="Downtown is thirty-six kilos short on tomatoes for the weekend. I moved ten from Marina — that lot expires in two days — and drafted a purchase order for the remaining twenty-six at two-oh-five a kilo from Bay Foods. Fifty-three thirty. Want me to send it?"

mkdir -p voice

curl -sS -X POST "https://api.elevenlabs.io/v1/text-to-speech/${VOICE_ID}" \
  -H "xi-api-key: ${ELEVENLABS_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "$(python3 - "$LINE" <<'PY'
import json, sys
print(json.dumps({
    "text": sys.argv[1],
    "model_id": "eleven_multilingual_v2",
    # Slightly high stability and low style: this should sound like a system, not a performance.
    "voice_settings": {"stability": 0.65, "similarity_boost": 0.75, "style": 0.0},
}))
PY
)" \
  --output "$OUT"

# curl writes the error JSON to the output file on failure, so check we got audio.
if file "$OUT" | grep -qiE 'audio|mpeg'; then
  printf 'ok  %s  (%s bytes)\n' "$OUT" "$(wc -c < "$OUT" | tr -d ' ')"
else
  printf 'FAILED — the API returned:\n' >&2
  cat "$OUT" >&2
  rm -f "$OUT"
  exit 1
fi
