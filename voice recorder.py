from tkinter import *
import os
import wave
import time
import threading
import pyaudio

window=Tk()
window.title("Voice Recorder")
window.geometry("500x500")
window.resizable(False,False)
window.config(bg="white")

class VoiceRecorder:

    
    def __init__(self):
        self.recording = False
        self.frames = []
        
        self.button = Button(window, text="🎤", font=("Arial",20, "bold"), command=self.click_handler)
        self.button.place(x=230, y=220)

        self.label = Label(window, text="00:00:00",font=("Arial",20, "bold"),bg='white')
        self.label.place(x=200,y=280)
    
    def click_handler(self):
        if self.recording:
           self.recording=False
           self.button.config(fg="black")
        else:
          self.recording=True
          self.button.config(fg="green")
          threading.Thread(target=self.record).start()

    def record(self):
          audio=pyaudio.PyAudio()
          stream=audio.open(format=pyaudio.paInt16,channels=1,rate=44100,input=True,frames_per_buffer=1024)

          self.frames=[]
          start=time.time()

          while self.recording:
              data=stream.read(1024)
              self.frames.append(data)

              passed=time.time()-start
              secs=passed%60
              mins=passed//60
              hours=mins//60
              self.label.config(text=f"{int(hours):02d}:{int(mins):02d}:{int(secs):02d}")
          stream.stop_stream()
          stream.close()
          audio.terminate()

          exists=True
          i=1
          while exists:
              if os.path.exists(f"recording{i}.wav"):
                  i+=1
              else:
                  exists=False
                  
              

          sound_file=wave.open(f"recording{i}.wav","wb")
          sound_file.setnchannels(1)
          sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
          sound_file.setframerate(44100)
          sound_file.writeframes(b"".join(self.frames))
          sound_file.close()                           

voice_recorder = VoiceRecorder()

photo = PhotoImage(file='C:/Users/Miruthula M/Downloads/image.png')
picture = Label(image=photo,bg='white')
picture.pack(padx=6, pady=5)

b1=Label(window,text="Press the button for start recording!",font=('arial',15,'bold'),bg='white',fg='black')
b1.place(x=80,y=150)
x1 = Label(text='Voice Recorder', font=('arial', 20, 'bold'),bg='white', fg='black')
x1.pack()
window.mainloop()
