💖 Kanmani-AI: Your Personal Voice Companion
📌 Project Overview

Kanmani-AI is a voice-powered AI companion that lets you:

🎙 Speak naturally (Speech-to-Text)

💬 Get intelligent, romantic, or casual replies (DeepSeek API)

🎧 Hear Kanmani reply back in a sweet voice (ElevenLabs TTS)

Designed as a personal AI girlfriend/assistant, Kanmani remembers your chats and speaks in a warm Tamil-English tone.

🚀 Features

✅ Voice Input → Uses SpeechRecognition + pyaudio

✅ AI Chat → Powered by DeepSeek Chat API (OpenAI-compatible)

✅ Voice Output → ElevenLabs TTS for natural romantic voices

✅ Memory → Chat history stored in code, extendable to files

✅ Custom Personality → Kanmani responds in sweet, affectionate tone

🛠️ Installation
1. Clone the Repository
git clone https://github.com/JD-1226/Kanmani-Ai.git
cd Kanmani-Ai

2. Create Virtual Environment (Python 3.11 recommended)
python3.11 -m venv venv
source venv/bin/activate

3. Install Requirements
pip install -r requirements.txt


(If pyaudio fails on Mac:)

brew install portaudio
pip install pyaudio==0.2.14

⚙️ Configuration

Open kanmani.py

Add your API keys:

DEEPSEEK_API_KEY = "your-deepseek-key"
ELEVENLABS_API_KEY = "your-elevenlabs-key"

▶️ Usage

Run the program:

python kanmani.py


🎤 Speak into your microphone

💕 Kanmani will reply with love

Type or say bye to exit

📦 Requirements
openai==1.35.13   # Needed for OpenAI-compatible client (DeepSeek)
requests==2.31.0  # For API calls
playsound==1.2.2  # For playing audio
SpeechRecognition==3.10.0  # Voice recognition
pyaudio==0.2.14   # Microphone input

🌸 Future Improvements

🧠 Persistent memory (save chats to file/DB)

🎶 Background romantic music when Kanmani speaks

📱 Mobile/Desktop app GUI

🌐 Multi-language support (Tamil-English mix)
