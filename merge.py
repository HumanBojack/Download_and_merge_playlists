import ssl
from tqdm import tqdm
from moviepy.editor import VideoFileClip, concatenate_videoclips
from pytube.contrib.playlist import Playlist

ssl._create_default_https_context = ssl._create_unverified_context

playlist = Playlist("https://www.youtube.com/playlist?list=PLfiMjLyNWxeaQQjpPhk7FlbMZtD56RUyX")
download_folder = "/Users/rom1/Documents/VSCode/merge_videos/tmp"

video_files = []
for video in tqdm(playlist.videos):
    stream = video.streams.filter(progressive=True).get_highest_resolution()
    stream.download(download_folder)
    file = f"{download_folder}/{stream.default_filename}"

    vfc = VideoFileClip(file)
    video_files.append(vfc)

output = concatenate_videoclips(video_files)
output.write_videofile(f"{playlist.title}.mp4")