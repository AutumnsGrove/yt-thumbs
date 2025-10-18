"""Command-line interface for YouTube thumbnail extractor."""

import argparse
import sys
from pathlib import Path

from .extractor import extract_video_id, get_thumbnail_url, download_thumbnail


def main() -> None:
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Extract and download YouTube video thumbnails",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s https://www.youtube.com/watch?v=dQw4w9WgXcQ
  %(prog)s https://youtu.be/dQw4w9WgXcQ --download
  %(prog)s https://youtu.be/dQw4w9WgXcQ --download --output my_thumb.jpg
        """,
    )

    parser.add_argument(
        "url",
        help="YouTube video URL",
    )

    parser.add_argument(
        "--download",
        "-d",
        action="store_true",
        help="Download the thumbnail instead of printing the URL",
    )

    parser.add_argument(
        "--output",
        "-o",
        help="Output filename (default: {video_id}.jpg)",
    )

    args = parser.parse_args()

    # Extract video ID from URL
    video_id = extract_video_id(args.url)
    if not video_id:
        print(
            f"Error: Could not extract video ID from URL: {args.url}", file=sys.stderr
        )
        print("Supported formats:", file=sys.stderr)
        print("  - https://www.youtube.com/watch?v=VIDEO_ID", file=sys.stderr)
        print("  - https://youtu.be/VIDEO_ID", file=sys.stderr)
        print("  - https://www.youtube.com/embed/VIDEO_ID", file=sys.stderr)
        sys.exit(1)

    # Get thumbnail URL
    thumbnail_url = get_thumbnail_url(video_id)

    # If download flag is not set, just print the URL
    if not args.download:
        print(thumbnail_url)
        return

    # Download mode
    output_path = args.output if args.output else f"{video_id}.jpg"

    # Create parent directory if it doesn't exist
    output_file = Path(output_path)
    if output_file.parent != Path("."):
        output_file.parent.mkdir(parents=True, exist_ok=True)

    print(f"Downloading thumbnail for video ID: {video_id}")
    print(f"Saving to: {output_path}")

    success = download_thumbnail(video_id, output_path)

    if success:
        print(f"Successfully downloaded thumbnail to {output_path}")
    else:
        print(
            f"Error: Failed to download thumbnail for video ID: {video_id}",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
