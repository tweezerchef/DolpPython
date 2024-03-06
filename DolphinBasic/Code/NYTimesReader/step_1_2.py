import tkinter as tk
import pyttsx3
import speech_recognition as sr
import openai

# Create the window
root = tk.Tk()
root.title("New York Times Top Stories Reader")

# Create the text box
text_box = tk.Text(root)
text_box.pack()

# Create the buttons
record_button = tk.Button(root, text="Record")
send_button = tk.Button(root, text="Send")
record_button.pack()
send_button.pack()

# Initialize the text-to-speech engine
engine = pyttsx3.init()


# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Function to record audio
def record():
    # Stop any existing speech
    engine.stop()

    # Create a recognizer object
    recognizer = sr.Recognizer()

    # Start recording
    with sr.Microphone() as source:
        print("Speak now...")
        audio = recognizer.listen(source)

    # Send the audio to OpenAI API
    client = openai.OpenAI()
    transcription = client.audio.transcriptions.create(model="whisper-1", file=audio)

    # Get the text from the transcription
    response_text = transcription.text

    # Display the text in the text box
    text_box.insert(tk.END, response_text)


# Function to send the text to the OpenAI API
def send():
    pass


# Bind the buttons to the functions
record_button.config(command=record)
send_button.config(command=send)

# Bind the space bar and return key to the record and send functions
root.bind("<space>", lambda event: record())
root.bind("<Return>", lambda event: send())

# Welcome message
speak(
    "Welcome to the New York Times Top Stories Reader. Select from any of the following sections to hear the headlines, arts, automobiles, books/review, business, fashion, food, health, home, insider, magazine, movies, new york region, obituaries, opinion, politics, real estate, science, sports, sunday review, technology, theater, t-magazine, travel, upshot, us, and world."
)

# Start the main loop
root.mainloop()
