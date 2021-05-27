from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
import os
import re
from datetime import datetime
from datetime import date
import time
from time import strftime
import sys

dates_list = []
new_date = ""

date_file = open("dates.txt", "r+")
dates = date_file.readlines()
date_file.close()


def manage_time(clients_day_entry, clients_hour_entry):
# this calculates the rest time to the delivery
    global dates_list, time_elapsed, dates
    date_str = clients_day_entry + " " + clients_hour_entry + ":00"
    date_dt = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')


# this saves the dates
    date_file = open("dates.txt", "a+")
    date_file.write(str(date_dt) + " \n")
    date_file.close()

# this adds all the dates from dates.txt to dates_list

for j in range(len(dates)):
    if dates[j] != "\n" and dates[j] != " ":
        dates_list.append(dates[j].replace("\n", ""))


manage_time("2021-10-15", "16:30")




now = ""






root = Tk()
def define_time():
# this calculates the rest time to the delivery
    global dates_list, time_elapsed, new_date

    new_date = dates_list[1]
    new_date = datetime.strptime(new_date, '%Y-%m-%d %H:%M:%S')
    print(type(new_date))
    calculate_time()


def print_time():
    global new_date, time_elapsed, lbl, now
    time_elapsed = new_date - now


    lbl.config(text=str(time_elapsed))
    lbl.after(1000, calculate_time())


def calculate_time():
    global new_date, time_elapsed, now

    now = strftime('%Y-%m-%d %H:%M:%S')
    now = datetime.strptime(now, '%Y-%m-%d %H:%M:%S')
    print(type(now))
    print_time()


root.title('Clock')

lbl = tk.Label(root)
lbl.pack(anchor='center')

calculate_time()

mainloop()
