import tkinter as tk
import random
import time

start = time.time()
class Application(tk.Frame):
    def init(self, master=None):
        super().init(master)
        self.grid()
        self.create_widgets()

    def create_table(self, size):
        row = col = size
        numbers = list(range(1, row * col + 1))
        random.shuffle(numbers)
        return [numbers[i:i + row] for i in range(0, len(numbers), col)]
    num = 1
    def populateMethod(self, method):
        #print(self.num)
        if self.num <= 25:
            if method == self.num:
                self.num = self.num + 1
                print ("clicked:", method)
            else:
                print("Error, expecting ", self.num)
        else: 
            print ("Training is over")

    def create_widgets(self):
        self.count = self.create_table(5)
        for row in self.count:
            for n in row:
                self.b = tk.Button(self, height = 1, width = 3, font=("Times New Roman", 44), text=n,
                command=lambda method=n: self.populateMethod(method))
                self.b.grid(row=self.count.index(row), column=row.index(n))



root = tk.Tk()
app = Application(master=root)
app.mainloop()
end = time.time()
print("time: ", end - start)
