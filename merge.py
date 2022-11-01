import os
import ssl
from tqdm import tqdm
from moviepy.editor import VideoFileClip, concatenate_videoclips
from pytube.contrib.playlist import Playlist
from argparse import ArgumentParser

ssl._create_default_https_context = ssl._create_unverified_context

def download_and_merge(playlist_url, download_folder, output_extension):
    os.makedirs(download_folder, exist_ok=True)
    playlist = Playlist(playlist_url)
    video_files = []

    i = 0
    for video in tqdm(playlist.videos):
        stream = video.streams.filter(progressive=True).get_highest_resolution()
        stream.download(download_folder)
        file = f"{download_folder}/{stream.default_filename}"

        vfc = VideoFileClip(file)
        video_files.append(vfc)

    output = concatenate_videoclips(video_files)
    output.write_videofile(f"{playlist.title}.{output_extension}")

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-U", "--playlist-url", help="Playlist url.", required=True)
    parser.add_argument("-F", "--download-folder", help="Folder in which the playlist videos will be saved", default="./tmp")
    parser.add_argument("-E", "--output-extension", help="Extension of the output file", default="mp4")

    args = parser.parse_args()
    download_and_merge(**vars(args))