#!/usr/bin/env bash
set -euo pipefail

# DISCLAIMER: uso autorizado únicamente.
# Autor: met4ll0f | https://github.com/met4ll0f

if [[ $# -ne 2 ]]; then
  echo "Uso: $0 <host_list.txt> <output_directory>"
  exit 1
fi

INPUT_FILE="$1"
OUTPUT_DIR="$2"
mkdir -p "$OUTPUT_DIR"

webscreenshot -i "$INPUT_FILE" -o "$OUTPUT_DIR" -m -r firefox || true

cat > "$OUTPUT_DIR/index.html" <<EOF
<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Web Screenshot Report</title></head>
<body style="background:#111;color:#eee;font-family:monospace">
<h1>Web Screenshot Report - met4ll0f</h1>
<p><a href="https://github.com/met4ll0f">GitHub</a></p>
<ul>
EOF

while read -r HOST; do
  [[ -z "$HOST" || "$HOST" =~ ^# ]] && continue
  for PROTO in http https; do
    PORT=80
    [[ "$PROTO" == "https" ]] && PORT=443
    IMG_FILE="${PROTO}_${HOST}_${PORT}.png"
    if [[ -f "$OUTPUT_DIR/$IMG_FILE" ]]; then
      echo "<li><a href=\"$IMG_FILE\">${PROTO}://${HOST}</a></li>" >> "$OUTPUT_DIR/index.html"
    fi
  done
done < "$INPUT_FILE"

echo "</ul></body></html>" >> "$OUTPUT_DIR/index.html"
echo "[OK] Reporte: $OUTPUT_DIR/index.html"
