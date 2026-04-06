import pyttsx3, time
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 180)
engine.setProperty('volume', 1.0)

engine.startLoop(False)   # non-blocking loop

def speak(t):
    engine.say(t)
    engine.iterate()      # pump engine; may call iterate multiple times
    engine.runAndWait()   # still fine to use; try both with/without iterate

speak("Loop test one")
time.sleep(0.2)
speak("Loop test two")

engine.endLoop()