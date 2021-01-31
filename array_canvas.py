from tkinter import *
from random import randrange
import time

CANVAS_COLOR = "#454545"
ARRAY_COLOR = "#dbdbdb"
SWAP_COLOR = "#f74f4f"
NO_SWAP_COLOR = "#458036"

class ArrayItem :

    def __init__(self, canvas, width, height, coordinate, canvas_height):
        self._canvas = canvas
        self._width = width
        self._height = height
        self._coordinate = coordinate
        self._canvas_height = canvas_height
        self._rectangle = self.create()
        self._sorted = False

    def get_height(self):
        return self._height

    def get_coordinate(self):
        return self._coordinate

    def get_rectangle(self):
        return self._rectangle

    def set_coordinate(self, coordinate):
        self._coordinate = coordinate


    def create(self):
        rectangle = self._canvas.create_rectangle(self._coordinate, 
                                     self._canvas_height - self._height, 
                                     self._coordinate + self._width, 
                                     self._canvas_height + 2, 
                                     width=1,
                                     fill=ARRAY_COLOR)
        return rectangle

    def update(self):
        self._canvas.delete(self._rectangle)
        self._rectangle = self._canvas.create_rectangle(self._coordinate, 
                                     self._canvas_height - self._height, 
                                     self._coordinate + self._width, 
                                     self._canvas_height + 2, 
                                     width=1,
                                     fill=ARRAY_COLOR)


class ArrayCanvas(Canvas):

    def __init__(self, root, width, height, size, speed):
        self._root = root
        self._width = width
        self._height = height
        self._size = size
        self._speed = speed
        self._sorting = True

        self._canvas = self.create_canvas()
        self._array = self.create_array(self._canvas)

    def create_canvas(self):
        canvas = Canvas(self._root, width=self._width, height=self._height, bg=CANVAS_COLOR, highlightthickness=2)
        canvas.pack(pady=50)
        return canvas

    def create_array(self, canvas):
        array = []
        for i in range(self._size):
            item_width = self._width / self._size
            item_height = randrange(self._height)
            item_coordinate = i * item_width

            array_item = ArrayItem(canvas, item_width, item_height, item_coordinate, self._height)

            array.append(array_item)

        return array

    def print_array(self):
        array_str = "["
        for i in self._array:
            array_str += str(i.get_height())
            array_str += ", "
        array_str += "]"
        print(array_str)

    def height(self):
        return self._height

    def get_array(self):
        return self._array

    def get_canvas(self):
        return self._canvas

    def bubble_sort_helper(self, current, stop_at):
        if(self._sorting):
            for rect in self._array:
                self._canvas.itemconfig(rect.get_rectangle(), fill=ARRAY_COLOR)

            if(current == stop_at):
                return

            if(self._array[current].get_height() > self._array[current+1].get_height()):
                # Swap visual
                self.swap(self._array[current], self._array[current+1])

                # Change to red
                self._canvas.itemconfig(self._array[current].get_rectangle(), fill=SWAP_COLOR)
                self._canvas.itemconfig(self._array[current+1].get_rectangle(), fill=SWAP_COLOR)

                # Swap actual
                temp = self._array[current]
                self._array[current] = self._array[current+1]
                self._array[current+1] = temp
            else:
                self._canvas.itemconfig(self._array[current].get_rectangle(), fill=NO_SWAP_COLOR)
                self._canvas.itemconfig(self._array[current+1].get_rectangle(), fill=NO_SWAP_COLOR)

            self._root.after(self._speed, self.bubble_sort_helper, current+1, stop_at)

    def bubble_sort(self, n, button, generate_button):
        if(self._sorting):
            if(n == 1):
                self.sorted(button, generate_button)
                return

            self.bubble_sort_helper(0, n-1)

            waiting_time = round((self._speed + (self._speed / 3)) * n)
            self._root.after(waiting_time, self.bubble_sort, n-1, button, generate_button)

    def sorted(self, button, generate_button):
        self._sorting = False

        for rect in self._array:
                self._canvas.itemconfig(rect.get_rectangle(), fill=ARRAY_COLOR)

        button.config(text="SORTED")
        button.config(bg="#3663f7", activebackground="#3663f7")
        button.config(state=DISABLED)

        generate_button.config(state=NORMAL, bg="#458036")

    def reset(self, button, generate_button):
        self._sorting = False
        self._canvas.delete("all")
        self._array = self.create_array(self._canvas)

        button.config(command=lambda : self.start_sorting(button, generate_button))
        button.config(bg="#458036")
        button.config(text="SORT")
        button.config(activebackground="#54a33e")

    def start_sorting(self, button, generate_button):
        self._sorting = True

        button.config(command=lambda : self.reset(button, generate_button))
        button.config(bg="#ab0000")
        button.config(text="RESET")
        button.config(activebackground="#850000")

        self.bubble_sort(len(self._array), button, generate_button)

    def swap(self, rect_1, rect_2):
        temp = rect_1.get_coordinate()
        rect_1.set_coordinate(rect_2.get_coordinate())
        rect_2.set_coordinate(temp)

        rect_1.update()
        rect_2.update()



