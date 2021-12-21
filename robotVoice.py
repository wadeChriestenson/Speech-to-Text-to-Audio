import speech_recognition as sr
from gtts import gTTS
voice = ''
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(text)
            if text == 'stop':
                break
            text = r.recognize_google(audio)
            voice = voice + str(text)
        except:
            print('say something....')
hr = gTTS(text=voice, slow=True)
hr.save('1.mp3')
