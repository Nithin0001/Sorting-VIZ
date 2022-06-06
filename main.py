from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from Sort import *

window = Tk()
window.title("Sorting Visualization")
window.maxsize(1280, 720)
window.minsize(1280, 720)
window.configure(bg="white")

selected_algo = StringVar()
data = []
FONT_TXT = ("Poppins", 18, "bold")


# draw the rectangles
def drawData(data_, color):
    canvas.delete("all")
    c_height = 520
    c_width = 1280
    x_width = c_width / (len(data_) + 1)
    offset = 2
    spacing = 2
    normalized_data = [i / max(data_) for i in data_]
    for i, height in enumerate(normalized_data):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 500
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color[i], outline="#32de84")
        if check.get() == 1:
            canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data_[i]))
    window.update()


# rest
def reset():
    global canvas
    canvas.destroy()


# generate random arrays
def gene():
    global data, canvas
    canvas = Canvas(window, width=1290, height=520, bg="#dce1e3")
    canvas.grid(row=1, column=0)
    time_in_s.configure(text="0 s")
    window.update()
    data = []
    if size_entry.get() == '':
        messagebox.showerror("Array size empty", "Enter the array size")
    else:
        try:
            size = int(size_entry.get())
        except:
            messagebox.showerror("", "Enter integers only")
        if size < 0:
            size = 10
        if size > 1000:
            size = 300
        for _ in range(size):
            data.append(random.randrange(0, 1000))
    drawData(data, ["#7fcdcd" for x in range(len(data))])


# start the algo
def start_algo():
    if size_entry.get() == '':
        messagebox.showerror("Array size empty", "Enter the array size")
    if not size_entry.get() == '':
        if not canvas.find_all():
            messagebox.showerror("Array not generated", "Press the Generate Button")
    global data
    if alg_menu.get() == "Bubble Sort":
        time_spent = BubbleSort(data=data, drawdata=drawData, speed=speed.get())
        time_in_s.configure(text=f"{time_spent} s")
        messagebox.showinfo("", "Done")
    elif alg_menu.get() == "Insertion Sort":
        time_spent = InsertionSort(data=data, drawdata=drawData, speed=speed.get())
        time_in_s.configure(text=f"{time_spent} s")
        messagebox.showinfo("", "Done")
    elif alg_menu.get() == "Radix Sort":
        time_spent = RadixSort(data=data, drawdata=drawData, speed=speed.get())
        time_in_s.configure(text=f"{time_spent} s")
        messagebox.showinfo("", "Done")
    elif alg_menu.get() == "Shell Sort":
        time_spent = ShellSort(data=data, drawdata=drawData, speed=speed.get())
        time_in_s.configure(text=f"{time_spent} s")
        messagebox.showinfo("", "Done")
    elif alg_menu.get() == "Selection Sort":
        time_spent = SelectionSort(data=data, drawdata=drawData, speed=speed.get())
        time_in_s.configure(text=f"{time_spent} s")
        messagebox.showinfo("", "Done")
    elif alg_menu.get() == "Heap Sort":
        time_spent = HeapSort(data=data, drawdata=drawData, speed=speed.get())
        time_in_s.configure(text=f"{time_spent} s")
        messagebox.showinfo("", "Done")
    elif alg_menu.get() == "Merge Sort":
        time_spent = MergeSort(data=data, drawdata=drawData, speed=speed.get())
        time_in_s.configure(text=f"{time_spent} s")
        messagebox.showinfo("", "Done")
    elif alg_menu.get() == "Quick Sort":
        time_spent = QuickSort(data=data, drawdata=drawData, speed=speed.get(), head=0, tail=len(data) - 1)
        time_in_s.configure(text=f"{time_spent} s")
        messagebox.showinfo("", "Done")


# UI frame contains all the buttons
ui_frame = Frame(window, width=1290, height=200, bg="white")
ui_frame.grid(row=0, column=0, padx=10, pady=10)

# canvas
canvas = Canvas(window, width=1290, height=520, bg="#dce1e3")
canvas.grid(row=1, column=0)

# algorithm text and algorithm selection box
algo_text = StringVar()
algo_text.set("Algorithm")
Label(ui_frame, textvariable=algo_text, bg="white", font=FONT_TXT).grid(row=0, column=0, sticky=W)
combobox_font = ("Poppins", 15, "bold")
alg_menu = ttk.Combobox(ui_frame, textvariable=selected_algo,
                        values=["Bubble Sort", "Merge Sort", "Insertion Sort", "Quick Sort", "Selection Sort",
                                "Heap Sort", "Shell Sort", "Radix Sort"], font=combobox_font, state="readonly")
alg_menu.grid(row=1, column=0)
alg_menu.current(0)  # default selected algorithm at 0th index

# array size entry
Label(ui_frame, text="Size (Max 1000)", bg="white", font=FONT_TXT).grid(row=2, column=0, sticky=W)
size_entry = Entry(ui_frame, highlightthickness=2, highlightbackground="black")
size_entry.grid(row=3, column=0, sticky=W)

# waring if array size not selected
waring = Label(ui_frame, text="", bg="white", font=FONT_TXT)
waring.grid(row=2, column=2, sticky=W)

# button import i.e images
gene_img = PhotoImage(file=r"img/button_generate.png")
start_img = PhotoImage(file=r"img/button_start.jpeg")
Button(ui_frame, image=start_img, command=start_algo).grid(row=0, column=2)  # start button
Button(ui_frame, image=gene_img, command=gene).grid(row=0, column=3)  # generator button

# algo speed selector through slider
speed = Scale(ui_frame, from_=0.01, to=1.0, length=300, digits=3, resolution=0.01, orient=HORIZONTAL,
              label="Select Speed")
speed.grid(row=2, column=1)
speed.configure(font=FONT_TXT)

# check box
check = IntVar()
c = Checkbutton(ui_frame, text="Display Numbers", onvalue=1, offvalue=0, variable=check, font=FONT_TXT)
c.grid(row=0, column=1)
c.select()

# time spent
time_label = Label(ui_frame, text="Time Spent : ", font=FONT_TXT)
time_label.grid(row=1, column=1)

# time in s
time_in_s = Label(ui_frame, text="0 s", font=FONT_TXT)
time_in_s.grid(row=1, column=2)

# reset
reset_img = PhotoImage(file=r"/Users/nithinr/PycharmProjects/Sorting Visualization/img/button_reset.png")
reset_btn = Button(ui_frame, command=reset, image=reset_img)
reset_btn.grid(row=0, column=4)

window.mainloop()
