import pyttsx3 as p
engine = p.init('sapi5')
engine.say("Hello world This is jarvis speaking ")
engine.runAndWait()


def speak(str):
    engine.say(str)
    engine.runAndWait()

def usr_input():
    str=input("Enter waht to you want to speak: ")
    if str=='z':
        exit()
    else:
        speak(str)

def main():
    while True:
        usr_input()
        
       
    
main()