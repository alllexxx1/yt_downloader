#!/usr/bin/env python3


from yt_downloader.downloader import download
from yt_downloader.arg_parser import parse_args


def main():
    args = parse_args()
    download(
        args.video_url,
        args.directory_path,
        args.format,
    )


if __name__ == "__main__":
    main()
