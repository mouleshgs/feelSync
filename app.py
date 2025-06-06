import streamlit as st
from utils.audio_recorder import record_audio, save_audio
from utils.transcriber import transcribe_audio
from utils.spotify_api import get_spotify_token, search_playlist_by_genre
from utils.emotion_classifier import get_emotion_classifier, classify_emotion
import os
from dotenv import load_dotenv

load_dotenv()
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

st.set_page_config(page_title="FeelSync 🎧", layout="centered")



st.markdown("<h1 style='text-align: center; color: #1ED760;'>🎧 FeelSync: Emotion-Based Tamil Music Recommender</h1>", unsafe_allow_html=True)
st.markdown("---")

if st.button("🎙️ Start Recording (7 seconds)"):
    with st.spinner("🔴 Recording in progress... Please speak now"):
        audio, fs = record_audio(duration=7)
        audio_file = save_audio(audio, fs)

    st.success("✅ Recording complete!")
    st.audio(audio_file, format='audio/wav')

    with st.spinner("📝 Transcribing and Translating Tamil to English..."):
        tamil_text, english_text = transcribe_audio(audio_file)

    # Display transcription
    st.markdown("### 🗣️ Transcription Output")
    st.markdown(f"**📝 Tamil Text:** `{tamil_text}`")
    st.markdown(f"**🌍 English Translation:** `{english_text}`")
    st.markdown("---")

    # Emotion detection
    with st.spinner("🎭 Detecting emotion from translated text..."):
        classifier = get_emotion_classifier()
        emotion_label = classify_emotion(classifier, english_text)

    st.markdown(f"### 🎭 Detected Emotion: `{emotion_label.capitalize()}`")

    # Emotion to genre mapping
    emotion_to_genre = {
        "admiration": "tamil feel good", "amusement": "tamil comedy", "anger": "tamil energetic",
        "annoyance": "tamil intense", "approval": "tamil motivation", "caring": "tamil melody",
        "confusion": "tamil chill", "curiosity": "tamil lofi", "desire": "tamil romantic",
        "disappointment": "tamil happy", "disapproval": "tamil dark", "disgust": "tamil intense",
        "embarrassment": "tamil lofi", "excitement": "tamil celebration", "fear": "tamil chill",
        "gratitude": "tamil devotional", "grief": "tamil calm", "joy": "tamil feel good",
        "love": "tamil romantic", "nervousness": "tamil chill", "optimism": "tamil motivation",
        "pride": "tamil anthem", "realization": "tamil melody", "relief": "tamil feel good",
        "remorse": "tamil calm", "sadness": "tamil motivation", "surprise": "tamil pop",
        "neutral": "tamil chill"
    }
    genre = emotion_to_genre.get(emotion_label, "tamil chill")


    # Spotify integration
    with st.spinner("🔍 Searching Spotify for matching playlists..."):
        token = get_spotify_token(CLIENT_ID, CLIENT_SECRET)
    
    
    playlist_url, image_url = search_playlist_by_genre(genre, token)
    
    

    if playlist_url:
        st.markdown("---")
        st.markdown(f"## 🔗 Recommended Playlist for **{emotion_label.capitalize()}** Emotion")
        if image_url:
            st.image(image_url, caption="Playlist Cover", use_column_width=True)
        st.markdown(f"[🎵 Open on Spotify]({playlist_url})", unsafe_allow_html=True)
    else:
        st.warning("⚠️ No playlist found for this emotion on Spotify.")


    # Clean up
    if os.path.exists(audio_file):
        os.remove(audio_file)
