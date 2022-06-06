from tkinter import *
from PIL import Image,Image as img  
from tkinter import filedialog as fd
from convertHSV import RGB_HSV
from time import sleep, time
from corpo import Gartic
import random
import os
import pyautogui
import threading




class Tela:
    
    def __init__(self, window):
        foto = ''
        self.window = window
        self.window.title("Gartic AutoDraw")
        self.window.geometry("280x390")
        self.window.iconbitmap("imagens/faviconpequeno.ico")
        self.window.resizable(width=0, height=0)
        self.window.configure(background='#44475a')
        #=========frame menu ============="
        self.frame1 = LabelFrame(self.window,text="Status")
        self.frame1.place(relwidth=1, relheight=0.4)
        #=====================Botões1 ================================
        self.btb1 =Button(self.window,text="Browser Image",bg="#6272a4",fg="white",font=("bungee",9,"normal"),command=self.browser)
        self.btb1.place(x=178, y=160, width=100, height=30)
        #=======================Botões2=============================#
        self.btb2 =Button(self.window,text="START",bg="#ffb86c",fg="white",font=("Ariel",9,"normal"),command=self.main)
        self.btb2.place(x=178, y=195, width=100, height=30)
        #================= TEXT ONDE FICA X E Y  ==============================#
        self.btb3 =Label(self.window,text="Press [q] position on screen",bg="#ff5555",fg="white",anchor=W,font=("Ariel",9,"normal"))
        self.btb3.place(x=3, y=160, width=170, height=20)
        #================= TEXT ONDE FICA X E Y ==============================#
        self.btb4 =Label(self.window,text="Press [r] position on palete de cores",bg="#ff5555",fg="white",anchor=W,font=("Ariel",9,"normal"))
        self.btb4.place(x=3, y=230, width=200, height=20)
        #==========================Text Status ===================#
        self.status = Listbox(self.frame1)
        self.status.place(relwidth=1, relheight=1)
        #===============Key press ================#
        self.window.bind("<q>",self.position)

        #===============Key press ================#
        self.window.bind("<r>",self.paleta_)
        #========================================#
        self.pos= StringVar()
        self.posicao = Label(self.window,textvariable=self.pos)
        self.posicao.place(x=30, y=180, width=100, height=20)
        #==============================================
        self.pl= StringVar()
        self.palet = Label(self.window,textvariable=self.pl)
        self.palet.place(x=30, y=250, width=100, height=20)

        #======================================
        self.btb3 =Label(self.window,text="Made in Khufos",bg="#44475a",fg="white",font=("Arial CE",9,"bold"))
        self.btb3.place(x=100, y=360, width=100, height=30)



    def browser(self):
        global foto
        self.filename = fd.askopenfilename(initialdir=os.getcwd(), title="Select A File", filetypes=(("jpg files", "*.jpg"),("PNG file","*.png"),("all files", "*.*")))

    def paleta_(self,event):
        global paleta_x 
        global paleta_y 
        paleta_x , paleta_y = pyautogui.position()
        self.pl.set('X = % d, Y = % d'%(paleta_x, paleta_y))


    def position(self,event):
        global pos_x 
        global pos_y
        pos_x , pos_y = pyautogui.position()
        self.pos.set('X = % d, Y = % d'%(pos_x, pos_y))


    def contagem(self):
        global count
        self.status.delete(0, END)
        self.status.insert(0,"Iniciando AutoDraw")
        #window.update() # allow window to catch up
        #sleep(1)
        for count in range(5,0,-1):
            msg = f'Contagem Regressiva {count}...'
            self.status.insert(8,msg)
            window.update() # allow window to catch up
            sleep(1)
            
                
    def main(self):
        try:
            self.contagem()
            a = Gartic(paleta_x,paleta_y,pos_x,pos_y,self.filename)
            a.paleta_cor()
            a.paleta_cruz()
            a.paleta_seta()
            a.paleta_autodraw()
        except:
            self.status.insert(8,"Tente de novo! Não acho alguma func paleta")




window=Tk()
Tela(window)
window.mainloop()