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