import tkinter as tk
import random
from time import sleep

# Define required data structures and variables
data = []
sorting_algorithm = None

# Sorting algorithms
def bubble_sort(data):
    n = len(data)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
                yield data
        if not swapped:
            break

def merge_sort(data):
    if len(data) > 1:
        mid = len(data)//2
        left_half = data[:mid]
        right_half = data[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
                yield data
            else:
                data[k] = right_half[j]
                j += 1
                yield data
            k += 1
        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1
            yield data
        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1
            yield data

# GUI class
class GUI(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Sorting Algorithm Visualizer")
        self.master.geometry("600x400")
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        # Input field
        self.input_label = tk.Label(self, text="Enter comma-separated numbers:")
        self.input_label.grid(row=0, column=0, pady=(10, 0))
        self.input_field = tk.Entry(self)
        self.input_field.grid(row=1, column=0)

        # Buttons frame
        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.grid(row=2, column=0, pady=(20, 0))

        # Sort button
        self.sort_button = tk.Button(self.buttons_frame, text="Sort", command=self.sort_data, width=10)
        self.sort_button.pack(side=tk.LEFT)

        # Shuffle button
        self.shuffle_button = tk.Button(self.buttons_frame, text="Shuffle", command=self.shuffle_data, width=10)
        self.shuffle_button.pack(side=tk.LEFT, padx=5)

        # Reset button
        self.reset_button = tk.Button(self.buttons_frame, text="Reset", command=self.reset_data, width=10)
        self.reset_button.pack(side=tk.LEFT)

        # Algorithm selector
        self.algorithm_label = tk.Label(self, text="Select algorithm:")
        self.algorithm_label.grid(row=3, column=0, pady=(20, 0))
        self.algorithm_selector = tk.StringVar(value="Bubble Sort")
        self.algorithm_dropdown = tk.OptionMenu(self, self.algorithm_selector, "Bubble Sort", "Merge Sort")
        self.algorithm_dropdown.grid(row=4, column=0)

        # Speed slider
        self.speed_label = tk.Label(self, text="Speed:")
        self.speed_label.grid(row=5, column=0, pady=(20, 0))
        self.speed_slider = tk.Scale(self, from_=1, to=100, orient=tk.HORIZONTAL)
        self.speed_slider.set(50)
        self.speed_slider.grid(row=6, column=0)

        # Canvas
        self.canvas = tk.Canvas(self, width=580, height=250, bg="white")
        self.canvas.grid(row=0, column=1, rowspan=7, padx=(20, 0))

    def sort_data(self):
        global data, sorting_algorithm
        data_str = self.input_field.get()
        try:
            data = list(map(int, data_str.split(",")))
            sorting_algorithm = self.algorithm_selector.get()
        except ValueError:
            return
        if sorting_algorithm == "Bubble Sort":
            self.visualize_sorting(bubble_sort(data))
        elif sorting_algorithm == "Merge Sort":
            self.visualize_sorting(merge_sort(data))

    def shuffle_data(self):
        global data
        random.shuffle(data)
        self.draw_bars()

    def reset_data(self):
        global data
        data = []
        self.input_field.delete(0, tk.END)
        self.canvas.delete("all")

    def draw_bars(self):
        self.canvas.delete("all")
        x0, y0, x1, y1 = 10, 230, 30, 250
        for i in range(len(data)):
            self.canvas.create_rectangle(x0, y0-data[i], x1, y1, fill="gray")
            x0 += 20
            x1 += 20

    def visualize_sorting(self, sorting_generator):
        self.sort_button.config(state=tk.DISABLED)
        self.shuffle_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)
        self.algorithm_dropdown.config(state=tk.DISABLED)
        speed = (100 - self.speed_slider.get()) / 100
        for data in sorting_generator:
            self.draw_bars()
            self.canvas.update()
            sleep(speed)
        self.draw_bars()
        self.sort_button.config(state=tk.NORMAL)
        self.shuffle_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.NORMAL)
        self.algorithm_dropdown.config(state=tk.NORMAL)

# Main function
def main():
    # Create GUI
    root = tk.Tk()
    app = GUI(master=root)
    app.mainloop()

if __name__ == '__main__':
    main()
