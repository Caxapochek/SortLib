
from time import sleep
import asyncio

class Sort:
    def __init__(self):
        self.array = []
        self.rect_array = []
    

    def swap(self, arr, rect_arr, k, m, window_self, sleep_time):
        c = arr[m]
        arr[m] = arr[k]
        arr[k] = c
        m_coord = window_self.canvas.coords(rect_arr[m])[0]
        k_coord = window_self.canvas.coords(rect_arr[k])[0]
        dif = m_coord - k_coord
        window_self.canvas.move(rect_arr[m], -dif, 0)
        window_self.canvas.move(rect_arr[k], dif, 0)
        rect_temp = rect_arr[m]
        rect_arr[m] = rect_arr[k]
        rect_arr[k] = rect_temp
        window_self.root.update()
        sleep(sleep_time)


    def BubbleSort(self, arr, rect_arr, window_self, sleep_time):
        lenght = len(arr)
        swaped = True
        for i in range(0, lenght):
            swaped = False
            for j in range(lenght-1, 0, -1):
                if (arr[j] > arr[j-1]):
                   self.swap(arr, rect_arr, j, j-1, window_self, sleep_time)
                   swaped = True
                if (window_self.stop):
                    break
            if not swaped:
                break


    def CocktailSort(self, arr, rect_arr, window_self, sleep_time):
        lenght = len(arr)
        swaped = True
        while(swaped):
            swaped = False
            for i in range(0, lenght-2):
                if(arr[i]>arr[i+1] and not window_self.stop):
                    self.swap(arr, rect_arr, i, i+1, window_self, sleep_time)
                    swaped = True
            if(not swaped):
                break
            swaped = False
            for i in range(lenght-2,-1,-1):
                if(arr[i]>arr[i+1] and not window_self.stop):
                    self.swap(arr, rect_arr, i, i+1, window_self, sleep_time)
                    swaped = True
                    if (window_self.stop):
                        break

