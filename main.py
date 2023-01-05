import tkinter as tk
from tkinter import ttk
import asyncio
import random


class App:
    async def exec(self):
        self.window = Window(asyncio.get_event_loop())
        await self.window.show()


class Window(tk.Tk):

    async def show(self):
        while True:
            self.root.update()
            await asyncio.sleep(0.1)

    def __init__(self, loop):
        self.win_wight = 600
        self.win_height = 800
        self.stop = False

        self.loop = loop
        self.root = tk.Tk()
        self.root.title('SortLib')
        self.root.wm_attributes('-alpha', 0.9)
        self.root.geometry(str(self.win_wight) + 'x' + str(self.win_height))
        self.root.resizable(width=False, height=False)

        self.frame = tk.Frame(bg='#ffffff')
        self.frame.place(relx=0.025, rely=0.15,
                         relheight=0.825, relwidth=0.95)
        self.canvas = tk.Canvas(self.frame)
        self.btn_stop = tk.Button(self.frame)

        self.entry = tk.Entry(width=20)
        self.entry.insert(0, '100')
        self.entry.grid(column=0, row=0, padx=10, pady=10)
        self.btn = tk.Button(text='Sort', bg='#f1f1ff',
                             command=lambda: self.loop.create_task(self.btn_click(int(self.entry.get()), (self.win_wight-50)/int(self.entry.get()), BubbleSort)))
        self.btn.grid(column=0, row=1, padx=10, pady=10)

    def stop_sort(self):
        self.stop = True

    async def btn_click(self, count, rect_wight, function):
        self.stop = False
        arr = []
        rect_arr = []

        self.canvas.destroy()
        self.btn_stop.destroy()
        self.canvas = tk.Canvas(self.frame, height=self.frame.winfo_height()-50,
                                width=self.frame.winfo_width(), bg='#f1f1f1')
        self.btn_stop = tk.Button(self.frame, text='Stop', bg='#ffc0c0',
                                  command=self.stop_sort, height=50,
                                  width=self.frame.winfo_width())
        self.canvas.pack(side='top')
        self.btn_stop.pack()

        for i in range(0, count):
            arr.append(random.randint(0, 255))
        for i in range(0, count):
            rect_arr.append(self.canvas.create_rectangle(
                10+rect_wight*i, 10+(255-arr[i])*2, 10+rect_wight+rect_wight*i, 600, fill='#'+'{:02X}'.format(arr[i])+'{:02X}'.format(255-arr[i])+'00'))
        await asyncio.sleep(2)

        function.sort(self=self, arr=arr, rect_arr=rect_arr)


class Function():
    def __init__() -> None:
        pass

    def sort(self):
        raise NotImplementedError("The method not implemented")


class BubbleSort(Function):
    def sort(self, arr, rect_arr):
        lenght = len(arr)
        for i in range(0, lenght):
            for j in range(i, lenght):
                if (arr[i] > arr[j]):
                    c = arr[i]
                    arr[i] = arr[j]
                    arr[j] = c
                    r_c0 = self.canvas.coords(rect_arr[i])[
                        0] - self.canvas.coords(rect_arr[j])[0]
                    self.canvas.move(rect_arr[i], -r_c0, 0)
                    self.canvas.move(rect_arr[j], r_c0, 0)
                    rect_temp = rect_arr[i]
                    rect_arr[i] = rect_arr[j]
                    rect_arr[j] = rect_temp
                    self.root.update()
            if (self.stop):
                break


asyncio.run(App().exec())
