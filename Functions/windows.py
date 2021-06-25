import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="Hello Felix")
label = tk.Label(
    text="Hello Felix", fg="White", bg="Black", width=10, height=10
)
button=tk.Button(
    text ="Click me",
    width=25,
    height=5,
    bg="blue",
    fg="yellow"
)
entry=tk.Entry(fg="yellow",bg="blue",width =60
               )
greeting.pack()
label.pack()
button.pack()
entry.pack()
window.mainloop()
