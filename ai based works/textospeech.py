import pyttsx3
def saying(t):
    engine = pyttsx3.init()
    print("Your text: ", t)
    engine.say(t)  
    engine.runAndWait()

while True:
    text = input("Enter a text to speak: ")
    saying(text)
