import sounddevice
from scipy.io.wavfile import write
from tkinter import *
from tkinter.messagebox import showinfo,showwarning
from tkinter.filedialog import askdirectory

add=""

def file_path():
    global add 
    add=askdirectory()
    
def save_file():
    global add
    try:
      time =int(sec.get())
      addr=add+"/"+"demo.wav"
      showinfo(title="start",message="Rec start")
      rece=sounddevice.rec((time*44100),samplerate=44100,channels=2)
      sounddevice.wait()
      write(addr,44100,rece)
      showinfo(title="End",message="Rec stop")
    except:
        showwarning(title="Time",message="Wrong Format Time")


def main_window():
    global sec
    win = Tk()
    win.geometry("500x600")
    win.resizable(False,False)
    win.title("wscube Tech")
    win.config(bg="yellow")

    img1 =PhotoImage (file="nik.png")
    L1 =Label(win,image=img1)
    L1.place(x=150,y=50,height=200,width=200)
    
    sec =Entry(win,font=(20))
    sec.place( x= 150 ,y=260,height=50,width=200)

    L2 =Label(win,text="Time in sec.",font=("Time in Roman",20),bg ="yellow")
    L2.place( x=180,y=320,height=50,width=150)

    b=Button(win,text="path",font=("Time New Roman",20),command=file_path)
    b.place( x=150,y=380,height=50,width=200)

    img2= PhotoImage(file="kum.png")
    start=Button(win,image=img2,command=save_file)
    start.place( x=230,y=440,height=50,width=50)





    win.mainloop()
main_window()