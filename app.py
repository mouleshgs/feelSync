import streamlit as st
from utils.audio_recorder import record_audio, save_audio
from utils.transcriber import transcribe_audio
from utils.spotify_api import get_spotify_token, search_playlist_by_genre
from utils.emotion_classifier import get_emotion_classifier, classify_emotion
import os

# Spotify credentials
CLIENT_ID = "c826b12cf2b749ad83a5006cf8919242"
CLIENT_SECRET = "68d9fac62d614e37bcd0083e9375ff7d"

st.title("🎧 FeelSync")

if st.button("Start Recording for 7 seconds"):
    audio, fs = record_audio(duration=7)
    audio_file = save_audio(audio, fs)
    st.success("✅ Recording complete!")

    with st.spinner("📝 Transcribing Tamil audio and translating..."):
        tamil_text, english_text = transcribe_audio(audio_file)
        st.write(f"**Tamil Transcription:** {tamil_text}")
        st.write(f"**English Translation:** {english_text}")

    classifier = get_emotion_classifier()
    emotion_label = classify_emotion(classifier, english_text)
    st.write(f"🎭 **Detected Emotion:** {emotion_label}")

    emotion_to_genre = {
        "positive": "tamil motivation",
        "negative": "tamil sad",
        "neutral": "tamil chill",
        "joy": "tamil feel good",
        "sadness": "tamil sad",
        "anger": "tamil energetic",
        "fear": "tamil chill",
        "surprise": "tamil pop",
    }
    genre = emotion_to_genre.get(emotion_label, "tamil chill")

    with st.spinner("🎵 Searching Spotify playlist..."):
        token = get_spotify_token(CLIENT_ID, CLIENT_SECRET)
        playlist_url = search_playlist_by_genre(genre, token)

    if playlist_url:
        st.markdown(f"### Spotify Playlist for Emotion '{emotion_label}':")
        st.markdown(f"[Open Playlist 🎶]({playlist_url})")
    else:
        st.warning("No playlist found for this emotion.")

    if os.path.exists(audio_file):
        os.remove(audio_file)
