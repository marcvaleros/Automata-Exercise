#Programming Assignment # 4
# Write a program that computes the conversion of an octal string into a binary string such that the numeric value remains the same. Leading zeros are allowed for the input, but not for the output (except for result 0). For example, input “1031” yields output “1000011001”, since 10318 = 537 = 10000110012, and input “00507” yields output “101000111”, since 5078 = 327 = 1010001112.

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


#label for rev string input
frame1 = tk.LabelFrame(frame,text="EXERCISE IV. CONVERTS OCTAL STRING TO BINARY STRING")
frame1.grid(row=0, column=0,pady=30)


input_box = tk.Entry(frame1, width=50)
input_box.grid(row=1,column=1, padx=10, pady=10)

output_box = tk.Label(frame1, text="", fg="green", bg=bgcolor, relief="ridge", wraplength=100, width=30, height=10)
output_box.grid(row=1,column=2,padx=10, pady=10)

btn1 = tk.Button(frame1, text="ENTER",cursor="hand2",relief="groove", command=lambda:octaltobinary()).grid(row=2, column=1, pady=10)

btn2 = tk.Button(frame1, text="CLEAR", cursor="hand2",relief="groove", command=lambda:clearString()).grid(row=2, column=2, pady=10)

#run app
root.mainloop()

#function to convert octal string to binary string
def octaltobinary(): 
    input_text = input_box.get()
    octal_num = int(input_text, 8)
    binary_string = bin(octal_num)[2:]
    binary_string = binary_string.lstrip('0') or '0'
    output_box.configure(text= binary_string)

def clearString():
    input_box.delete(0, tk.END)
    output_box.configure(text="")