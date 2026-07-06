import streamlit as st
from modules.speech_to_text import transcribe_audio

st.set_page_config(page_title="Voice-Based Concept Understanding Analyser")

st.title("🎤 Voice-Based Concept Understanding Analyser")

uploaded_file = st.file_uploader(
    "Upload an audio file",
    type=["wav", "mp3", "m4a"]
)

if uploaded_file:
    with open("uploads/input_audio.wav", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Audio uploaded successfully.")

    if st.button("Transcribe Audio"):
        with st.spinner("Transcribing..."):
            text = transcribe_audio("uploads/input_audio.wav")

        st.subheader("Transcript")
        st.write(text)