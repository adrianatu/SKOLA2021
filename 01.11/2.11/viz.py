import tkinter as tk 

window = tk.Tk()

label = tk.Label(
  text = "Teksts!Teksts Teksts",
  foreground = "red",
  background = "black"
  )

label1 = tk.Label(
  text = "čau!",
  fg = "red",
  bg = "black",
  width = 11,
  height = 7
 )

label.pack()
label1.pack()

window.mainloop()

