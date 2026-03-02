from clipper import download_video, transcribe_video, create_clips
from scorer import find_viral_moments

def main():
    youtube_url = input("Enter YouTube URL: ").strip()

    print("Downloading video...")
    video_path = download_video(youtube_url)

    print("Transcribing video...")
    segments = transcribe_video(video_path)

    print("Finding viral moments with AI...")
    moments = find_viral_moments(segments)

    print("Creating clips...")
    create_clips(video_path, moments)

    print("Done. Clips saved inside the 'clips' folder.")

if __name__ == "__main__":
    main()
