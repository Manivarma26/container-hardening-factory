#!/usr/bin/env bash
set -e

IMAGE=$1
OUTPUT="outputs/reports/dockle-${IMAGE//[:\/]/_}.json"

echo "🔒 Running Dockle CIS benchmark scan on image: $IMAGE"
dockle --exit-code 0 --json "$OUTPUT" "$IMAGE"
echo "✅ Dockle scan complete: $OUTPUT"
