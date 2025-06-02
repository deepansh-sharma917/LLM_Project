# Local Voice-Activated Virtual Assistant using Phi-3 and Ollama
A simple, privacy-friendly voice assistant powered by the Phi-3 large language model served via Ollama, capable of listening to your voice, understanding prompts, and responding naturally — all running locally.

🔧 Features
🎤 Voice Input: Uses your microphone to listen for spoken commands.

🧠 LLM-Powered: Sends prompts to Phi-3 via Ollama’s local REST API for intelligent responses.

🔊 Voice Output: Converts the assistant's response to speech using pyttsx3.

🔐 Privacy-First: No cloud calls — all processing happens locally.

🔁 Modular Design: Clean separation of logic into main.py, voice.py, and LLM interaction components.

📦 Technologies Used
Ollama – Local LLM serving platform

Phi-3 – Lightweight open-source large language model by Microsoft

Python – Core programming language

SpeechRecognition – For converting voice to text

pyttsx3 – For converting text to voice

Requests – For making REST API calls to Ollama

🚀 How It Works
Voice Input – Your microphone input is captured using SpeechRecognition.

LLM Query – The spoken text is sent to Phi-3 running locally via Ollama using a POST request.

Response Handling – The LLM response is returned and spoken aloud using pyttsx3.

