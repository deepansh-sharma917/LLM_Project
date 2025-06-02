from ollama_client import query_ollama
from voice import speak, listen

def text_mode():
    print("Welcome to Jarvis CLI. Type 'exit' to quit.")
    while True:
        prompt = input("You: ")
        if prompt.lower() in ["exit", "quit"]:
            print("Jarvis: Goodbye!")
            break
        response = query_ollama(prompt)
        print(f"Jarvis: {response}")

def voice_mode():
    speak("Hello, I am Jarvis. Say something or say exit to quit.")
    while True:
        command = listen()
        print(f"You said: {command}")
        if "exit" in command.lower():
            speak("Goodbye!")
            break
        response = query_ollama(command)
        speak(response)
        print(f"Jarvis: {response}")

if __name__ == "__main__":
    mode = input("Choose mode (text/voice): ").strip().lower()
    if mode == "voice":
        voice_mode()
    else:
        text_mode()
