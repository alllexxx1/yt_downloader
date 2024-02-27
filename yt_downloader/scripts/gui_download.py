#!/usr/bin/env python3


from yt_downloader.gui_downloader import gui_download
from yt_downloader.downloader import download
from sys import argv


def main():
    try:
        if argv[1]:
            gui_download(download, theme=argv[1])
    except IndexError:
        print("Theme hasn't been specified. By-default theme will be applied")
        gui_download(download)


if __name__ == "__main__":
    main()
