# NerdBot AI - Voice Assistant

This project is a voice-controlled AI assistant built using Python. It can perform tasks such as answering questions using the Bard API, playing music, opening websites and applications, and providing the current time. It uses speech recognition, text-to-speech, and other Python libraries to enhance its functionality.

## Features

- **Voice Interaction**: Listens to voice commands and executes tasks.
- **Bard API Integration**: Provides answers to user questions.
- **Music Playback**: Plays music from a predefined list.
- **Website Navigation**: Opens websites like Google, YouTube, Instagram, and WhatsApp.
- **Application Launching**: Opens local applications like Spotify, Notepad, and Calculator.
- **Time Announcement**: Provides the current time upon request.

## Prerequisites

- Python 3.x
- Pip package manager

### Python Packages

The following Python packages are required:

- `win32com.client` for text-to-speech.
- `speech_recognition` for voice command recognition.
- `webbrowser` for website navigation.
- `datetime` for time functions.
- `pygame` for playing music.
- `requests` for API communication.
- `retrying` for handling retries in API calls.

Install the necessary packages with the following command:

bash

pip install pywin32 SpeechRecognition pygame requests retrying

**Bard API Key**

Set your Bard API key as an environment variable using the following command:

bash

export BARD_API_KEY=your_bard_api_key

Alternatively, set the key directly in the script:

python
os.environ['BARD_API_KEY'] = "your_bard_api_key"

## Usage
Launch the program: Run the main() function, which initializes the AI assistant.
Voice Commands: Speak commands such as:
"More information" to ask questions using the Bard API.
"Open music" followed by the song name to play predefined songs.
"Open website" followed by a site name like Google or YouTube.
"The time" to get the current time.
"Open" followed by app names like Spotify, Notepad, or Calculator.

**Example Commands**
Ask a Question:
"More information"
Then ask a question like: "What is AI?"
Play Music:
"Open music Malang Sajna"
Open Website:
"Open Google website"
Get Current Time:
"What is the time?"

## Error Handling
The script includes a retry mechanism for API calls using retrying, which retries failed requests up to 3 times with exponential backoff.
Exception handling is added for recognizing voice commands, API responses, and playing music.
Music Files
To add or change the music files, modify the music_paths dictionary with appropriate paths to your music files:

python

music_paths = {
    "Song Name": "C:\\path\\to\\song.mp3",
}

## API Reference

Bard API: The script communicates with the Bard API to fetch answers to user questions. Ensure your API key is valid and set correctly.
