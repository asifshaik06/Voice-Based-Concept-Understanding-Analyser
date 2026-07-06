import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Voice-Based Concept Understanding Analyser",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 Voice-Based Concept Understanding Analyser (VBCUA)")

st.markdown("""
This application evaluates conceptual understanding using:

- 🎙️ Speech-to-Text
- 🧠 Semantic Similarity
- 📊 Audio Feature Analysis
- 📄 PDF Report Generation
""")

st.divider()

uploaded_file = st.file_uploader(
    "Upload an audio file",
    type=["wav", "mp3", "m4a"]
)

if uploaded_file:
    upload_dir = Path("uploads")
    upload_dir.mkdir(exist_ok=True)

    file_path = upload_dir / uploaded_file.name

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("Audio uploaded successfully!")
    st.audio(str(file_path))

    st.info("Speech-to-Text module will be implemented next.")

st.sidebar.title("Project Progress")

st.sidebar.success("✅ Streamlit UI")
st.sidebar.info("⏳ Speech-to-Text")
st.sidebar.info("⏳ Semantic Similarity")
st.sidebar.info("⏳ Audio Analysis")
st.sidebar.info("⏳ PDF Report")