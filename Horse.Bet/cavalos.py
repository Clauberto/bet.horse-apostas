from tkinter import *
from openpyxl import load_workbook
import pandas as pd


class Cavalos():
    
    book = pd.ExcelFile('BetHorse.xlsx')
    cava = book.parse("Cavalos")
    
    


    def __init__(self, cavalos):
        self.cavalos = cavalos
        self.cavalos.geometry("550x500")
        self.cavalos.title("bet.horse: Cavalos")
        self.__numCavalo01 = self.cava['Cavalos'][0]
        self.__numCavalo02 = self.cava['Cavalos'][1]
        self.__numCavalo03 = self.cava['Cavalos'][2]
        self.__numCavalo04 = self.cava['Cavalos'][3]
        self.chances01 = self.cava['Chances'][0]
        self.chances02 = self.cava['Chances'][1]
        self.chances03 = self.cava['Chances'][2]
        self.chances04 = self.cava['Chances'][3]
        self.multiplicador01 = (50/self.chances01) + 1
        self.multiplicador02 = (50/self.chances02) + 1
        self.multiplicador03 = (50/self.chances03) + 1
        self.multiplicador04 = (50/self.chances04) + 1
        self.debug()

    @property
    def numCavalo01(self):
        return self.__numCavalo01

    @numCavalo01.setter
    def numCavalo01(self,novo__numCavalo01):
        raise ValueError("Impossível alterar o numCavalo01 diretamente, use o metodo!")


    @property
    def numCavalo02(self):
        return self.__numCavalo02

    @numCavalo02.setter
    def numCavalo02(self,novo__numCavalo02):
        raise ValueError("Impossível alterar o numCavalo02 diretamente, use o metodo!")
    
    @property
    def numCavalo03(self):
        return self.__numCavalo03

    @numCavalo03.setter
    def numCavalo03(self,novo__numCavalo03):
        raise ValueError("Impossível alterar o numCavalo03 diretamente, use o metodo!")


    @property
    def numCavalo04(self):
        return self.__numCavalo04

    @numCavalo04.setter
    def numCavalo04(self,novo__numCavalo04):
        raise ValueError("Impossível alterar o numCavalo04 diretamente, use o metodo!")




    def debug(self):

        Label(self.cavalos, text=self.__numCavalo01).place(x=50, y=250)
        Label(self.cavalos, text=self.__numCavalo02).place(x=175, y=250)
        Label(self.cavalos, text=self.__numCavalo03).place(x=300, y=250)
        Label(self.cavalos, text=self.__numCavalo04).place(x=425, y=250)

        Label(self.cavalos, text="Chances: "+str(self.chances01)+"%").place(x=50, y=275)
        Label(self.cavalos, text="Chances: "+str(self.chances02)+"%").place(x=175, y=275)
        Label(self.cavalos, text="Chances: "+str(self.chances03)+"%").place(x=300, y=275)
        Label(self.cavalos, text="Chances: "+str(self.chances04)+"%").place(x=425, y=275)

        Label(self.cavalos, text="Multiplicador: "+str("%.2f" %self.multiplicador01)+"X").place(x=50, y=300)
        Label(self.cavalos, text="Multiplicador: "+str("%.2f" %self.multiplicador02)+"X").place(x=175, y=300)
        Label(self.cavalos, text="Multiplicador: "+str("%.2f" %self.multiplicador03)+"X").place(x=300, y=300)
        Label(self.cavalos, text="Multiplicador: "+str("%.2f" %self.multiplicador04)+"X").place(x=425, y=300)

        Button(self.cavalos, text="Apostas", command=self.cavalos.destroy, bg="red", fg="white", width=15).place(x=200, y=370)


    
