class Sort():
    def __init__(self):
        self.array = []
        self.rect_array = []
    
    def swap(self, arr, rect_arr, canvas, k, m, root):
        c = arr[m]
        arr[m] = arr[k]
        arr[k] = c
        r_c0 = canvas.coords(rect_arr[m])[
            0] - canvas.coords(rect_arr[k])[0]
        canvas.move(rect_arr[m], -r_c0, 0)
        canvas.move(rect_arr[k], r_c0, 0)
        rect_temp = rect_arr[m]
        rect_arr[m] = rect_arr[k]
        rect_arr[k] = rect_temp
        root.update()

    def BubbleSort(self, canvas, arr, rect_arr, stop, root, window_self):
        lenght = len(arr)
        print(arr)

        for i in range(0, lenght):
            for j in range(i+1, lenght):
                if (arr[i] > arr[j]):
                   self.swap(arr, rect_arr, canvas, i, j, root)
            if (window_self.stop):
                break

    def printt(self):
        print("Hello")
