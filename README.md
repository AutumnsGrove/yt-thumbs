# yt-thumbs

[![Tests](https://github.com/AutumnsGrove/yt-thumbs/actions/workflows/test.yml/badge.svg)](https://github.com/AutumnsGrove/yt-thumbs/actions/workflows/test.yml)
[![PyPI version](https://badge.fury.io/py/yt-thumbs.svg)](https://badge.fury.io/py/yt-thumbs)
[![Python versions](https://img.shields.io/pypi/pyversions/yt-thumbs.svg)](https://pypi.org/project/yt-thumbs/)
[![codecov](https://codecov.io/gh/AutumnsGrove/yt-thumbs/branch/main/graph/badge.svg)](https://codecov.io/gh/AutumnsGrove/yt-thumbs)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

YouTube thumbnail extractor. Zero dependencies.

## Features

- Extract thumbnail URLs from YouTube videos
- Download thumbnails in highest available quality
- Automatically falls back from maxresdefault (1280x720) to hqdefault if unavailable
- Zero external dependencies (uses only Python standard library)
- Lightning-fast performance
- Support for all common YouTube URL formats

## Installation

### Using UV Tool (Recommended)

Install as a UV tool for global access:

```bash
uv tool install yt-thumbs
```

Or install from source:

```bash
git clone https://github.com/yourusername/yt-thumbs.git
cd yt-thumbs
uv tool install .
```

### Using pip

```bash
pip install yt-thumbs
```

## Usage

### Get Thumbnail URL (Default)

Simply print the thumbnail URL to stdout:

```bash
yt-thumbs https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

Output:
```
https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg
```

### Download Thumbnail

Download the thumbnail image to disk:

```bash
yt-thumbs https://www.youtube.com/watch?v=dQw4w9WgXcQ --download
```

This saves the thumbnail as `dQw4w9WgXcQ.jpg` in the current directory.

### Custom Output Filename

Specify a custom filename for the downloaded thumbnail:

```bash
yt-thumbs https://www.youtube.com/watch?v=dQw4w9WgXcQ --download --output my-thumbnail.jpg
```

### Supported URL Formats

All common YouTube URL formats are supported:

```bash
# Standard watch URL
yt-thumbs https://www.youtube.com/watch?v=dQw4w9WgXcQ

# Short URL
yt-thumbs https://youtu.be/dQw4w9WgXcQ

# Embed URL
yt-thumbs https://www.youtube.com/embed/dQw4w9WgXcQ

# URLs without protocol (http/https)
yt-thumbs youtube.com/watch?v=dQw4w9WgXcQ
```

## CLI Options

```
usage: yt-thumbs [-h] [--download] [--output OUTPUT] url

Extract YouTube thumbnail URLs and download thumbnails

positional arguments:
  url                   YouTube video URL

options:
  -h, --help            show this help message
  --download, -d        Download the thumbnail instead of printing URL
  --output OUTPUT, -o OUTPUT
                        Output filename (default: {video_id}.jpg)
```

## Batch Mode

Process multiple URLs and get a markdown table with video metadata:

```bash
# Create a file with URLs (one per line)
cat > urls.txt <<EOF
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://youtu.be/wiTbtugbhgw
EOF

# Process all URLs and output markdown table
yt-thumbs --batch urls.txt

# Or save to a file
yt-thumbs --batch urls.txt --output results.md
```

Output format:
```markdown
| Thumbnail URL | Video Name | Video Description |
|---------------|------------|-------------------|
| https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg | Rick Astley - Never Gonna Give You Up | The official video for "Never Gonna Give You Up"... |
```

## Examples

### Piping URL to clipboard (macOS)

```bash
yt-thumbs https://youtu.be/dQw4w9WgXcQ | pbcopy
```

### Batch download multiple thumbnails

```bash
cat video_urls.txt | while read url; do
  yt-thumbs "$url" --download
done
```

### Download with custom naming

```bash
yt-thumbs https://youtu.be/dQw4w9WgXcQ --download --output thumbnails/rick-roll.jpg
```

## How It Works

YouTube provides thumbnail images at predictable URLs based on the video ID. This tool:

1. Extracts the video ID from any YouTube URL format
2. Constructs the thumbnail URL (tries maxresdefault first)
3. If downloading, attempts to fetch maxresdefault (1280x720)
4. Falls back to hqdefault (480x360) if maxresdefault is unavailable
5. Saves the image to the specified location

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/yt-thumbs.git
cd yt-thumbs

# Install in development mode
uv pip install -e .
```

### Running Tests

```bash
# Run tests with coverage
uv run pytest --cov=src/yt_thumbs --cov-report=term-missing

# Or with dev dependencies installed
pytest
```

### Code Quality

```bash
# Linting
ruff check src tests

# Format checking
ruff format --check src tests

# Format code
ruff format src tests

# Type checking
mypy src/yt_thumbs --strict
```

## Requirements

- Python 3.10 or higher
- No external dependencies (uses standard library only)

## License

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Why yt-thumbs?

- **Fast**: No heavy dependencies like yt-dlp or pytube
- **Simple**: One command to get what you need
- **Reliable**: Uses YouTube's official thumbnail URLs
- **Lightweight**: Pure Python with standard library only
- **Flexible**: Get URLs or download files
