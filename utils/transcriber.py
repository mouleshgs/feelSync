import subprocess
from googletrans import Translator
import os

def transcribe_audio(filename):
    abs_path = os.path.abspath(filename)
    folder = os.path.dirname(abs_path)
    base_filename = os.path.basename(filename)

    subprocess.run([
        "whisper", base_filename,
        "--language", "ta",
        "--model", "large"
    ], cwd=folder, check=True)

    text_filename = os.path.join(folder, os.path.splitext(base_filename)[0] + ".txt")

    with open(text_filename, "r", encoding="utf-8") as f:
        tamil_text = f.read()

    translator = Translator()
    translated = translator.translate(tamil_text, src='ta', dest='en')

    return tamil_text, translated.text
