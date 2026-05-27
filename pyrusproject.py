import tkinter as tk
import time
import pyautogui
import os, sys
from PIL import Image , ImageTk
import winsound
import keyword

time.sleep(1)

dir = os.path.dirname(os.path.abspath(sys.argv[0]))

print(dir)

pyautogui.hotkey('win', 'd')
time.sleep(0.7)
prcr = pyautogui.screenshot('desktop.png')



windows = tk.Tk()
windows.geometry("{}x{}".format(windows.winfo_screenwidth(), windows.winfo_screenheight()))
windows.attributes('-topmost', True)


bg = ImageTk.PhotoImage(Image.open('desktop.png'))
bgimage = tk.Label(windows, image=bg , width=windows.winfo_screenwidth(), height=windows.winfo_screenheight())
bgimage.place(x=0, y=0)


def updateImage(number,sleepNumber):
    imgName = f"{dir}/images/img{number}.png"
    img = Image.open(imgName).resize((windows.winfo_screenwidth(), windows.winfo_screenheight()))
    bg1 = ImageTk.PhotoImage(img)
    bgimage.configure(image=bg1)
    windows.update()
    time.sleep(sleepNumber)






def initiate(e):
    time.sleep(1)
    updateImage(2,0.90)
    winsound.PlaySound(f"{dir}/noise3.wav", winsound.SND_ASYNC)
    updateImage(3,0.5)
    updateImage(4,0.05)
    winsound.PlaySound(f"{dir}/noise2.wav", winsound.SND_ASYNC)
    updateImage(5,0.75)
    winsound.PlaySound(f"{dir}/noise1.wav", winsound.SND_ASYNC)
    updateImage(6,0.4)
    winsound.PlaySound(f"{dir}/noise3.wav", winsound.SND_ASYNC)
    updateImage(1,0.5)
    winsound.PlaySound(f"{dir}/noise3.wav", winsound.SND_ASYNC)
    updateImage(3,0.2)
    winsound.PlaySound(f"{dir}/noise2.wav", winsound.SND_ASYNC)
    updateImage(5,0.3)
    winsound.PlaySound(f"{dir}/noise1.wav", winsound.SND_ASYNC)
    updateImage(6,0.6)
    winsound.PlaySound(f"{dir}/noise3.wav", winsound.SND_ASYNC)
    updateImage(2, 0.90)
    winsound.PlaySound(f"{dir}/noise3.wav", winsound.SND_ASYNC)
    updateImage(3, 0.5)
    updateImage(4, 0.05)
    winsound.PlaySound(f"{dir}/noise2.wav", winsound.SND_ASYNC)
    updateImage(5, 0.75)
    winsound.PlaySound(f"{dir}/noise1.wav", winsound.SND_ASYNC)
    updateImage(6, 0.4)
    updateImage(3, 0.2)
    winsound.PlaySound(f"{dir}/noise2.wav", winsound.SND_ASYNC)
    updateImage(5, 0.3)
    winsound.PlaySound(f"{dir}/noise1.wav", winsound.SND_ASYNC)
    updateImage(6, 0.6)
    winsound.PlaySound(f"{dir}/noise3.wav", winsound.SND_ASYNC)
    updateImage(6, 0.4)
    winsound.PlaySound(f"{dir}/noise3.wav", winsound.SND_ASYNC)
    updateImage(1, 0.5)
    winsound.PlaySound(f"{dir}/noise3.wav", winsound.SND_ASYNC)
    updateImage(3, 0.2)
    winsound.PlaySound(f"{dir}/noise2.wav", winsound.SND_ASYNC)
    updateImage(5, 0.3)
    winsound.PlaySound(f"{dir}/noise1.wav", winsound.SND_ASYNC)
    updateImage(6, 0.6)
    winsound.PlaySound(f"{dir}/noise3.wav", winsound.SND_ASYNC)
    updateImage(2, 0.90)
    winsound.PlaySound(f"{dir}/noise3.wav", winsound.SND_ASYNC)
    updateImage(3, 0.5)
    updateImage(4, 0.05)
    winsound.PlaySound(f"{dir}/noise2.wav", winsound.SND_ASYNC)
    updateImage(5, 0.75)
    winsound.PlaySound(f"{dir}/noise1.wav", winsound.SND_ASYNC)
    updateImage(6, 0.4)
    updateImage(3, 0.2)
    updateImage(2, 0.90)
    winsound.PlaySound(f"{dir}/noise3.wav", winsound.SND_ASYNC)
    updateImage(3, 0.5)
    updateImage(4, 0.05)
    winsound.PlaySound(f"{dir}/noise2.wav", winsound.SND_ASYNC)
    updateImage(5, 0.75)
    winsound.PlaySound(f"{dir}/noise1.wav", winsound.SND_ASYNC)
    updateImage(6, 0.4)
    updateImage(3, 0.2)
    winsound.PlaySound(f"{dir}/noise2.wav", winsound.SND_ASYNC)
    updateImage(5, 0.3)
    winsound.PlaySound(f"{dir}/noise1.wav", winsound.SND_ASYNC)
    updateImage(6, 0.6)
    winsound.PlaySound(f"{dir}/noise3.wav", winsound.SND_ASYNC)
    updateImage(6, 0.4)
    winsound.PlaySound(f"{dir}/noise3.wav", winsound.SND_ASYNC)
    updateImage(1, 0.5)
    windows.destroy()


bgimage.bind('<Button-1>',initiate)


def terminate(e):
    windows.destroy()

windows.bind('<Up>',terminate)

def blockKeys(e):
    if e.keysym == 'Up':
        return
    return "break"


windows.bind_all('Key', blockKeys)
windows.attributes('-fullscreen', True)
windows.update()
windows.mainloop()