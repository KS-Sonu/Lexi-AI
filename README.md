# 🚀 LexiAI - Your Personal Voice Assistant

Hey there! 👋 Ever wished for a smart assistant that listens to your voice and handles your daily tasks? Meet **LexiAI**, a fun and powerful voice-controlled AI assistant built in Python! Just say "Lexi" and watch the magic happen. From playing your favorite tunes to fetching weather updates, sending emails, and even chatting with AI – LexiAI has got you covered. No typing required! 🎉

## ✨ What is LexiAI?

LexiAI is like having a super-smart friend in your computer. It's a voice-activated assistant that uses speech recognition to understand your commands and responds with text-to-speech. Powered by Google's Gemini AI, it can answer questions, play music, check the weather, read news, and send emails – all hands-free! Perfect for busy folks who want to multitask without lifting a finger.

Imagine this: You're cooking dinner, and you want to know the weather. Just shout "Lexi, what's the weather in New York?" Boom! Instant update. Or "Lexi, play sapphire" – your playlist starts rolling. It's intuitive, fun, and built for real-life use.

## 🎯 Key Features

LexiAI packs a punch with these awesome capabilities:

- **🎤 Voice Activation**: Wake it up with "Lexi" – no buttons needed!
- **🎵 Music Playback**: Say "play [song name]" to open your favorite tracks on YouTube (from a custom library).
- **🌤️ Weather Updates**: Ask "What's the weather in [city]?" and get real-time info via OpenWeatherMap.
- **📰 News Headlines**: Say "news" to hear the top 5 tech headlines from NewsAPI.
- **📧 Email Sending**: Command "send email to [contact] saying [message]" – emails go out instantly.
- **🤖 AI Chat**: For anything else, LexiAI taps into Gemini AI for smart, conversational responses.
- **📱 WhatsApp Ready**: (Bonus module) Send messages via WhatsApp – integrate it for even more fun!

All wrapped in a sleek, modular Python codebase that's easy to tweak and expand.

## 🛠️ Prerequisites

Before diving in, make sure you have:
- **Python 3.8+** (We recommend 3.10 or higher for best performance).
- A **microphone** (built-in or external) for voice input.
- Internet connection (for APIs and music playback).
- **Windows** (currently optimized for Windows SAPI5 TTS; can be adapted for other OS).

## 📦 Installation

Let's get LexiAI up and running in a few simple steps! We'll use a virtual environment to keep things clean.

1. **Clone the Repo**:
   ```bash
   git clone https://github.com/KS_Sonu/LexiAI.git
   cd LexiAI
   ```

2. **Create a Virtual Environment**:
   - Open VS Code (or your terminal).
   - Press `Ctrl+Shift+P`, type "Create Environment", and select `venv`.
   - Choose Python version and activate it.

3. **Install Packages**:
   Run these commands in your terminal (inside the virtual env):
   ```bash
   pip install speechrecognition pyaudio setuptools pyttsx3 google-generativeai requests pywhatkit python-dotenv
   pip install pipwin  # For Windows audio support
   pipwin install pyaudio
   ```
   - Pro tip: If pyaudio gives trouble, try `pip install PyAudio` or check the [Process step by step.txt](Process%20step%20by%20step.txt) for more tips.

4. **Set Up API Keys** (Super Important! 🔑):
   - LexiAI uses free APIs – but you need your own keys for security.
   - Create a `.env` file in the project root (copy from `.env.example` if provided, or create one).
   - Fill in your keys:
     - **Gemini AI**: Get a key from [Google AI Studio](https://makersuite.google.com/app/apikey).
     - **OpenWeatherMap**: Sign up at [openweathermap.org](https://openweathermap.org/api) for a free key.
     - **NewsAPI**: Grab a key from [newsapi.org](https://newsapi.org).
     - **Gmail (for emails)**: Enable 2FA, generate an App Password in Gmail settings.
     - **WhatsApp (optional)**: No key needed, but ensure pywhatkit is set up.
   - The code loads these from `.env` automatically – never hardcode them!

5. **Customize Contacts & Music**:
   - Edit `contacts.py` for email contacts.
   - Update `contacts.json` for phone numbers (WhatsApp).
   - Add songs to `musiclibrary.py` with YouTube links.

## 🚀 Usage

Ready to chat with LexiAI? Here's how:

1. **Run the Assistant**:
   ```bash
   python Main.py
   ```
   - You'll hear "Initializing Lexi......" – she's waking up!

2. **Activate & Command**:
   - Say **"Lexi"** to wake her up.
   - She'll say "Ya I'm listening. Say 'stop' to end conversation."
   - Now give commands! Examples:
     - "Play sapphire" → Opens the song on YouTube.
     - "What's the weather in London?" → Gets live weather.
     - "News" → Reads top headlines.
     - "Send email to sonu saying Hey buddy!" → Emails your contact.
     - "Who won the last World Cup?" → Gemini AI answers.
   - Say **"stop"** or **"exit"** to end the session.

3. **Test It Out**:
   - Run `python test.py` to check your Gemini API.
   - Use `s.py` for TTS tests if needed.

Pro Tips:
- Speak clearly and close to the mic.
- If speech recognition fails, check your internet or mic settings.
- LexiAI runs in a loop – just keep talking until you say stop!

## 🤝 Contributing

Love LexiAI? Want to add features like voice memos or smart home control? Awesome! Fork the repo, make changes, and submit a pull request. Let's make her even smarter together. 💡

- Report bugs or suggest ideas in Issues.
- Follow the code style: Keep it modular, add comments, and test your changes.

## 📄 License

This project is open-source under the MIT License. Feel free to use, modify, and share – just give credit! 😊

---

Built with ❤️ using Python, speech recognition, and a dash of AI magic. Questions? Open an issue or reach out. Happy assisting! 🎤✨</content>
<parameter name="filePath">d:\DATA ANALYST\Python project.py\LexiAI\README.md