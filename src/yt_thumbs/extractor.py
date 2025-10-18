"""YouTube thumbnail extractor utilities.

This module provides functions to extract video IDs from YouTube URLs,
generate thumbnail URLs, and download thumbnails.
"""

import re
import urllib.request
import urllib.error
from typing import Optional


def extract_video_id(url: str) -> Optional[str]:
    """Extract video ID from a YouTube URL.

    Supports the following URL formats:
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtu.be/VIDEO_ID
    - https://www.youtube.com/embed/VIDEO_ID

    Args:
        url: The YouTube URL to parse

    Returns:
        The video ID if found, None otherwise
    """
    # Pattern for youtube.com/watch?v=VIDEO_ID
    watch_pattern = r"(?:youtube\.com/watch\?v=)([a-zA-Z0-9_-]{11})"

    # Pattern for youtu.be/VIDEO_ID
    short_pattern = r"(?:youtu\.be/)([a-zA-Z0-9_-]{11})"

    # Pattern for youtube.com/embed/VIDEO_ID
    embed_pattern = r"(?:youtube\.com/embed/)([a-zA-Z0-9_-]{11})"

    # Try each pattern
    for pattern in [watch_pattern, short_pattern, embed_pattern]:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    return None


def get_thumbnail_url(video_id: str) -> str:
    """Get the maxresdefault thumbnail URL for a video ID.

    Args:
        video_id: The YouTube video ID

    Returns:
        The maxresdefault thumbnail URL
    """
    return f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"


def download_thumbnail(video_id: str, output_path: str) -> bool:
    """Download a YouTube thumbnail to a file.

    Attempts to download the maxresdefault quality thumbnail first.
    If that returns a 404, falls back to hqdefault quality.

    Args:
        video_id: The YouTube video ID
        output_path: Path where the thumbnail should be saved

    Returns:
        True if download succeeded, False otherwise
    """
    # Try maxresdefault first
    max_res_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"

    try:
        with urllib.request.urlopen(max_res_url) as response:
            # Check if we got actual image data (maxresdefault exists)
            content_length = response.headers.get("Content-Length")
            if content_length and int(content_length) > 1000:  # Valid image
                with open(output_path, "wb") as f:
                    f.write(response.read())
                return True
    except (urllib.error.HTTPError, urllib.error.URLError):
        pass

    # Fallback to hqdefault
    hq_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"

    try:
        with urllib.request.urlopen(hq_url) as response:
            with open(output_path, "wb") as f:
                f.write(response.read())
        return True
    except (urllib.error.HTTPError, urllib.error.URLError, OSError):
        return False
