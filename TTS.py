import speech_recognition as sr 
import pyttsx3 
import re
r = sr.Recognizer() 
def SpeakText(command): 
    engine = pyttsx3.init() 
    engine.say(command) 
    engine.runAndWait() 
def solve(x): return eval(''.join(re.findall("[+-/x]*[0-9]*",x)))
while(1):
    try: 
        with sr.Microphone() as source2: 
            r.adjust_for_ambient_noise(source2, duration=0.1) 
            audio2 = r.listen(source2) 
            #MyText = r.recognize_sphinx(audio2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            if MyText=='close':
                SpeakText("closing")
                break
            SpeakText("you said"+MyText)
            print(MyText)
            if MyText=='close':
                break
            if MyText.find('calculate')>=0:
                SpeakText('result is'+str(solve(MyText)))
                print(solve(MyText))
    except:
        SpeakText("speak again")
