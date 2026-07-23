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

# 

 Installation & Usage

To run this project locally, follow these general steps:

1. Clone this repository to your local machine.
2. Install all required Python dependencies.
3. Install FFmpeg, which is required for audio processing with Whisper.
4. Create a .env file and add your Cohere API key.
5. Run the main application.

Start the project using:
python main.py

Once the application starts, it will listen for voice input through the microphone. The captured speech is converted into text, processed by the AI model, and the generated response is converted back into speech and played to the user. The conversation continues until the user exits the application using one of the supported exit commands.

---

#  Project Demonstration



##### Note

The Arabic text may appear as disconnected characters in the terminal due to the local console's Arabic text rendering. This is only a display issue and does not affect the application's functionality.
---

#  Future Improvements

- Wake-word detection
- Graphical User Interface (GUI)
- Conversation history
- Multiple voice options
- Streaming AI responses
- Offline language model support










