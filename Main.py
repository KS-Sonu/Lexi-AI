import speech_recognition as sr  # For converting speech to text
import webbrowser  # To open websites in the default browser
import pyttsx3  # For text-to-speech (so Jarvis can talk)
import musiclibrary  # Your custom music file with song names and links
import google.generativeai as genai  # For accessing Gemini AI
import requests # Used to make HTTP requests to the weather API
import json
from email_service import send_email
from contacts import contacts
import re
import pyaudio
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


 
# Initialize the speech recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init(driverName='sapi5')  # Force Windows SAPI5
engine.setProperty('rate', 180)            # Moderate rate
engine.setProperty('volume', 1.0)          # Full volume



# Speak out the given text
def speak(text):
    try:
        print(f"Speaking: {text}")  # Debug output
        # Re-initialize SAPI5 per utterance to avoid the "second line silent" bug
        local_engine = pyttsx3.init('sapi5')
        local_engine.setProperty('rate', 180)
        local_engine.setProperty('volume', 1.0)
        voices = local_engine.getProperty('voices')
        if voices and len(voices) > 0:
            local_engine.setProperty('voice', voices[0].id)  # try voices[1] if needed
        local_engine.say(text)
        local_engine.runAndWait()
        print(f"Finished speaking: {text}")  # Debug output
    except Exception as e:
        print(f"Error in speak function: {e}")
        # Fallback to print if TTS fails
        print(f"Lexi says: {text}")

def listen():
    # Simple listen function using speech_recognition
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Sorry, I did not catch that.")
            return ""
        except sr.RequestError:
            speak("Sorry, I'm having trouble connecting to the speech service.")
            return ""

    


# Function to fetch weather using OpenWeatherMap API
def get_weather(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Setting parameters for the API: city name and API key
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"   
    }

    try:
        # Send a GET request to the weather API
        response = requests.get(base_url, params=params)
        data = response.json()  # Convert the JSON response to a Python dictionary

        # If the response code is 200, it means the request was successful
        if response.status_code == 200:
            city_name = data["name"]
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"]

            # Constructing the result sentence
            weather_report = f"The weather in {city_name} is {weather} with a temperature of {temp}°C."
            return weather_report
        else:
            return "Sorry, I couldn't get the weather info. Please try again."
    except Exception as e:
        return f"Error occurred while fetching weather: {str(e)}"

 # Top 5 News headlines from the browser   
# Function to fetch and speak top 5 news headlines


def get_news():
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/everything?q=technology&sortBy=publishedAt&language=en&apiKey={api_key}"

    try:
        # Sending request to News API
        r = requests.get(url)
        data = r.json()  # Convert JSON response to dictionary

        # Check for success
        if r.status_code == 200 and data["status"] == "ok":
            articles = data.get("articles", [])[:5]  # Get first 5 articles

            if not articles:
                speak("Sorry, I couldn't find any news at the moment.")
                return

            speak("Here are the top 5 news headlines for today.")
            
            for i, article in enumerate(articles, start=1):
                title = article.get("title", "No title available")
                print(f"Headline {i}: {title}")  # Show in terminal
                speak(f"Headline {i}: {title}")  # Speak aloud

        else:
            error_message = data.get("message", "Something went wrong.")
            speak(f"News fetch failed. Reason: {error_message}")

    except Exception as e:
        speak(f"An error occurred while getting news. {str(e)}")

def clean_message(msg):
    # Remove non-printable characters and extra spaces
    msg = msg.replace('\xa0', ' ')  # replace weird non-breaking space
    msg = re.sub(r'[^\x00-\x7F]+', ' ', msg)  # remove other non-ascii
    return msg.strip()

        

# Set Google Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # <- Insert  actual API key here

# Function to ask Gemini AI and get a smart response
def ask_gemini(prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text.strip()  # Return the reply from Gemini

# Process user's voice command
def processcommand(c):
    print(f"Processing command: '{c}'")
    # Test command to verify speech is working
    if "test" in c.lower():
        speak("Test successful! Speech is working.")
        return
    


    # Play song from custom music library
    elif c.lower().startswith("play"):
        try:
            song = c.lower().split(" ")[1]
            if song in musiclibrary.music:
                link = musiclibrary.music[song]
                webbrowser.open(link)
                speak(f"Playing {song}")
            else:
                available_songs = ", ".join(musiclibrary.music.keys())
                speak(f"Sorry, I don't have {song} in my library. Available songs are: {available_songs}")
        except IndexError:
            speak("Please specify which song to play. For example, say 'play saphire'")
        except Exception as e:
            speak(f"Error playing music: {str(e)}")

    elif "weather" in c.lower():
        # Example: "What is the weather in Bangalore?"
        words = c.lower().split("in")
        if len(words) > 1:
            city = words[1].strip()
            weather_info = get_weather(city)
            speak(weather_info)
        else:
            speak("Please tell me the city name.")

    elif "news" in c.lower():
        get_news()

     # Send email feature (modular & clean)
    # Inside processcommand()
    # Send email feature (modular & clean)
    elif "send email to" in c.lower():
        try:
            parts = c.lower().replace("send email to", "").strip().split("saying")
            name = parts[0].strip()
            message = parts[1].strip()

            #  Lookup the email using the name
            if name in contacts:
                to_email = contacts[name]
            else:
                speak("Sorry, I don't know the email address of " + name)
                return

            message = clean_message(message)
            subject = "Message from Lexi"

            success = send_email(to_email, subject, message)
            if success:
                speak("Lexi: Email sent successfully.")
            else:
                speak("Something went wrong while sending the email.")

            speak("Sending this email:")
            speak(message)

        except Exception as e:
            print("Error:", e)
            speak("I couldn't process the email command.")

   

    # For any other question, use Gemini AI
    else:
        answer = ask_gemini(c)
        speak(answer)

# Main function starts here
if __name__ == "__main__":
    print("Starting Lexi...")
    speak("Initializing Lexi......")
    
    while True:
        print("Waiting for wake word 'Lexi'...")
        try:
            with sr.Microphone() as source:
                print("Microphone activated...")
                audio = r.listen(source, timeout=10, phrase_time_limit=15)
                print("Audio captured...")
                
            word = r.recognize_google(audio)
            print(f"Recognized: {word}")

            # If user says "Lexi", activate assistant
            if word and "lexi" in word.lower():
                print("Wake word detected! About to speak...")  # Add this line
                speak("Ya I'm listening. Say 'stop' to end conversation")
                print("Speak function completed!")

                # Keep listening for commands until 'stop' is said
                while True:
                    try:
                        with sr.Microphone() as source:
                            print("Lexi Active - Listening for command...")
                            audio = r.listen(source, timeout=10, phrase_time_limit=20)
                            command = r.recognize_google(audio)
                            print(f"You said: {command}")

                            # End conversation on stop or exit
                            if "stop" in command.lower() or "exit" in command.lower():
                                speak("Conversation ended.")
                                break

                            # Otherwise, process the spoken command
                            processcommand(command)
                    except sr.WaitTimeoutError:
                        print("No command detected.")
                        continue
                    except sr.UnknownValueError:
                        print("Could not understand command.")
                        continue
                    except sr.RequestError as e:
                        print(f"Speech recognition error: {e}")
                        continue
                    except Exception as e:
                        print(f"Error: {e}")
                        continue
                
                print("Exiting command mode, returning to wake word detection...")

        except sr.WaitTimeoutError:
            print("No speech detected.")
            continue
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            continue
        except sr.RequestError as e:
            print(f"Network issue: {e}")
            continue
        except Exception as e:
            print(f"Error: {e}")
            continue
            
