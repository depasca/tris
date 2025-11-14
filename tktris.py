import tkinter as tk
w = tk.Tk()
title = tk.Label(text="Tetris Game")
# title.pack()


for i in range(3):
    for j in range(3):
        btn = tk.Button(text=f"{i}{j}")
        btn.grid(row=i, column=j)


w.mainloop()
