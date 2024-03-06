import tkinter as tk
from tkinter import scrolledtext
import pyttsx3
import threading
import sounddevice as sd
from scipy.io.wavfile import write
import tempfile
import openai
import os


# Replace 'your_openai_api_key' with your actual OpenAI API key
openai.api_key = "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"

# Text-to-speech engine initialization
engine = pyttsx3.init()


def speak(text):
    """Function to speak text."""
    engine.say(text)
    engine.runAndWait()


def welcome_message():
    """Speak the welcome message using pyttsx3."""
    text = "Welcome to the New York Times Top Stories Reader. Select from any of the following sections to hear the headlines: arts, automobiles, books/review, business, fashion, food, health, home, insider, magazine, movies, new york region, obituaries, opinion, politics, real estate, science, sports, sunday review, technology, theater, t-magazine, travel, upshot, us, and world."
    threading.Thread(target=lambda: speak(text)).start()


def record_audio(duration=5, fs=44100):
    """Record audio with the given duration and sample rate."""
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype="float32")
    sd.wait()  # Wait until recording is finished
    return recording, fs


def save_temporary_audio_file(recording, fs):
    """Save the recording to a temporary WAV file and return its path."""
    tmp_file = tempfile.mktemp(suffix=".wav")
    write(tmp_file, fs, recording)  # Save as WAV file
    return tmp_file


def transcribe_audio(file_path):
    """Transcribe the given audio file using OpenAI's Whisper model."""
    response = openai.Audio.create(file=open(file_path, "rb"), model="whisper-1")
    return response["data"]["text"]


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("NYT Top Stories Reader")
        self.geometry("800x600")
        self.create_widgets()
        welcome_message()

    def create_widgets(self):
        self.text_box = scrolledtext.ScrolledText(
            self, wrap=tk.WORD, width=70, height=20
        )
        self.text_box.pack(pady=20)

        self.record_button = tk.Button(self, text="Record", command=self.on_record)
        self.send_button = tk.Button(self, text="Send", command=self.on_send)

        self.record_button.pack(side=tk.LEFT, padx=(100, 20), pady=20)
        self.send_button.pack(side=tk.RIGHT, padx=(20, 100), pady=20)

    def on_record(self):
        """Handle audio recording."""
        self.text_box.insert(tk.END, "\nRecording... Please speak.")
        recording, fs = record_audio(duration=5)
        self.temp_audio_file = save_temporary_audio_file(recording, fs)
        self.text_box.insert(tk.END, "\nRecording stopped and saved.")

    def on_send(self):
        """Transcribe the recorded audio and display the transcription."""
        if hasattr(self, "temp_audio_file"):
            self.text_box.insert(tk.END, "\nTranscribing audio...")
            try:
                transcription = transcribe_audio(self.temp_audio_file)
                self.text_box.insert(tk.END, f"\nTranscription: {transcription}")
            except Exception as e:
                self.text_box.insert(tk.END, f"\nFailed to transcribe audio: {e}")
            finally:
                os.remove(self.temp_audio_file)  # Clean up the temporary file
        else:
            self.text_box.insert(tk.END, "\nPlease record audio first.")


if __name__ == "__main__":
    app = Application()
    app.mainloop()
