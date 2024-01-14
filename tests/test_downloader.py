import pytest
from yt_downloader.downloader import (
    download,
    InvalidFormatException,
)


@pytest.fixture
def tmp_directory(tmp_path):
    return tmp_path


@pytest.mark.parametrize(
    "formatter",
    ["mp4", "mp3"],
)
def test_download_mp4(tmp_directory, formatter):
    url = "https://www.youtube.com/watch?v=R9aMV8QIEB0"
    directory_path = tmp_directory / "test_video"
    formatter = formatter

    download(url, directory_path, formatter)

    assert directory_path.exists()


def test_download_exception(tmp_directory):
    url = "https://www.youtube.com/watch?v=R9aMV8QIEB0"
    directory_path = tmp_directory / "test_video.cda"
    formatter = "cda"

    with pytest.raises(InvalidFormatException) as e:
        download(url, directory_path, formatter)
    assert str(e.value) == "Something has gone wrong: Invalid format"
