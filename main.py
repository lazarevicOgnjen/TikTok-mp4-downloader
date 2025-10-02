import os
import subprocess
import sys

url = os.getenv("TIKTOK_URL")
if not url:
    sys.exit("TIKTOK_URL env variable missing")

# –no-part –output makes the file name predictable
subprocess.run([
    "yt-dlp",
    "-f", "bv*[ext=mp4]+ba",
    "--no-watermark",
    "--no-part",
    "-o", "video.mp4",
    url
], check=True)
