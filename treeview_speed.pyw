import os
import sys
import time
import _thread as thread
import tkinter.ttk

from datetime import datetime
from tkinter import *
from tkinterdnd2 import *


root = TkinterDnD.Tk()
root.title("treeview test")
root.geometry(f'1000x500+0+0')
root.resizable(True, True)

treeview_list = tkinter.ttk.Treeview(root, selectmode='extended')
treeview_list["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
treeview_list['show']    = "headings"
treeview_yscroll = tkinter.ttk.Scrollbar(root, orient="vertical", command=treeview_list.yview)
treeview_list.configure(yscrollcommand=treeview_yscroll.set)
treeview_list.pack(side=LEFT, fill=BOTH, expand=True)
treeview_yscroll.pack(side=LEFT, fill=Y, expand=False)

treeview_list["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
treeview_list.heading("1",  text=f"csv line", anchor="center")
treeview_list.heading("2",  text=f"run time", anchor="center")
treeview_list.heading("3",  text=f"csv data", anchor="center")
treeview_list.heading("4",  text=f"csv data", anchor="center")
treeview_list.heading("5",  text=f"csv data", anchor="center")
treeview_list.heading("6",  text=f"csv data", anchor="center")
treeview_list.heading("7",  text=f"csv data", anchor="center")
treeview_list.heading("8",  text=f"csv data", anchor="center")
treeview_list.heading("9",  text=f"csv data", anchor="center")

treeview_list.column("1",   stretch=False, minwidth=5, width=100, anchor="w")
treeview_list.column("2",   stretch=False, minwidth=5, width=100, anchor="w")
treeview_list.column("3",   stretch=False, minwidth=5, width=280, anchor="w")
treeview_list.column("4",   stretch=False, minwidth=5, width=80, anchor="center")
treeview_list.column("5",   stretch=False, minwidth=5, width=80, anchor="center")
treeview_list.column("6",   stretch=False, minwidth=5, width=80, anchor="center")
treeview_list.column("7",   stretch=False, minwidth=5, width=80, anchor="center")
treeview_list.column("8",   stretch=False, minwidth=5, width=80, anchor="center")
treeview_list.column("9",   stretch=False, minwidth=5, width=80, anchor="center")

def get_line(path):
    f_path = open(path, 'r')
    line = len(f_path.readlines())
    return line

def run_thread():
    total_line = get_line("log.csv")

    time_start = datetime.now()

    count_total = 0
    with open("log.csv", "r") as f:
        for line in f:
            count_total += 1

            index_num  = len(treeview_list.get_children()) + 1
            index_str  = str(index_num)

            time_diff  = ((datetime.now() - time_start).total_seconds())
            treeitem = [ f"{count_total}/{total_line}",
                         '%.3f'%time_diff,
                         f"{line}",
                         f"{count_total}",
                         f"{count_total+10}",
                         f"{count_total+100}",
                         f"{count_total+1000}",
                         f"{count_total+10000}",
                         f"{count_total+100000}",
                       ]
            treeview_list.insert('', 'end', text=index_num, iid=index_num, values=treeitem)
            treeview_list.yview(index_num)
            print(f"count_total = {count_total}, {int(time_diff)} sec")

thread.start_new_thread(run_thread, ())

root.mainloop()
