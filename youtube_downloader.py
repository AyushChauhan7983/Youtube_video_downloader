from tkinter import *
from pytube import YouTube

root=Tk()
root.geometry("800x300")
root.title("YOUTUBE VIDEO DOWNLOADER APPLICATION")
def download() :
    try:
        myVar.set("Downloading...")
        root.update()
        YouTube(link.get()).streams.first().download()
        link.set("Video downloaded successfully")
    except Exception as e:
        myVar.set("Mistake")
        root.update()
        link.set("Enter the correct link")

Label(root,text="Welcome to youtube downloader application",font="Consolas 20 bold").pack()
myVar=StringVar()
myVar.set("Enter the link below")
Entry(root,textvariable=myVar,font="Times 15",width=40).pack(pady=10)
link=StringVar()
Entry(root,textvariable=link,width=60).pack(pady=10)
Button(root,text="Download video",fg='#000000',bg='#00ffff',command=download).pack()
root.mainloop()