import tkinter as tk

window = tk.Tk()


def akmens(event):
  lbl_lietizv ["text"] = "Tava izvēle:akmens"
  dat_izvele()

def papirs(event):
  lbl_lietizv ["text"] = "Tava izvēle:papīrīts"
  dat_izvele()


def skeres(event):
  lbl_lietizv ["text"] = "Tava izvēle:šķēres"
  dat_izvele()

def dat_izvele():
  izvēle = ["akmens","šķēres","papīrīts"]
  datizv = random.choice(izveeles)
  lbl_datoraizv["text"] = f"Datora izvēle:{datizv}"

def rezultati():
  dators = lbl_datoraizv["text"]
  lietotajs = lbl_lietizv["text"]
  lietotajs = lietotajs.split()
  

  if dators[2] == lietotajs[2]:
   lbl_rezultats["text"] = "Rezultats: neizšķirts"
   
  else:
   lbl_rezultats["text"] = "vēl jāsataisa"
  



window = tk.Tk()



lbl_info = tk.Label(text = "SVEIKI!\n Šī ir spēle akmens,šķēres, papīrīts!")

lbl_darit = tk.Label(text = "Izvēlies kadu no piedāvātajiem variantiem:")

lbl_lietizv = tk.Label()
lbl_datoraizv = tk.Label()
lbl_rezultats = tk.Label()

btn_akmens = tk.Button(text = "akmens")
btn_skeres = tk.Button(text = "šķēres")
btn_papirs = tk.Button(text = "papīrīts")

btn_akmens.bind("<Button-1>",akmens)
btn_skeres.bind("<Button-1>",skeres)
btn_papirs.bind("<Button-1>",papirs)




lbl_info.pack(fill = tk.x)
lbl_darit.pack()
lbl_lietizv.pack()
lbl_datoraizv.pack()
lbl_rezultats.pack()
lbl_datoraizv.pack()
lbl_rezultats.pack()


window.mainloop()