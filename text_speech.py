# pip install pyttsx3
import pyttsx3
txt_sp=pyttsx3.init()
text=input('Enter the text.......')
voice=txt_sp.getProperty('voices')
for i in voice:
    print('ID:',i.id)
txt_sp.setProperty('voice',voice[0].id)
txt_sp.say(text)
txt_sp.runAndWait()