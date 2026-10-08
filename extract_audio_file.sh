#!/usr/bin/env bash
set -euo pipefail

if ! command -v ffmpeg &>/dev/null; then
    echo "ffmpeg not found. Install it first (e.g. brew install ffmpeg)." >&2
    exit 1
fi

if [ "$#" -ne 1 ] || [ ! -f "$1" ]; then
    echo "Usage: $0 <video file>" >&2
    exit 1
fi

video="$1"
out="${video%.*}.mp3"
echo "Extracting: $video -> $out"
ffmpeg -y -i "$video" -vn -acodec libmp3lame -q:a 2 "$out"
