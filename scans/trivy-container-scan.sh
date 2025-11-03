#!/usr/bin/env bash
set -e

IMAGE=$1
OUTPUT="outputs/reports/trivy-${IMAGE//[:\/]/_}.json"

echo "🔍 Running Trivy vulnerability scan on image: $IMAGE"
trivy image --scanners vuln,secret --format json -o "$OUTPUT" "$IMAGE"
echo "✅ Trivy scan complete: $OUTPUT"
