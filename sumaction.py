import streamlit as st
import os
import tempfile
from sumaction_utils import *


# max file size for Whisper
MAX_FILE_SIZE_MB = 25
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024

# Streamlit App
st.title("SumAction")

# dictionary input field
st.subheader("1. Enter Meeting Participants:")
members_dict_str = st.text_area("Enter participant names and emails as a Python dictionary (e.g., {'Name': 'email@example.com', ...})")

# transcript upload field
st.subheader("2. Upload Meeting File:")
meeting_file = st.file_uploader(f"Upload MP3 or TXT file (Maximum file size: {MAX_FILE_SIZE_MB} MB)", type=["mp3", "txt"])

# Query input field
st.subheader("Ask a Question about the Meeting (Optional):")
query = st.text_input("Your question:")
# Query input button
query_button = st.button("Ask")

# Runs query LLM
if query_button and meeting_file:
    if meeting_file.size > MAX_FILE_SIZE_BYTES:
        st.error(f"File size exceeds the maximum allowed size of {MAX_FILE_SIZE_MB}MB. Please upload a smaller file.")
        meeting_file = None
    elif meeting_file.type == "text/plain":
        transcript = meeting_file.read().decode("utf-8")
        query_response = query_gpt4(transcript, query)
        st.info(query_response)
    elif meeting_file.type == "audio/mpeg":
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(meeting_file.read())
            audio_path = tmp_file.name
        transcript = whisper_transcribe(audio_path)
        os.remove(audio_path)
        query_response = query_gpt4(transcript, query)
        st.info(query_response)
    else:
        st.error("Unsupported file type for querying.")
elif query_button and not meeting_file:
    st.warning("Please upload a meeting file to ask a question.")

# Process and send emails button
st.subheader("Process Meeting and Send Emails:")
process_button = st.button("Process Meeting and Send Emails")

# Runs processing and sends emails
if process_button and members_dict_str and meeting_file:
    try:
        names_dict = eval(members_dict_str)
        if not isinstance(names_dict, dict):
            st.error("Invalid format for participants dictionary.")
        else:
            with st.spinner("Processing meeting and generating emails..."):
                if meeting_file.type == "text/plain":
                    transcript = meeting_file.read().decode("utf-8")
                    main(transcript, names_dict)
                elif meeting_file.type == "audio/mpeg":
                    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                        tmp_file.write(meeting_file.read())
                        audio_path = tmp_file.name
                    transcript = whisper_transcribe(audio_path)
                    os.remove(audio_path)
                    main(transcript, names_dict)
                else:
                    st.error("Unsupported file type for processing.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
elif process_button:
    if not members_dict_str:
        st.warning("Please enter the meeting participants.")
    if not meeting_file:
        st.warning("Please upload a meeting file.")