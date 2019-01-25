# Live Speech Recognition
#sudo pip3 install SpeechRecognition
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Something:")
    audio = r.listen(source)
    
    try:
        text = r.Recognize_google(audio)
        print("You said : {}",format(text))
    except:
        print("Could not recognize your voice!!!")
