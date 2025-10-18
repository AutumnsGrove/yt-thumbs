"""Tests for the YouTube thumbnail extractor module.

This module contains unit tests for the extractor.py functions including:
- extract_video_id() with valid and invalid URLs
- get_thumbnail_url() for URL format verification
"""

from yt_thumbs.extractor import extract_video_id, get_thumbnail_url


class TestExtractVideoId:
    """Test cases for the extract_video_id function."""

    def test_extract_video_id_from_watch_url(self):
        """Test extracting video ID from standard youtube.com/watch URL."""
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        video_id = extract_video_id(url)
        assert video_id == "dQw4w9WgXcQ"

    def test_extract_video_id_from_short_url(self):
        """Test extracting video ID from shortened youtu.be URL."""
        url = "https://youtu.be/dQw4w9WgXcQ"
        video_id = extract_video_id(url)
        assert video_id == "dQw4w9WgXcQ"

    def test_extract_video_id_from_embed_url(self):
        """Test extracting video ID from youtube.com/embed URL."""
        url = "https://www.youtube.com/embed/dQw4w9WgXcQ"
        video_id = extract_video_id(url)
        assert video_id == "dQw4w9WgXcQ"

    def test_extract_video_id_from_watch_url_without_https(self):
        """Test extracting video ID from watch URL without protocol."""
        url = "youtube.com/watch?v=dQw4w9WgXcQ"
        video_id = extract_video_id(url)
        assert video_id == "dQw4w9WgXcQ"

    def test_extract_video_id_from_short_url_without_https(self):
        """Test extracting video ID from short URL without protocol."""
        url = "youtu.be/dQw4w9WgXcQ"
        video_id = extract_video_id(url)
        assert video_id == "dQw4w9WgXcQ"

    def test_extract_video_id_with_empty_string(self):
        """Test that empty string returns None."""
        url = ""
        video_id = extract_video_id(url)
        assert video_id is None

    def test_extract_video_id_with_random_url(self):
        """Test that random non-YouTube URL returns None."""
        url = "https://www.example.com/some/random/page"
        video_id = extract_video_id(url)
        assert video_id is None

    def test_extract_video_id_with_invalid_youtube_url(self):
        """Test that invalid YouTube URL format returns None."""
        url = "https://www.youtube.com/invalid"
        video_id = extract_video_id(url)
        assert video_id is None


class TestGetThumbnailUrl:
    """Test cases for the get_thumbnail_url function."""

    def test_get_thumbnail_url_returns_correct_format(self):
        """Test that thumbnail URL is in the correct format."""
        video_id = "dQw4w9WgXcQ"
        thumbnail_url = get_thumbnail_url(video_id)
        expected_url = "https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"
        assert thumbnail_url == expected_url

    def test_get_thumbnail_url_contains_video_id(self):
        """Test that thumbnail URL contains the video ID."""
        video_id = "dQw4w9WgXcQ"
        thumbnail_url = get_thumbnail_url(video_id)
        assert video_id in thumbnail_url

    def test_get_thumbnail_url_with_different_video_id(self):
        """Test thumbnail URL generation with a different video ID."""
        video_id = "jNQXAC9IVRw"
        thumbnail_url = get_thumbnail_url(video_id)
        expected_url = "https://img.youtube.com/vi/jNQXAC9IVRw/maxresdefault.jpg"
        assert thumbnail_url == expected_url
        assert video_id in thumbnail_url
