from tkinter import *
from tkinter.messagebox import showinfo
import pyttsx3
import speech_recognition as sr
def speak(text: str):
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 100)
engine.say(text)
engine.runAndWait()
def recordEng():
r = sr.Recognizer()
with sr.Microphone() as source:
r.pause_threshold = 1
audio = r.listen(source)
try:
query = r.recognize_google(audio, language="en-US")
except Exception as e:
showinfo(title='Error!', message=e)
speak("I am sorry, I did not get that, but could you please repeat that")
return "Nothing"
return query
def recordHin():
r = sr.Recognizer()
with sr.Microphone() as source:
r.pause_threshold = 1
audio = r.listen(source)
try:
query = r.recognize_google(audio, language="hi-IN")
except Exception as e:
showinfo(title='Error!', message=e)
speak("I am sorry, I did not get that, but could you please repeat that")
return "Nothing"
return query
def recordGuj():
r = sr.Recognizer()
with sr.Microphone() as source:
r.pause_threshold = 1
audio = r.listen(source)
try:
query = r.recognize_google(audio, language="gu-IN")
except Exception as e:
showinfo(title='Error!', message=e)
speak("I am sorry, I did not get that, but could you please repeat that")
return "Nothing"
return query
def recordMar():
r = sr.Recognizer()
with sr.Microphone() as source:
r.pause_threshold = 1
audio = r.listen(source)
try:
query = r.recognize_google(audio, language="mr-IN")
except Exception as e:
showinfo(title='Error!', message=e)
speak("I am sorry, I did not get that, but could you please repeat that")
return "Nothing"
return query
def TTS():
tts_wn = Toplevel(root)
tts_wn.title('Text-to-Speech Converter')
tts_wn.geometry("350x250")
tts_wn.configure(bg='PowderBlue')
Label(tts_wn, text='Text-to-Speech Converter', font=("Cambria", 15),
bg='PowderBlue').place(x=50)
text = Text(tts_wn, height=5, width=30, font=12)
text.place(x=10, y=60)
speak_btn = Button(tts_wn, text='Record', bg='LightSkyBlue', command=lambda:
speak(str(text.get(1.0, END))))
speak_btn.place(x=140, y=200)
def STTEng():
stt_wn = Toplevel(root)
stt_wn.title('Speech-to-Text Converter in English')
stt_wn.geometry("350x200")
stt_wn.configure(bg='PowderBlue')
Label(stt_wn, text='Speech-to-Text Converter', font=("Cambria", 15),
bg='PowderBlue').place(x=50)
text = Text(stt_wn, font=12, height=3, width=30)
text.place(x=7, y=100)
record_btn = Button(stt_wn, text='Record', bg='LightSkyBlue', command=lambda:
text.insert(END, recordEng()))
record_btn.place(x=140, y=50)
def STTHin():
stt_wn = Toplevel(root)
stt_wn.title('Speech-to-Text Converter in Hindi')
stt_wn.geometry("350x200")
stt_wn.configure(bg='PowderBlue')
Label(stt_wn, text='Speech-to-Text Converter', font=("Cambria", 15),
bg='PowderBlue').place(x=50)
text = Text(stt_wn, font=12, height=3, width=30)
text.place(x=7, y=100)
record_btn = Button(stt_wn, text='Record', bg='LightSkyBlue', command=lambda:
text.insert(END, recordHin()))
record_btn.place(x=140, y=50)
def STTGuj():
stt_wn = Toplevel(root)
stt_wn.title('Speech-to-Text Converter in Gujarati')
stt_wn.geometry("350x200")
stt_wn.configure(bg='PowderBlue')
Label(stt_wn, text='Speech-to-Text Converter', font=("Cambria", 15),
bg='PowderBlue').place(x=50)
text = Text(stt_wn, font=12, height=3, width=30)
text.place(x=7, y=100)
record_btn = Button(stt_wn, text='Record', bg='LightSkyBlue', command=lambda:
text.insert(END, recordGuj()))
record_btn.place(x=140, y=50)
def STTMar():
stt_wn = Toplevel(root)
stt_wn.title('Speech-to-Text Converter in Marathi')
stt_wn.geometry("350x200")
stt_wn.configure(bg='PowderBlue')
Label(stt_wn, text='Speech-to-Text Converter', font=("Cambria", 15),
bg='PowderBlue').place(x=50)
text = Text(stt_wn, font=12, height=3, width=30)
text.place(x=7, y=100)
record_btn = Button(stt_wn, text='Record', bg='LightSkyBlue', command=lambda:
text.insert(END, recordMar()))
record_btn.place(x=140, y=50)
def instruction():
instructions = '''
These are the instructions:
1. Wait for some time because STT and TTS conversions take time.
2. Pause for a second to end your phrase in STT conversion, because that is the
pause_threshold amount.
'''
showinfo("Instructions", instructions)
#GUI
root = Tk()
root.title('TTS and STT Converter')
root.geometry('500x500')
root.resizable(0, 0)
root.configure(bg='MistyRose')
Label(root, text='Text-To-Speech and Speech-To-Text Converter', font=('Cambria',
16), bg='MistyRose', wrap=True, wraplength=300).place(x=125, y=0)
tts_btn = Button(root, text=' TTS Conversion ', font=('Cambria', 16),
bg='AliceBlue', command=TTS)
tts_btn.place(x=125, y=200)
stt_btn = Button(root, text='STT Conversion in English', font=('Cambria', 16),
bg='AliceBlue', command=STTEng)
stt_btn.place(x=125, y=250)
stt_btn = Button(root, text=' STT Conversion in Hindi ', font=('Cambria', 16),
bg='AliceBlue', command=STTHin)
stt_btn.place(x=125, y=300)
stt_btn = Button(root, text='STT Conversion in Gujarati', font=('Cambria', 16),
bg='AliceBlue', command=STTGuj)
stt_btn.place(x=125, y=350)
stt_btn = Button(root, text='STT Conversion in Marathi', font=('Cambria', 16),
bg='AliceBlue', command=STTMar)
stt_btn.place(x=125, y=400)
instruction_btn = Button(root, text=' Instructions ',
font=('Cambria', 16), bg='AliceBlue', command=instruction)
instruction_btn.place(x=125, y=450)
root.update()
root.mainloop()
