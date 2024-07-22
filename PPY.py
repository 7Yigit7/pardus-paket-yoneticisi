#Yazan Yiğit Çıtak
#Pardus için, Pardus ise özgürlük için :)

import tkinter as tk
from os import system

class pencere:#Pencere Sınıfı
    def __init__(self,
                 title="",
                 minsize1=0,
                 minsize2=0,
                 maxsize1=0,
                 maxsize2=0
                 ):
        self.title = title
        self.minsize1 = minsize1
        self.minsize2 = minsize2
        self.maxsize1 = maxsize1
        self.maxsize2 = maxsize2


gui_class = pencere(#Ana Pencere özellikleri
    title="Pardus Paket Yöneticisi",
    minsize1=600,
    minsize2=800,
    maxsize1=600,
    maxsize2=800,
    )

def paket_inst():
    install = paket_adi.get()
    system(f"sudo apt install {install}")
def upgrade():
    system("sudo apt upgrade")

gui = tk.Tk()

gui.title(gui_class.title)
gui.minsize(gui_class.minsize1,gui_class.minsize2)
gui.maxsize(gui_class.maxsize1,gui_class.maxsize2)

title = tk.Label(gui,
                 text="Pardus Paket Yöneticisi",
                 font=f"italic 20",
                 fg="black",
                 ).pack()

paket_gir = tk.Label(gui,
                     text="\n\nPaket adı girin",
                     font=f"italic 14",
                     fg="black",
                     ).pack()
paket_adi = tk.Entry(gui)
paket_adi.pack()
paket_kur = tk.Button(gui,
                      text="Kur",
                      font="italic 14",
                      bg="yellow",
                      command=paket_inst
                      ).pack()

bos = tk.Label(gui,text="\n\n\n\n").pack()

güncelle = tk.Button(gui,
                     text="Sistemi güncelle",
                     font="italic 20",
                     bg="yellow",
                     command=upgrade
                     ).pack()

v = tk.Label(gui,text="1.0").place(x=1,y=1)

gui.mainloop()
