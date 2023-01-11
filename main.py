import tkinter as tk
from tkinter import messagebox
from time import sleep
import asyncio
import random
from functions import *


class Window(tk.Tk):
    def __init__(self, loop):
        """
        The Default __init__ Constructor. Constructors are used to initializing the object’s state.
        """
        self.win_wight = 600
        self.win_height = 800
        self.stop = True  # To stop sorting

        self.loop = loop

        # Main window
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.title('SortLib')
        self.root.wm_attributes('-alpha', 0.9)
        self.root.geometry(str(self.win_wight) + 'x' + str(self.win_height))
        self.root.resizable(width=False, height=False)

        # Frame for the image of the sorting progress
        self.frame = tk.Frame(bg='#ffffff')
        self.frame.place(relx=0.05, rely=0.15,
                         relheight=0.825, relwidth=0.9)
        self.canvas = tk.Canvas(self.frame)
        self.btn_stop = tk.Button(self.frame)


      
        # Textbox for enter the number of elements
        self.entrylabel = tk.Label(text="Count:")
        self.entrylabel.grid(column=0, row=0, padx=10, pady=4)
        self.entry_count = tk.Entry(width=20)
        self.entry_count.insert(0, '100')
        self.entry_count.grid(column=1, row=0, padx=10, pady=4)

        
        # Textbox for enter the sleep time
        self.entrylabel = tk.Label(text="Sleep Time(msec):")
        self.entrylabel.grid(column=0, row=2, padx=10, pady=4)
        self.entry_sleep = tk.Entry(width=20)
        self.entry_sleep.insert(0, '0.1')
        self.entry_sleep.grid(column=1, row=2, padx=10, pady=4)

        #OptionMenu for selecting the sorting method        
        self.menulabel = tk.Label(text="Type:")
        self.menulabel.grid(column=0, row=1, padx=10, pady=4)
        sort = Sort()
        OptionList = {
        "BubbleSort":  sort.BubbleSort,
        "CocktailSort": sort.CocktailSort
        }
        variable = tk.StringVar(self.root)
        variable.set(list(OptionList.keys())[0])

        self.opt = tk.OptionMenu(self.root, variable, *list(OptionList.keys()))
        self.opt.config(width=10)
        self.opt.grid(column=1, row=1, padx=10, pady=4)

        # Button for start sorting
        self.btn_start = tk.Button(text='Sort', bg='#f1f1ff',
                             command=lambda: self.loop.create_task(self.StartSort(int(self.entry_count.get()), 
                                                                    (self.win_wight-80)/int(self.entry_count.get()), 
                                                                    OptionList.get(variable.get()),float(self.entry_sleep.get())/1000)))
        self.btn_start.grid(column=2, row=2, padx=10, pady=4)


    async def show(self):   
        """
        Async method that updates the window
        """
        while True:
            self.root.update()
            await asyncio.sleep(0.1)


    def on_closing(self):
        """
        The method that closes the window and asynchronous processes
        """
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
            asyncio.get_running_loop().stop()  # Get running event loop in the current OS thread and stop them


    def stop_sort(self):
        self.stop = True

        
    def StartSort(self, count, rect_width, function, sleep_time):
        """
        Func for start sorting 

        count: number of items to sort
        rect_width: column width
        function: sorting method from functions.py
        """
        arr = []
        rect_arr = []
        self.stop = False
        self.btn_start['state'] = "disabled"

        # Destroy and creating new canvas
        self.canvas.destroy()
        self.btn_stop.destroy()
        self.canvas = tk.Canvas(self.frame, height=self.frame.winfo_height()-50,
                                width=self.frame.winfo_width(), bg='#fcfcfc')
        self.btn_stop = tk.Button(self.frame, text='Stop', bg='#ffc0c0',
                                  command=self.stop_sort, height=50,
                                  width=self.frame.winfo_width())
        self.canvas.pack(side='top')
        self.btn_stop.pack()

        # Filling the canvas with columns of elements
        for i in range(0, count):
            arr.append(random.randint(0, 255))
        for i in range(0, count):
            color = '#'+'{:02X}'.format(arr[i])+'{:02X}'.format(255-arr[i])+'00'
            rect_arr.append(self.canvas.create_rectangle(
                10+rect_width*i, 10+(255-arr[i])*2, 10+rect_width+rect_width*i, 600, width = 0, fill=color))

        # Update window
        self.root.update()
        sleep(1)
        
        # Sort start
        function(arr, rect_arr, self, sleep_time)
        
        self.stop = True
        self.btn_start["state"] = "normal"



window = Window(asyncio.get_event_loop())
asyncio.run(window.show())

