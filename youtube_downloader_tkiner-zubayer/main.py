import tkinter as tk
from pytube import YouTube


def downloadVid():
    global E1
    string = E1.get()
    lb.configure(text=string)
    #print(string);
    yt = YouTube(str(string))
    videos = yt.get_videos()
    s=1
    for v in videos:
        print(str(s)+ '.' + str(v))
        s += 1
    n = int(input("Enter your choice:"))
    vid = videos[n-1]
    dest = str(input("Enter the destination:"))
    vid.download(dest)
    print(yt.filename+"\n Video has been downloaded")


root = tk.Tk()

root.geometry('450x300')

w=tk.Label(root, text="Youtube Downloader")
w.pack()

E1 = tk.Entry(root,bd=6)
E1.focus()
E1.pack(side=tk.TOP)

lb = tk.Label(root,text="the Link")
lb.pack()


button = tk.Button(root,text="Download",bg="black",fg="green",command=downloadVid )
button.pack(side=tk.BOTTOM)

root.mainloop()





