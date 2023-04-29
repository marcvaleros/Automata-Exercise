#Programming Assignment # 3

import tkinter as tk
bgcolor = "lightgray"

#init app
root = tk.Tk()
root.title("Automata Programming Exercise")
root.maxsize(800, 600)
#center app
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window width and height
window_width = 800
window_height = 600

# Calculate the x and y coordinates of the top-left corner of the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the geometry of the window
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

#frame widget (group elements tgt)
frame = tk.Frame(root)
frame.pack()



def clearString2():
    input_box.delete(0, tk.END)
    output_box.configure(text="", bg=bgcolor)


def checkLanguage():
    count_a, count_b, count_c = 0, 0, 0
    s = input_box.get().lower()
    for char in s:
        if char == 'a':
            count_a += 1
        elif char == 'b':
            count_b += 1
        elif char == 'c':
            count_c += 1
        else:
            output_box.configure(text="NO",bg="red",fg="white") 
        if count_b > count_a or count_c > count_b:
            output_box.configure(text="NO",bg="red",fg="white")

    if count_a == count_b and count_b == count_c:
        output_box.configure(text="YES",bg="green",fg="white")
    else:
        output_box.configure(text="NO",bg="red",fg="white")

frame2 = tk.LabelFrame(frame,text="EXERCISE III. ACCEPT A LANGUAGE L = {a^n b^n C^n / n >= 0}")
frame2.grid(row=1,column=0,pady=10)

input_box = tk.Entry(frame2, width=50)
input_box.grid(row=1,column=1, padx=10, pady=10)

output_box = tk.Label(frame2, text="", fg="green", bg=bgcolor, relief="ridge", wraplength=100, width=30, height=10)
output_box.grid(row=1,column=2,padx=10, pady=10)

btn3 = tk.Button(frame2, text="ENTER",cursor="hand2",relief="groove", command=lambda:checkLanguage()).grid(row=2, column=1, pady=10)

btn4 = tk.Button(frame2, text="CLEAR", cursor="hand2",relief="groove", command=lambda:clearString2()).grid(row=2, column=2, pady=10)

#run app
root.mainloop()