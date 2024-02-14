import pyttsx3
engine=pyttsx3.init()
voices = engine.getProperty('voices')

# Print available voices
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)

# Set a specific voice (replace 'your_preferred_voice_id' with the ID of the desired voice)
preferred_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
engine.setProperty('voice', preferred_voice_id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Test the voice
speak(t=input("enter text:"));