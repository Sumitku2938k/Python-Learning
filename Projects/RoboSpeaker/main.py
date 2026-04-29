# import os
#
# if __name__ == '__main__':
#     print("Welcome to RoboSpeaker 1.1 Created  by Goutam")
#     while True:
#         x = input("Enter what you want me to speak:")
#         if x == "q":
#             os.system("say 'bye bye friend'")
#             break
#         command = f"say {x}"
#         os.system(command)

import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

print("Welcome to RoboSpeaker 1.1 Created  by Goutam")
while True:
    x = input("Enter what you want me to speak: ")
    if x == "q":
        speak.Speak("Bye bye friend")
        break
    command = f"{x}"
    speak.Speak(command)