import streamlit as st
import os
import tempfile
import ffmpeg
from pydub import AudioSegment

# --- Streamlit Page Setup ---
st.set_page_config(page_title="Free Viral Clipper", page_icon="✂️", layout="centered")

st.title("✂️ Free Viral Clipper (No API)")
st.markdown("Upload a video! This tool scans the audio wave to find the highest-energy 30 seconds (loudest reactions, laughs, or arguments) and clips it automatically.")

# --- Core Functions ---
def extract_audio(video_path, audio_path):
    """Extracts audio as a WAV file so we can analyze the soundwaves."""
    try:
        # Convert to a simple WAV format for easy reading
        ffmpeg.input(video_path).output(audio_path, acodec='pcm_s16le', ac=1, ar='16000', loglevel="quiet").run(overwrite_output=True)
        return True
    except ffmpeg.Error as e:
        st.error(f"FFmpeg Error extracting audio. Details: {e}")
        return False

def find_highest_energy_moment(audio_path, clip_duration=30):
    """Scans the audio to find the 30-second window with the most energy/loudness."""
    audio = AudioSegment.from_wav(audio_path)
    
    # Break audio into 1-second chunks
    chunk_length_ms = 1000 
    chunks = [audio[i:i+chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]
    
    # Get the "loudness" (Root Mean Square) of each second
    rms_values = [chunk.rms for chunk in chunks]
    
    max_energy = 0
    best_start_sec = 0
    
    # Fallback: If video is shorter than the clip duration, just return the whole video length
    if len(rms_values) <= clip_duration:
        return 0, len(rms_values)
    
    # Slide a 30-second window across the video to find the loudest part
    for i in range(len(rms_values) - clip_duration):
        window_energy = sum(rms_values[i:i+clip_duration]) / clip_duration
        if window_energy > max_energy:
            max_energy = window_energy
            best_start_sec = i
            
    return best_start_sec, best_start_sec + clip_duration

def cut_video(video_path, output_path, start_time, end_time):
    """Cuts the video using FFmpeg based on timestamps."""
    try:
        ffmpeg.input(video_path, ss=start_time, to=end_time).output(output_path, c="copy", loglevel="quiet").run(overwrite_output=True)
        return True
    except ffmpeg.Error as e:
        st.error(f"FFmpeg Error cutting video. Details: {e}")
        return False

# --- App UI & Logic Flow ---
uploaded_video = st.file_uploader("Upload a video file (MP4, MOV)", type=["mp4", "mov", "webm"])

if uploaded_video is not None:
    st.video(uploaded_video)
    
    if st.button("🚀 Find the Loudest/Viral Moment", use_container_width=True):
        with st.spinner("Scanning audio waves..."):
            
            # 1. Create temporary files
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
                temp_video.write(uploaded_video.read())
                temp_video_path = temp_video.name
            
            temp_audio_path = temp_video_path.replace(".mp4", ".wav")
            output_clip_path = temp_video_path.replace(".mp4", "_clip.mp4")

            try:
                # 2. Extract Audio
                with st.status("Extracting audio track..."):
                    success = extract_audio(temp_video_path, temp_audio_path)
                
                if success:
                    # 3. Analyze Audio Waves (NO API!)
                    with st.status("Scanning for peak energy and laughter..."):
                        start_ts, end_ts = find_highest_energy_moment(temp_audio_path, clip_duration=30)
                        st.success(f"High-energy moment found: {start_ts}s to {end_ts}s!")
                    
                    # 4. Cut Final Video
                    with st.status("Clipping the final video..."):
                        cut_success = cut_video(temp_video_path, output_clip_path, start_ts, end_ts)
                    
                    # 5. Display Output
                    if cut_success:
                        st.balloons()
                        st.markdown("### 🎉 Your Clip is Ready!")
                        st.video(output_clip_path)
                        
                        with open(output_clip_path, "rb") as file:
                            st.download_button(
                                label="⬇️ Download Clip to Camera Roll",
                                data=file,
                                file_name="high_energy_clip.mp4",
                                mime="video/mp4",
                                use_container_width=True
                            )
            
            except Exception as e:
                st.error(f"An unexpected error occurred: {str(e)}")
                
            finally:
                # 6. Clean up temporary files
                for path in [temp_video_path, temp_audio_path, output_clip_path]:
                    if os.path.exists(path):
                        try:
                            os.remove(path)
                        except:
                            pass