import streamlit as st
from clipper import download_video, transcribe_video, create_clips
from scorer import find_viral_moments
import os

st.set_page_config(page_title="ClipForge AI", layout="centered")

st.title("🎬 ClipForge AI")
st.write("AI-Powered YouTube Clip Generator (100% Free & Local)")

youtube_url = st.text_input("Paste YouTube URL")

if st.button("Generate Clips"):
    if youtube_url:
        with st.spinner("Downloading video..."):
            video_path = download_video(youtube_url)

        with st.spinner("Transcribing..."):
            segments = transcribe_video(video_path)

        with st.spinner("Finding viral moments..."):
            moments = find_viral_moments(segments)

        with st.spinner("Creating clips..."):
            create_clips(video_path, moments)

        st.success("Clips created!")

        if os.path.exists("clips"):
            for file in os.listdir("clips"):
                st.video(os.path.join("clips", file))
    else:
        st.warning("Please enter a YouTube URL.")
