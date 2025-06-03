import sounddevice as sd
from scipy.io.wavfile import write


def record_audio(duration=7, fs=16000):
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    return audio, fs

def save_audio(audio, fs, filename="tamil_voice.wav"):
    write(filename, fs, audio)
    return filename
