from random import random
from tkinter import *
from tkinter import messagebox
from cavalos import Cavalos
import random
import pandas as pd

class Bethorse():

    book = pd.ExcelFile('BetHorse.xlsx')
    cava = book.parse("Cavalos")

    def __init__(self, master):
        self.master = master
        self.master.geometry("500x500")
        self.master.title("bet.horse: Apostas de Joquei")
        self.valorApostado = DoubleVar()
        self.cavaloEscolhido = self.cava['Cavalos'][0]
        self.multiplicadorEscolhido = DoubleVar()
        self.chancesEscolhido = self.cava['Chances'][0]
        self.__nCavalo = IntVar()
        self.vencedor = IntVar()
        self.debug()

    @property
    def nCavalo(self):
        return self.__nCavalo

    @nCavalo.setter
    def nCavalo(self,novo_nCavalo):
        raise ValueError("Impossível alterar o nCavalo diretamente, use o metodo!")

    def debug(self):
        Label(self.master, text="Valor Apostado").place(x=175, y=250)
        valorApostado = Entry(self.master, textvariable=self.valorApostado)
        valorApostado.place(x=175, y=270)

        Label(self.master, text="Número Cavalo").place(x=175, y=300)
        __nCavalo = Entry(self.master, textvariable=self.__nCavalo)
        __nCavalo.place(x=175, y=320)

        
        Button(self.master, text="Cavalos", command=self.cavalos, bg="red", fg="white", width=15).place(x=180, y=370)

        Button(self.master, text="Apostar", command=self.aposta, bg="red", fg="white", width=15).place(x=180, y=400)


    def cavalos(self):
        Cavalo = Cavalos(Tk())
        Cavalo.cavalos.mainloop()

    def aposta(self):
        resultado = random.randint(1, 100)
        cava01 = self.cava['Chances'][0]
        cava02 = self.cava['Chances'][1]
        cava03 = self.cava['Chances'][2]

        if (resultado <= cava01):
            self.vencedor = 1
            
        elif (resultado > cava01 and resultado <= (100 - cava02)):
            self.vencedor = 2

        elif (resultado > (100 - cava02) and resultado <= (100 - cava03)):
            self.vencedor = 3

        else:
            self.vencedor = 4

        if (self.__nCavalo.get() == 1):
            self.cavaloEscolhido = self.cava['Cavalos'][0]
            self.multiplicadorEscolhido = (50/float(self.cava['Chances'][0]))+1
            self.chancesEscolhido = self.cava['Chances'][0]
            
            

        if (self.__nCavalo.get() == 2):
            self.cavaloEscolhido = self.cava['Cavalos'][1]
            self.multiplicadorEscolhido = (50/float(self.cava['Chances'][1]))+1
            self.chancesEscolhido = self.cava['Chances'][1]
            
        

        if (self.__nCavalo.get() == 3):
            self.cavaloEscolhido = self.cava['Cavalos'][2]
            self.multiplicadorEscolhido = (50/float(self.cava['Chances'][2]))+1
            self.chancesEscolhido = self.cava['Chances'][2]

        if (self.__nCavalo.get() == 4):
            self.cavaloEscolhido = self.cava['Cavalos'][3]
            self.multiplicadorEscolhido = (50/float(self.cava['Chances'][3]))+1
            self.chancesEscolhido = self.cava['Chances'][3]
        
        if (self.vencedor == self.__nCavalo.get()):
            messagebox.showinfo("Resultado de Aposta", "VENCEU"
                                                        +"\nCavalo Apostado: "+str(self.cavaloEscolhido)
                                                        +"\nChances de Ganhar: "+str(self.chancesEscolhido)+"%"
                                                        +"\nValor Apostado: "+str(self.valorApostado.get())
                                                        +"\nMultiplicador: "+str("%.2f" %self.multiplicadorEscolhido)+"X"
                                                        +"\nDinheiro Ganho: "+str("%.2f" %((self.valorApostado.get())*(self.multiplicadorEscolhido))))  
        else:
            messagebox.showinfo("Resultado de Aposta", "PERDEU"
                                                        +"\nCavalo Apostado: "+str(self.cavaloEscolhido)
                                                        +"\nChances de Ganhar: "+str(self.chancesEscolhido)+"%"
                                                        +"\nValor Apostado: "+str(self.valorApostado.get())
                                                        +"\nMultiplicador: "+str("%.2f" %self.multiplicadorEscolhido)+"X"
                                                        +"\nDinheiro Perdido: "+str("%.2f" %(self.valorApostado.get())))          
       



