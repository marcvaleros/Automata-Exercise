import tkinter as tk

#init app
root = tk.Tk()
root.title("Automata Programming Exercise")

#center app
x= root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight() * 0.1)
root.geometry('500x600+' + str(x) + '+' + str(y))

#frame widget (group elements tgt)
frame1 = tk.Frame(root, width=500, height=600, bg="#3d6466")
frame1.grid(row=0,column=0)
frame1.pack_propagate(False)

tk.Label(frame1, text="Enter the string to be reversed:").pack()

# create an input box
input_box = tk.Entry(frame1)
input_box.pack()  # add it to the window


#run app
root.mainloop()