import tkinter as tk
import pyttsx3
from openai import OpenAI

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Create main window
root = tk.Tk()
root.title("New York Times Top Stories Reader")

# Create text box for input/output
text_box = tk.Text(root)
text_box.pack()

# Create buttons
record_button = tk.Button(root, text="Record", command=lambda: record())
send_button = tk.Button(root, text="Send", command=lambda: send())
record_button.pack()
send_button.pack()

# Initialize variables
recording = False
response_text = ""


# Function to start/stop recording
def record():
    global recording
    if not recording:
        recording = True
        # Start recording audio
    else:
        recording = False
        # Stop recording audio


# Function to send recorded audio to OpenAI API
def send():
    global response_text
    # Send audio to OpenAI API
    # Replace "audio.mp3" with the file path of the recorded audio
    client = OpenAI(api_key="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 ")
    audio_file = open("audio.mp3", "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", file=audio_file
    )
    response_text = transcription.text
    # Display response in text box
    text_box.insert(tk.END, response_text)


# Speak initial message when window opens
def welcome_message():
    engine.say(
        "Welcome to the New York Times Top Stories Reader. Select from any of the following sections to hear the headlines, arts, automobiles, books/review, business, fashion, food, health, home, insider, magazine, movies, new york region, obituaries, opinion, politics, real estate, science, sports, sunday review, technology, theater, t-magazine, travel, upshot, us, and world."
    )
    engine.runAndWait()


# Bind spacebar to record function
root.bind("<space>", lambda event: record())

# Bind return key to send function
root.bind("<Return>", lambda event: send())

# Display welcome message on window open
welcome_message()

# Start main loop
root.mainloop()
