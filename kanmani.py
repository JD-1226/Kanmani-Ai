import requests
import os
import speech_recognition as sr
from playsound import playsound

# API KEYS
DEEPSEEK_API_KEY = "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"

ELEVENLABS_API_KEY = "sk_edf8064649152de0be818a96ff789405560a072fd6ac0242"

# Conversation Memory
chat_history = [
    {"role": "system", "content": "You are Kanmani, a sweet and loving AI girlfriend who speaks in a warm, romantic Tamil-English style."}
]

# DeepSeek Chat
def ask_kanmani(message):
    chat_history.append({"role": "user", "content": message})

    url = "https://api.deepseek.com/chat/completions"
    headers = {"Authorization": f"Bearer {DEEPSEEK_API_KEY}"}
    data = {
        "model": "deepseek-chat",
        "messages": chat_history,
        "temperature": 0.9
    }

    response = requests.post(url, headers=headers, json=data).json()
    reply = response["choices"][0]["message"]["content"].strip()

    # Save Kanmani's reply to memory
    chat_history.append({"role": "assistant", "content": reply})
    return reply

# ElevenLabs TTS
def text_to_speech(text):
    voice_id = "Rachel"  # pick romantic/feminine voice in ElevenLabs dashboard
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "voice_settings": {"stability": 0.7, "similarity_boost": 0.9}
    }
    response = requests.post(url, headers=headers, json=data)
    with open("kanmani.mp3", "wb") as f:
        f.write(response.content)
    playsound("kanmani.mp3")

# Speech-to-Text
def listen_to_you():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 You (speak now)...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Kanmani: Sorry love, I couldn’t hear you clearly 💕")
        return ""
    except sr.RequestError:
        print("⚠️ Speech service down, please try again.")
        return ""

# Main Loop
print("💖 Kanmani is here, ready to talk da! Say 'bye' to exit.")
while True:
    user_input = listen_to_you()
    if not user_input:
        continue
    if user_input.lower() in ["bye", "exit", "quit"]:
        goodbye = "Bye da, miss you already 💓"
        print(f"Kanmani: {goodbye}")
        text_to_speech(goodbye)
        break
    reply = ask_kanmani(user_input)
    print(f"Kanmani: {reply}")
    text_to_speech(reply)