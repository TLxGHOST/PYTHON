import os

if __name__ == '__main__':
    print("Hello world")
    while True:
        x=input("Enter the command: ")
        if x=='z':
            os.system('exit')
        else:
            command=f'mshta vbscript:Execute("CreateObject(""SAPI.SpVoice"").Speak(""{x}"")(window.close)")'
            os.system(command)