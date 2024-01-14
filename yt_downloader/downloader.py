from pytube import YouTube


def download(url, directory_path, formatter):
    try:
        yt = YouTube(url)
        print(f'Title: {yt.title}')
        print(f'Views: {yt.views}')
        print(f'Length: {yt.length} sec')
        print(f'Media download format: {formatter}')

        media = make_media(yt, formatter)
        media.download(directory_path)

    except Exception as e:
        print('Something has gone wrong: ', str(e))


def make_media(yt, formatter):
    if formatter == 'mp4':
        return yt.streams.get_highest_resolution()
    elif formatter == 'mp3':
        return yt.streams.get_audio_only()
    else:
        raise Exception('Invalid format')
