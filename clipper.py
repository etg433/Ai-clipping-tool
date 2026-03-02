import streamlit as st
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

st.title("AI Video Clipper")

# 1. Provide a way to get a file (Upload)
uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    # Save the uploaded file locally so ffmpeg can see it
    with open("temp_video.mp4", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    output = "clipped_video.mp4"
    
    if st.button("Clip Video (10s - 20s)"):
        try:
            # Use 'targetname' for MoviePy 1.0.3
            ffmpeg_extract_subclip("temp_video.mp4", 10, 20, targetname=output)
            
            if os.path.exists(output):
                st.success("Clipping successful!")
                st.video(output)
            else:
                st.error("Output file was not created.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
