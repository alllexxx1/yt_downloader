import argparse
from dotenv import (
    load_dotenv,
)
import os


load_dotenv()
DIRECTORY_PATH = os.getenv("DIRECTORY_PATH")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Download content stored on YouTube in mp4/mp3 format."
    )

    parser.add_argument("video_url")
    parser.add_argument(
        "-d",
        "--directory_path",
        default=DIRECTORY_PATH,
        help="choose a directory to save a piece of media "
        "or specify directory path through the .env file",
    )
    parser.add_argument(
        "-f",
        "--format",
        choices=["mp4", "mp3"],
        default="mp4",
        help="set format of video downloading " "(default format: mp4)",
    )
    args = parser.parse_args()
    return args
