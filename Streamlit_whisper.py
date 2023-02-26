import streamlit as st
import whisper

st.title("Transcription App")

# upload audio file with streamlit
audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3", "m4a", "mp4"])

model = whisper.load_model("base")
st.text("Whisper Model Loaded")

if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcribe Audio")
        transcription = model.transcribe(audio_file.name)
        st.sidebar.success("Transcription Complete")
        st.markdown(transcription["text"])

        # add download button
        download_button_str = f"Download Transcription as Text File"
        download_file_name = f"{audio_file.name}_transcription.txt"
        st.download_button(
            label=download_button_str,
            data=transcription["text"],
            file_name=download_file_name,
            mime="text/plain",
        )
    else:
        st.sidebar.error("Please upload an audio file")

st.sidebar.header("Play Original Audio File")
st.sidebar.audio(audio_file)


