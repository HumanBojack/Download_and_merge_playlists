# Download and merge youtube playlists
## Goal
This script (`merge.py`) is used to merge a youtube playlist into a single video file.
It takes as input a **playlist URL** and outputs a **video file**.

## Usage
```
usage: merge.py [-h] -U PLAYLIST_URL [-F DOWNLOAD_FOLDER] [-E OUTPUT_EXTENSION]

options:
  -h, --help            show this help message and exit
  -U PLAYLIST_URL, --playlist-url PLAYLIST_URL
                        Playlist url.
  -F DOWNLOAD_FOLDER, --download-folder DOWNLOAD_FOLDER
                        Folder in which the playlist videos will be saved
  -E OUTPUT_EXTENSION, --output-extension OUTPUT_EXTENSION
                        Extension of the output file
```