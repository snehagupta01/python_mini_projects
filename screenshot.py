import time
import pyautogui
import tkinter as tk
# print("hi")

def takess():
    name=int(round(time.time()*1000))
    name='F:/python_mini_projects/screenshot/ssdata/{}.png'.format(name)
    # time.sleep(5)
    img=pyautogui.screenshot(name)
    img.show()

#takess()
root=tk.Tk()
frame=tk.Frame(root)
frame.pack()

button=tk.Button(
    frame,
    text="Take screenshot",
    command=takess)

button.pack(side=tk.LEFT)

close=tk.Button(
    frame,
    text="Quit",
    command=quit)

close.pack(side=tk.RIGHT)

root.mainloop()