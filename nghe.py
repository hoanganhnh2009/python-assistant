# https://pypi.org/project/SpeechRecognition/
import speech_recognition

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("Robot: I'm listening")
    audio = robot_ear.listen(mic)

try:
    you = robot_ear.recognize_google(audio)
except:
    you = ""

print(you)

# import speech_recognition as sr
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(
#         index, name))
