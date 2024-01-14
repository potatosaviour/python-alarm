from tkinter import *
import datetime
import time
from playsound import playsound as ps

def Alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        actual_time = datetime.datetime.now()
        cur_time = actual_time.strftime("%H:%M:%S")
        cur_date = actual_time.strftime("%d/%m/%Y")
        msg = "Current Time: " + str(cur_time)
        print(msg)
        if cur_time == set_alarm_timer:
            ps("alarm.mp3")
            break


def get_alarm_time():
    alarm_set_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    Alarm(alarm_set_time)

def display_time():
    current_time = time.strftime('%H:%M:%S')
    time_label.config(text=current_time)
    time_label.after(1000, display_time)

window = Tk()
window.title("Alarm Clock")
window.geometry("400x400")
window.config(bg="#922B21")
window.resizable(width=False, height=False)

time_label = Label(window, font=("Arial", 30), fg="white", bg="#922B21")
time_label.pack(pady=30)

time_format = Label(window, text="Alarm time is in 24 hour format!", fg="white", bg="#922B21", font=("Arial", 15))
time_format.pack(pady=10)

add_time = Label(window, text="Hour Min Sec", font=60, fg="white", bg="black")
add_time.place(x=140)

set_your_alarm = Label(window, text="Set Time for Alarm: ", fg="white", bg="#922B21", relief="solid", font=("Helvetica", 15, "bold"))
set_your_alarm.place(x=50, y=80)

hour = StringVar()
minute = StringVar()
second = StringVar()

hour_time = Entry(window, textvariable=hour, bg="#48C9B0", width=4, font=(20))
hour_time.place(x=240, y=80)

minute_time = Entry(window, textvariable=minute, bg="#48C9B0", width=4, font=(20))
minute_time.place(x=290, y=80)

second_time = Entry(window, textvariable=second, bg="#48C9B0", width=4, font=(20))
second_time.place(x=340, y=80)

submit = Button(window, text="Set Your Alarm", fg="Black", bg="#D4AC0D", width=15, command=get_alarm_time, font=(20))
submit.place(x=100, y=150)

display_time()

window.mainloop()
