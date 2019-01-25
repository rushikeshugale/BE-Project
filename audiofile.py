# File Speech Recognition
#sudo pip3 install SpeechRecognition
import speech_recognition as sr

r = sr.Recognizer()

audio = 'File name(with .wav)'
with sr.AudioFile(audio) as source:
    audio = r.listen(source)
    
    try:
        text = r.Recognize_google(audio)
        print("You said : {}",format(text))
    except exception as e:
        print(e)
