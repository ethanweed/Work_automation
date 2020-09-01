#!/bin/bash
for i in *.mkv ; do ffmpeg -i "$i" -qscale 0 "${i%.*}.mp4" ; done

