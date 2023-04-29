#Programming Assignment # 2

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
    input_box2.delete(0, tk.END)
    output_box2.configure(text="", bg=bgcolor)


def count_string():
    s = input_box2.get().lower()
    a_count = s.count('a')
    b_count = s.count('b')

    if a_count % 2 == 0 and b_count %2 != 0:
      output_box2.configure(text="YES",bg="green",fg="white")
    else: 
      output_box2.configure(text="NO",bg="red",fg="white")

frame2 = tk.LabelFrame(frame,text="EXERCISE II. ACCEPT STRING WITH EVEN A's & ODD B's")
frame2.grid(row=1,column=0,pady=10)

input_box2 = tk.Entry(frame2, width=50)
input_box2.grid(row=1,column=1, padx=10, pady=10)

output_box2 = tk.Label(frame2, text="", fg="green", bg=bgcolor, relief="ridge", wraplength=100, width=30, height=10)
output_box2.grid(row=1,column=2,padx=10, pady=10)

btn3 = tk.Button(frame2, text="ENTER",cursor="hand2",relief="groove", command=lambda:count_string()).grid(row=2, column=1, pady=10)

btn4 = tk.Button(frame2, text="CLEAR", cursor="hand2",relief="groove", command=lambda:clearString2()).grid(row=2, column=2, pady=10)

#run app
root.mainloop()