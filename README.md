#  Voice AI Assistant

## Introduction

Voice AI Assistant is a Python-based application that enables users to interact with an AI model through voice commands. The assistant captures the user's speech, converts it into text using OpenAI Whisper, sends the recognized text to Cohere's Large Language Model (LLM) to generate an intelligent response, and finally converts the response back into speech. The application supports both Arabic and English, providing a seamless and interactive conversational experience.

---

#  Libraries Used

The project integrates several Python libraries, each responsible for a specific task:

| Library | Purpose |
|---------|---------|
| SpeechRecognition | Captures audio from the microphone and records the user's speech. |
| OpenAI Whisper | Converts spoken language into text (Speech-to-Text). |
| Cohere | Generates intelligent responses using a Large Language Model (LLM). |
| pyttsx3 | Converts the generated text into speech (Text-to-Speech). |
| python-dotenv | Loads the API key securely from the .env file. |
| PyAudio | Enables microphone input for speech recording. |
| FFmpeg | Processes audio files required by Whisper. |
| Torch | Runs the Whisper speech recognition model. |

---

#  Project Workflow

The project was developed by dividing the application into four Python files, where each file performs a specific task. This modular approach improves readability, simplifies maintenance, and allows each component to be developed independently before integrating them into a complete voice assistant.

### 1. Speech Recognition (`speech_to_text.py`)
The assistant listens through the microphone and converts the user's speech into text using the Whisper model.

### 2. AI Processing (`llm.py`)
The recognized text is sent to Cohere's Large Language Model, which analyzes the request and generates an appropriate response.

### 3. Text-to-Speech (`text_to_speech.py`)
The generated response is converted into speech so the assistant can reply audibly.

### 4. Main Application (`main.py`)
The main file connects all previous modules together. It manages the application's workflow by recording the user's voice, converting it into text, generating an AI response, converting that response into speech, and repeating the process until the user exits the application.

---

#  Installation

### Step 1 – Clone the Repository
git clone https://github.com/YourUsername/Voice-AI-Assistant.git
cd Voice-AI-Assistant

---

### Step 2 – Create a Virtual Environment
python -m venv .venv

Activate it.

Windows
.venv\Scripts\activate

macOS / Linux
source .venv/bin/activate

---

### Step 3 – Install the Required Libraries
pip install -r requirements.txt

---

### Step 4 – Install FFmpeg

Download and install FFmpeg, then add its bin folder to your system PATH.

Verify the installation:
ffmpeg -version

---

### Step 5 – Configure the API Key

Create a .env file and add your Cohere API key.
COHERE_API_KEY=YOUR_API_KEY

---

### Step 6 – Run the Project
python main.py

The assistant will begin listening for voice input. Speak into the microphone, and the assistant will recognize your speech, generate a response, and read it aloud. To stop the application, say "Exit", "Quit", or "خروج".

---

# 🎥 Project Demonstration

> Add your project demonstration video here.


---

#  Future Improvements

- Wake-word detection
- Graphical User Interface (GUI)
- Conversation history
- Multiple voice options
- Streaming AI responses
- Offline language model support










