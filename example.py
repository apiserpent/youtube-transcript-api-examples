"""YouTube Transcript API - Python example.

Docs: https://apiserpent.com/youtube-transcript-api
Run:  SERPENT_API_KEY=sk_live_... python example.py
"""
import os
import sys

import requests

API_KEY = os.environ.get("SERPENT_API_KEY")
if not API_KEY:
    sys.exit("Set the SERPENT_API_KEY environment variable first.")

params = {"video": "https://youtu.be/8jPQjjsBbIc", "output": "text"}

response = requests.get(
    "https://apiserpent.com/api/social/youtube/transcript",
    params=params,
    headers={"X-API-Key": API_KEY},
    timeout=60,
)
response.raise_for_status()
data = response.json()

for key in ['title', 'channel', 'language']:
    print(f"{key}: {data.get(key)}")
print((data.get("text") or "")[:500])
