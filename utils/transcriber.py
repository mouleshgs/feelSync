import subprocess
from googletrans import Translator
import os

def transcribe_audio(filename):
    # Get absolute path and folder of the audio file
    abs_path = os.path.abspath(filename)
    folder = os.path.dirname(abs_path)
    base_filename = os.path.basename(filename)

    # Run whisper CLI with working directory set to audio file folder
    subprocess.run([
        "whisper", base_filename,
        "--language", "ta",
        "--model", "large"
    ], cwd=folder, check=True)

    # Build path to the generated text file
    text_filename = os.path.join(folder, os.path.splitext(base_filename)[0] + ".txt")

    # Read the transcription text
    with open(text_filename, "r", encoding="utf-8") as f:
        tamil_text = f.read()

    # Translate to English
    translator = Translator()
    translated = translator.translate(tamil_text, src='ta', dest='en')

    return tamil_text, translated.text
