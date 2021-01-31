from tkinter import *
from tkinter import ttk
from array_canvas import *

BACKGROUND_COLOR = "#2e2e2e"
SIDE_FRAME_COLOR = "#454545"
BUTTON_COLOR = "#458036"
BUTTON_CLICK_COLOR = "#54a33e"
BUTTON_FONT = ("Helvetica", 10, "bold")
FONT_CLICK_COLOR = "#616161"

class Frames :

    def __init__(self, root):

        self._side_frame = Frame(root, width=250, height=500, bg=SIDE_FRAME_COLOR)
        self._side_frame.pack_propagate(False)
        self._side_frame.grid_propagate(False)
        self._side_frame.pack(side="left")
        self.load_options(self._side_frame)

        self._main_frame = Frame(root, width=400, height=450)
        self._main_frame.configure(bg=BACKGROUND_COLOR)
        self._main_frame.pack(padx=75, pady=20)
    
    def load_sort_button(self, frame):
        self._sort_button = Button(frame, text="SORT", font=BUTTON_FONT)
        self._sort_button.config(command=lambda : self._array_canvas.start_sorting(self._sort_button, self._generate_button))
        self._sort_button.config(height=3, width=15, bd=0)
        self._sort_button.config(bg=BUTTON_COLOR, activebackground=BUTTON_CLICK_COLOR, activeforeground=FONT_CLICK_COLOR, fg="white", disabledforeground="white")
        self._sort_button.pack()

    def load_options(self, frame):
        self._sorting_button = Button(frame, text="SORTING", font=BUTTON_FONT, command=lambda : self.load_sorting_options(frame))
        self._sorting_button.config(bg=BUTTON_COLOR, activebackground=BUTTON_CLICK_COLOR, activeforeground=FONT_CLICK_COLOR, fg="white")
        self._sorting_button.config(height=2, width=10, bd=0)

        self._searching_button = Button(frame, text="SEARCHING", font=BUTTON_FONT)
        self._searching_button.config(bg=BUTTON_COLOR, activebackground=BUTTON_CLICK_COLOR, activeforeground=FONT_CLICK_COLOR, fg="white")
        self._searching_button.config(height=2, width=10, bd=0)
        
        self._sorting_button.grid(row=0, column=0, padx=25, pady=20)
        self._searching_button.grid(row=0, column=1)

    def load_sorting_options(self, frame):
        self._sorting_button.config(state=DISABLED, disabledforeground="white")
        self._searching_button.config(state=DISABLED, bg="#2a4f20")

        self.load_reset_button(frame)

        self._bubble_sort_button = Button(frame, text="BUBBLE", font=BUTTON_FONT, command=self.bubble_sort)
        self._bubble_sort_button.config(bg=BUTTON_COLOR, activebackground=BUTTON_CLICK_COLOR, activeforeground=FONT_CLICK_COLOR, fg="white")
        self._bubble_sort_button.config(bd=0)
        self._bubble_sort_button.grid(row=1, column=0)

    def bubble_sort(self):
        self._alg = "BUBBLE"
        self._bubble_sort_button.config(state=DISABLED, disabledforeground="white")
        self.load_generate_button()
        self.load_size_speed_sliders()

    def load_size_speed_sliders(self):
        self._array_size_slider = Scale(self._side_frame, from_=1, to=100, orient=HORIZONTAL)
        self._array_size_slider.config(font=BUTTON_FONT)
        self._array_size_slider.config(fg="white", activebackground=BUTTON_CLICK_COLOR, highlightbackground=SIDE_FRAME_COLOR, troughcolor=BACKGROUND_COLOR)
        self._array_size_slider.config(bd=0, length=200)
        self._array_size_slider.config(sliderrelief='flat', highlightthickness=0, background=SIDE_FRAME_COLOR)
        self._array_size_slider.config(label="ARRAY SIZE:")
        self._array_size_slider.config(command=self.slider_func)
        
        self._speed_slider = Scale(self._side_frame, from_=1, to=100, orient=HORIZONTAL)
        self._speed_slider.config(font=BUTTON_FONT)
        self._speed_slider.config(fg="white", activebackground=BUTTON_CLICK_COLOR, highlightbackground=SIDE_FRAME_COLOR, troughcolor=BACKGROUND_COLOR)
        self._speed_slider.config(bd=0, length=200)
        self._speed_slider.config(sliderrelief='flat', highlightthickness=0, background=SIDE_FRAME_COLOR)
        self._speed_slider.config(label="SPEED:")
        self._speed_slider.config(command=self.slider_func)

        self._array_size_slider.place(x=25,y=200)
        self._speed_slider.place(x=25,y=275)

    def slider_func(self, value):
        self._generate_button.destroy()
        self.load_generate_button()

    def load_generate_button(self):
        self._generate_button = Button(self._side_frame, text="GENERATE", font=BUTTON_FONT)
        self._generate_button.config(command=self.generate)
        self._generate_button.config(bg=BUTTON_COLOR, activebackground=BUTTON_CLICK_COLOR, activeforeground=FONT_CLICK_COLOR, fg="white")
        self._generate_button.config(height=3, bd=0)
        self._generate_button.pack(side="bottom", ipadx=50)

    def generate(self):
        self.reset_main_frame()
        size = self._array_size_slider.get()
        speed = 101 - self._speed_slider.get()
        self._array_canvas = ArrayCanvas(root=self._main_frame, width=400, height=250, size=size, speed=speed)
        self.load_sort_button(self._main_frame)
        self._generate_button.config(state=DISABLED, bg="#2a4f20")

    def load_reset_button(self, frame):
        self._reset_button = Button(frame, text="RESET SETTINGS", font=BUTTON_FONT)
        self._reset_button.config(command=self.reset_side_frame)
        self._reset_button.config(bg="#ab0000", activebackground="#850000", activeforeground=FONT_CLICK_COLOR, fg="white")
        self._reset_button.config(bd=0)
        self._reset_button.pack(side="bottom", ipadx=50, pady=15)

    def reset_side_frame(self):
        for widget in self._side_frame.winfo_children():
            widget.destroy()
        self.load_options(self._side_frame)

    def reset_main_frame(self):
        for widget in self._main_frame.winfo_children():
            widget.destroy()
        