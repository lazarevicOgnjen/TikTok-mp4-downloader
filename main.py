#!/usr/bin/env python3
import os
import subprocess
import sys

URL = os.getenv("TIKTOK_URL")
if not URL:
    sys.exit("❌  TIKTOK_URL environment variable missing")

# 1) video+audio MP4
subprocess.run(
    ["yt-dlp", "-f", "bv*[ext=mp4]+ba", "--no-part", "-o", "video.mp4", URL.strip()],
    check=True,
)

# 2) audio-only MP3
subprocess.run(
    ["yt-dlp", "-x", "--audio-format", "mp3", "--no-part", "-o", "audio.mp3", URL.strip()],
    check=True,
)

print("✅  video.mp4  and  audio.mp3  ready")
