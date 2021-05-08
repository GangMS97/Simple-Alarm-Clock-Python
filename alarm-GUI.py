# Alarm clock using Python Tkinter module by Rajkumar Selvaraj
from tkinter import *
from tkinter import ttk
import time
import os
from tkinter import messagebox

# def main():
root = Tk()
root.title("Alarm clock")


def SubmitButton():
    AlarmTime = entry1.get()
    Message1()
    # label2.config(text ="The Alarm will Ring at {} ".format(AlarmTime))  #delayed in execution
    # CurrentTime = time.strftime("%H:%M")
    print("the alarm time is: {}".format(AlarmTime))
    # label2.config(text="")\
    def update_clock(self):
        CurrentTime = time.strftime("%H:%M")

        # label2.config(text ="The Alarm will Ring at {} ".format(AlarmTime))
        if AlarmTime == CurrentTime:
            print("now Alarm Musing Playing")
            os.system("start alarm-music.mp3")
            label2.config(text="Alarm music playing.....")
            label3.config(text=format(AlarmTime))
            messagebox.showinfo(title='Alarm Message', message="{}".format(entry2.get()))
        else:
            self.root.after(1000, self.update_clock)



    #if AlarmTime == CurrentTime:
     #   print("now Alarm Musing Playing")
      #  os.system("start alarm-music.mp3")
       # label2.config(text="Alarm music playing.....")
        #label3.config(text=format(AlarmTime))
        #messagebox.showinfo(title='Alarm Message', message="{}".format(entry2.get()))




def ListButton():
    AlarmTime = entry1.get()
    # Message1()
    messagebox.showinfo(title='Alarm List', message="{}".format(entry1.get()))



def Message1():
    AlarmTimeLable = entry1.get()
    label2.config(text="the Alarm time is Counting...")
    # label2.config(text= "the Alarm will ring at {}".format(AlarmTimeLable))
    messagebox.showinfo(title='Alarm clock', message='Alarm will Ring at {}'.format(AlarmTimeLable))


frame1 = ttk.Frame(root)
frame1.pack()
frame1.config(height=100, width=100)

label1 = ttk.Label(frame1, text="Enter the Alarm time :")
label1.pack()

entry1 = ttk.Entry(frame1, width=30)
entry1.pack()
entry1.insert(3, "example - 12:29")

labelAlarmMessage = ttk.Label(frame1, text="Alarm Message:")
labelAlarmMessage.pack()

entry2 = ttk.Entry(frame1, width=30)
entry2.pack()

button1 = ttk.Button(frame1, text="submit", command=SubmitButton)
button1.pack()

button2 = ttk.Button(frame1, text="list", command=ListButton)
button2.pack()
# this Label2 will show the Last Alarm Time
label2 = ttk.Label(frame1)
label2.pack()
label3 = ttk.Label(frame1)
label3.pack()

# label2.config(text="hello")

root.mainloop()

