import tkinter
from tkinter import *
from tkinter import ttk
import time
import os
from tkinter import messagebox


class TimerApp(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)

        self.timeMsgList = []
        self.remove_idx = -1

        self.frame1 = ttk.Frame()
        self.frame1.pack()
        self.frame1.config(height=100, width=100)

        self.label1 = ttk.Label(self.frame1, text="Enter the Alarm time :")
        self.label1.pack()

        self.entry1 = ttk.Entry(self.frame1, width=30)
        self.entry1.pack()
        self.entry1.insert(3, "example - 13:15")

        self.labelAlarmMessage = ttk.Label(self.frame1, text="Alarm Message:")
        self.labelAlarmMessage.pack()

        self.entry2 = ttk.Entry(self.frame1, width=30)
        self.entry2.pack()

        self.button1 = ttk.Button(self.frame1, text="submit", command=self.submit_button)
        self.button1.pack()
        # this Label2 will show the Last Alarm Time

        self.button2 = ttk.Button(self.frame1, text="list", command=self.list_button)
        self.button2.pack()

        self.label2 = ttk.Label(self.frame1)
        self.label2.pack()

    def timer(self):
        print('DEBUG : current Time = {}'.format(time.strftime('%H:%M:%S')))
        print('DEBUG : current Alarm List = {}'.format(str(self.timeMsgList)))
        cur_time = time.strftime('%H:%M')
        for i in range(len(self.timeMsgList)):
            if cur_time == self.timeMsgList[i][0]:
                self.after(0, self.alarm_alarm(self.timeMsgList[i][1]))
                self.remove_idx = i
        if self.remove_idx >= 0:
            self.timeMsgList.pop(self.remove_idx)
            self.remove_idx = -1
        self.after(1000, self.timer)

    def submit_button(self):
        time_str = self.entry1.get()
        msg_str = self.entry2.get()
        self.timeMsgList.append((time_str, msg_str))

    def list_button(self):
        messagebox.showinfo(title='Alarm List', message="{}".format(self.timeMsgList))


    def alarm_alarm(self, msg):
        print("now Alarm Musing Playing")
        os.system("start alarm-music.mp3")
        self.label2.config(text="Alarm music playing.....")
        messagebox.showinfo(title='Alarm Message', message="{}".format(msg))


root = TimerApp()
root.title("Alarm clock")
root.timer()
root.mainloop()