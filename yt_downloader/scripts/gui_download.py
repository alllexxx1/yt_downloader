#!/usr/bin/env python3


from yt_downloader.gui_downloader import gui_download
from yt_downloader.downloader import download


def main():
    gui_download(download)


if __name__ == "__main__":
    main()
