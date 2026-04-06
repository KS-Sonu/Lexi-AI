# whatsapp_bot.py
# type: ignore
import pywhatkit as kit

import datetime

def send_whatsapp_message(number, message):
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute + 2  # give 2 min buffer

    try:
        kit.sendwhatmsg(number, message, hour, minute)
        print("Message scheduled successfully.")
    except Exception as e:
        print(f"Error sending message: {e}")
