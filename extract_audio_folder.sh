#!/usr/bin/env bash
set -euo pipefail

if ! command -v ffmpeg &>/dev/null; then
    echo "ffmpeg not found. Install it first (e.g. brew install ffmpeg)." >&2
    exit 1
fi

if [ "$#" -ne 1 ] || [ ! -d "$1" ]; then
    echo "Usage: $0 <folder>" >&2
    exit 1
fi

folder="$1"
shopt -s nullglob nocaseglob
videos=("$folder"/*.{mp4,mkv,mov,avi,webm,flv,wmv,m4v})
shopt -u nocaseglob

if [ "${#videos[@]}" -eq 0 ]; then
    echo "No video files found in $folder" >&2
    exit 1
fi

for video in "${videos[@]}"; do
    out="${video%.*}.mp3"
    echo "Extracting: $video -> $out"
    ffmpeg -y -i "$video" -vn -acodec libmp3lame -q:a 2 "$out"
done
