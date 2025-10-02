#!/usr/bin/env python3
import os, subprocess, sys

URL = os.getenv("TIKTOK_URL")
if not URL:
    sys.exit("❌  TIKTOK_URL missing")

# 1) best *pre-muxed* MP4 (video + audio)
subprocess.run(
    ["yt-dlp", "-f", "bv*+ba/b", "--no-part", "-o", "video.mp4", URL.strip()],
    check=True,
)

# 2) audio-only MP3
subprocess.run(
    ["yt-dlp", "-x", "--audio-format", "mp3", "--no-part", "-o", "audio.mp3", URL.strip()],
    check=True,
)

print("✅  video.mp4  and  audio.mp3  ready")
