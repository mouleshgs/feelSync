# FeelSync 

**Emotion-Based Tamil Song Recommender using Voice Input**

FeelSync is an innovative AI-powered application that analyzes your emotions through Tamil voice input and recommends personalized Tamil music playlists from Spotify. The system combines advanced speech recognition, natural language processing, and emotion detection to create a seamless music discovery experience.

## Features

- **Voice Input Recording**: Records 7-second Tamil audio clips using your microphone
- **Speech-to-Text Transcription**: Converts Tamil speech to text using OpenAI's Whisper model
- **Language Translation**: Translates Tamil text to English for emotion analysis
- **Emotion Detection**: Analyzes emotional sentiment using RoBERTa-based transformer models
- **Smart Music Matching**: Maps detected emotions to appropriate Tamil music genres
- **Spotify Integration**: Searches and recommends relevant Tamil playlists from Spotify
- **User-Friendly Interface**: Clean and intuitive Streamlit web application

## Technology Stack

### Core Technologies
- **Python**: Primary programming language
- **Streamlit**: Web application framework
- **OpenAI Whisper**: Advanced speech recognition model (large variant)
- **Hugging Face Transformers**: RoBERTa-based emotion classification
- **Spotify Web API**: Music playlist search and retrieval
- **Google Translate API**: Tamil to English translation

### Key Libraries
- `whisper`: Speech-to-text transcription
- `transformers`: Emotion classification using SamLowe/roberta-base-go_emotions model
- `sounddevice`: Audio recording functionality
- `googletrans`: Language translation services
- `requests`: HTTP API communication
- `scipy`: Audio file processing
- `streamlit`: Web interface development

## Requirements

All dependencies are listed in `requirements.txt`. Key requirements include:

```
streamlit==1.45.1
whisper==1.1.10
transformers==4.52.4
googletrans==4.0.0rc1
sounddevice==0.5.2
torch==2.7.0
tensorflow==2.19.0
scipy==1.15.3
python-dotenv==1.1.0
```

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/mouleshgs/feelSync.git
cd feelSync
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Spotify API Configuration
1. Create a Spotify Developer account at [https://developer.spotify.com/](https://developer.spotify.com/)
2. Create a new application in the Spotify Dashboard
3. Copy your Client ID and Client Secret
4. Set up Streamlit secrets by creating `.streamlit/secrets.toml`:

```toml
[spotify]
client_id = "your_spotify_client_id"
client_secret = "your_spotify_client_secret"
```

### 4. Run the Application
```bash
streamlit run app.py
```

## How It Works

### 1. Voice Input Processing
- User clicks the recording button to capture 7 seconds of Tamil speech
- Audio is recorded at 16kHz sample rate using `sounddevice`
- Recorded audio is temporarily saved as a WAV file

### 2. Speech Recognition & Translation
- **Whisper Large Model** transcribes Tamil audio to Tamil text
- **Google Translate API** converts Tamil text to English for emotion processing
- Both original Tamil and translated English text are displayed

### 3. Emotion Analysis
- **RoBERTa-based classifier** (`SamLowe/roberta-base-go_emotions`) analyzes English text
- Detects emotions from 27+ categories including joy, sadness, anger, love, etc.
- Returns the most confident emotion prediction

### 4. Music Genre Mapping
The system maps detected emotions to Tamil music genres:

```python
emotion_to_genre = {
    "joy": "tamil feel good",
    "love": "tamil romantic", 
    "sadness": "tamil motivation",
    "anger": "tamil energetic",
    "excitement": "tamil celebration",
    "gratitude": "tamil devotional",
    # ... and more mappings
}
```

### 5. Spotify Playlist Recommendation
- Generates Spotify API access token using Client Credentials flow
- Searches for Tamil playlists matching the detected emotion genre
- Returns playlist URL and cover image for user interaction

## Project Structure

```
feelSync/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── .gitignore                 # Git ignore rules
├── README.md                  # Project documentation
└── utils/                     # Utility modules
    ├── audio_recorder.py      # Audio recording functionality
    ├── transcriber.py         # Speech-to-text processing
    ├── emotion_classifier.py  # Emotion detection
    └── spotify_api.py         # Spotify API integration
```

## Supported Emotions

The system recognizes 27+ emotions including:
- **Positive**: Joy, Love, Excitement, Gratitude, Optimism, Pride
- **Negative**: Sadness, Anger, Fear, Disgust, Disappointment, Grief
- **Complex**: Curiosity, Surprise, Nervousness, Embarrassment, Confusion
- **Social**: Caring, Admiration, Approval, Disapproval

## Music Genre Categories

Tamil music genres mapped to emotions:
- **Feel Good**: Joy, Relief, Gratitude
- **Romantic**: Love, Desire
- **Energetic**: Anger, Excitement
- **Motivation**: Sadness, Approval, Optimism
- **Devotional**: Gratitude
- **Chill**: Confusion, Fear, Nervousness
- **Celebration**: Excitement
- **Calm**: Grief, Remorse

## API Integration

### Spotify Web API
- **Authentication**: Client Credentials OAuth flow
- **Endpoint**: Search API for playlist discovery
- **Parameters**: Genre-based query with Tamil language focus
- **Response**: Playlist metadata, URLs, and cover images

### Whisper API
- **Model**: Large variant for high accuracy
- **Language**: Tamil (ta) specification
- **Output**: Text transcription files

## Usage Instructions

1. **Start the Application**: Run `streamlit run app.py`
2. **Record Audio**: Click "🎙️ Start Recording" and speak in Tamil for 7 seconds
3. **View Transcription**: See both Tamil and English text output
4. **Emotion Detection**: Review the detected emotion category
5. **Music Recommendation**: Click the Spotify playlist link to start listening

## Privacy & Security

- **Temporary Audio Storage**: Audio files are automatically deleted after processing
- **No Data Persistence**: Voice recordings are not permanently stored
- **API Security**: Spotify credentials are managed through Streamlit secrets
- **Local Processing**: Most processing happens locally except for API calls


## Links

- **Repository**: [https://github.com/mouleshgs/feelSync](https://github.com/mouleshgs/feelSync)
- **Spotify Developer**: [https://developer.spotify.com/](https://developer.spotify.com/)
- **Whisper Documentation**: [https://openai.com/research/whisper](https://openai.com/research/whisper)

