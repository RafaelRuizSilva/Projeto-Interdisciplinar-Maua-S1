from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
from Planodefundo import PlanoDeFundo
import Voltar_Tela_Principal


class Sobre(PlanoDeFundo):

    def botao_voltar(self):
        self.voltar = Button(self.root,
                             text = 'Voltar',
                             font = 'Ariel 16',
                             borderwidth = 0,
                             fg = 'white',
                             bg = '#002240',
                             activebackground='#002240',
                             command = self.voltar_menu
                             )
        self.voltar.pack()
        self.voltar.place(x=50, y=510)


    def voltar_menu(self):
        try:
            self.btn_nivel1.destroy()
        except:
            pass
        try:
            self.btn_nivel2.destroy()
        except:
            pass
        try:
            self.btn_nivel3.destroy()
        except:
            pass
        try:
            self.label_fundo.destroy()
        except:
            pass
        
        tp = Voltar_Tela_Principal.TelaPrincipal('images/tela_principal.png', self.root)
        
        tp.orquestrador()


    def orquestradora(self):

        Sobre.botao_voltar(self)
