import yt_dlp
import whisper
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def download_video(url):
    ydl_opts = {
        "format": "mp4",
        "outtmpl": "video.mp4"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return "video.mp4"


def transcribe_video(video_path):
    model = whisper.load_model("base")
    result = model.transcribe(video_path)
    return result["segments"]


def create_clips(video_path, moments):
    os.makedirs("clips", exist_ok=True)

    for i, moment in enumerate(moments):
        start = moment["start"]
        end = moment["end"]

        output_path = f"clips/clip_{i+1}.mp4"
        ffmpeg_extract_subclip(video_path, start, end, targetname=output_path)
