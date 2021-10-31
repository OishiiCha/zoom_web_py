from tkinter import *
import webbrowser
import platform
import csv
import os

bgc = "grey12"

height = 200
width = 300

myfont = ("arial",10)

root = Tk()
root.geometry(str(width)+"x"+str(height))
root.title("Zoom Web")
root.config(bg=bgc)
root.resizable(width=False, height=False)
if platform.system() == "Windows":
    root.iconbitmap("data/zoom_web.ico")

row1 = int(height/5*1)
row2 = int(height/5*2)
row3 = int(height/5*3)
row4 = int(height/5*4)

def enter_data():
    txt_name = ent.get()
    meeting_id = txt_name.replace(" ", "")
    if len(meeting_id) in (10,11):
        link = "https://pwa.zoom.us/wc/join/" + meeting_id
        error_message = Label(root, text="                                                     ", bg=bgc, font=myfont, justify="center")
        error_message.place(x=int(width/2), y=row3, anchor="center")
        webbrowser.open(link, 1)
    else:
        error_message = Label(root, text="Please enter a valid meeting ID", bg=bgc, fg="white", font=myfont, justify="center")
        error_message.place(x=int(width/2), y=row3, anchor="center")


def set_mem1():
    data_location = str("data/memory/"+variable.get()+".txt")
    if os.path.isfile(data_location):
        os.remove(data_location)
    with open(data_location, "x") as f1:
        f1.writelines(str(ent.get()))
        f1.close


def read_mem1():
    data_location = str("data/memory/"+variable.get()+".txt")
    f1r = open(data_location,"r")
    mem_data = f1r.read()
    webbrowser.open("https://pwa.zoom.us/wc/join/"+mem_data, 1)



m_id = Label(root, text = "Meeting ID:", bg=bgc, fg="white", font=myfont)
m_id.place(x=int(width/5*1), y=row1, anchor="center")
ent = Entry(root, justify="center", bg="white", fg="black", font=myfont)
ent.place(x=int(width/5*3), y=row1, anchor="center")
btn = Button(root, text="Enter", bg=bgc, fg="white", font=myfont, command=enter_data)
btn.place(x=int(width/2), y=row2, anchor="center")
saved_b = Button(root, text="Open", bg="deepskyblue2", fg="white", font=myfont, command= read_mem1)
saved_b.place(x=int(width/4*1), y=row4, anchor="center")
myoption = ["Mem1", "Mem2", "Mem3", "Mem4"]
variable = StringVar(root)
variable.set(myoption[0])
memoption = OptionMenu(root, variable, *myoption)
memoption.place(x=int(width/2), y=row4, anchor="center")
set_b = Button(root, text="Save", bg="deepskyblue2", fg="white", font=myfont, command=set_mem1)
set_b.place(x=int(width/4*3), y=row4, anchor="center")

if __name__ == '__main__':
    root.mainloop()

