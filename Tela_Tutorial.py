from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
from Planodefundo import PlanoDeFundo
import Voltar_Tela_Principal
import Slides_Tutorial_Nivel2
import Slides_Tutorial_Nivel1
import Slides_Tutorial_Nivel3


class TelaTutorial(PlanoDeFundo):

    def nivel1(self):
        self.btn_mod1 = Button(self.root,
                                 text='Nível 1 - Introdução',
                                 font='Verdana 13',
                                 fg='black',
                                 bg='#33C8EB',
                                 borderwidth=False,
                                 height=45,
                                 width=105,
                                 activebackground='#33C8EB',
                                 command=self.abrir_slide_1
                                 )
        self.btn_mod1.pack()
        self.btn_mod1.place(width=300, height=55,  x=375, y=260)


    def nivel2(self):
        self.btn_mod2 = Button(self.root,
                                 text='Nível 2 - Principais comandos',
                                 font='Verdana 13',
                                 fg='black',
                                 bg='#3D97E1',
                                 borderwidth=False,
                                 height=45,
                                 width=105,
                                 activebackground='#3D97E1',
                                 command=self.abrir_slide_2
                                 )
        self.btn_mod2.pack()
        self.btn_mod2.place(width=300, height=55, x=375, y=360)

    
    def nivel3(self):
        self.btn_mod3 = Button(self.root,
                                 text='Nível 3 - Consultas avançadas',
                                 font='Verdana 13',
                                 fg='black',
                                 bg='#5B30D4',
                                 borderwidth=False,
                                 height=45,
                                 width=105,
                                 activebackground='#5B30D4',
                                 command = self.abrir_slide_3
                                 )
        self.btn_mod3.pack()
        self.btn_mod3.place(width=300, height=55, x=375, y=460)


    def voltar_menu(self):
        self.btn_mod1.destroy()
        self.btn_mod2.destroy()
        self.btn_mod3.destroy()
        self.label_fundo.destroy()
        
        vp = Voltar_Tela_Principal.TelaPrincipal('images/tela_principal.png', self.root)

        vp.orquestrador()


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


    def botao_hover(self):
        self.btn_mod1.bind('<Enter>', self.button_hover)
        self.btn_mod1.bind('<Leave>', self.button_leave)    


    def button_hover(self, e):
        self.btn_mod1['fg'] = 'white'


    def button_leave(self, e):
        self.btn_mod1['fg'] = 'black'


    def botao_hover2(self):
        self.btn_mod2.bind('<Enter>', self.button_hover2)
        self.btn_mod2.bind('<Leave>', self.button_leave2)  


    def button_hover2(self, e):
        self.btn_mod2['fg'] = 'white'


    def button_leave2(self, e):
        self.btn_mod2['fg'] = 'black'


    def botao_hover3(self):
        self.btn_mod3.bind('<Enter>', self.button_hover3)
        self.btn_mod3.bind('<Leave>', self.button_leave3)  


    def button_hover3(self, e):
        self.btn_mod3['fg'] = 'white'


    def button_leave3(self, e):
        self.btn_mod3['fg'] = 'black'

    
    def abrir_slide_3(self):
        try:
            self.btn_mod1.destroy()
        except:
            pass
        try:
            self.btn_mod2.destroy()
        except:
            pass
        try:
            self.btn_mod3.destroy()
        except:
            pass
        try:
            self.voltar.destroy()
        except:
            pass
        try:
            self.label_fundo.destroy()
        except:
            pass
        
        
        slide3 = Slides_Tutorial_Nivel3.Slide1('slidesTutorial/innerjoin.png', self.root)

        slide3.orquestradora()


    def abrir_slide_2(self):

        try:
            self.btn_mod1.destroy()
        except:
            pass
        try:
            self.btn_mod2.destroy()
        except:
            pass
        try:
            self.btn_mod3.destroy()
        except:
            pass
        try:
            self.voltar.destroy()
        except:
            pass
        try:
            self.label_fundo.destroy()
        except:
            pass
        
        
        slide2 = Slides_Tutorial_Nivel2.Slide1('slidesTutorial/database.png', self.root)

        slide2.orquestradora()

    def abrir_slide_1(self):
        try:
            self.btn_mod1.destroy()
        except:
            pass
        try:
            self.btn_mod2.destroy()
        except:
            pass
        try:
            self.btn_mod3.destroy()
        except:
            pass
        try:
            self.voltar.destroy()
        except:
            pass
        try:
            self.label_fundo.destroy()
        except:
            pass
        
        
        slide1 = Slides_Tutorial_Nivel1.Slide1('slidesTutorial/Slide1.png', self.root)

        slide1.orquestradora()


    def orquestradora(self):

        TelaTutorial.nivel1(self)

        TelaTutorial.nivel2(self)
        
        TelaTutorial.nivel3(self)

        TelaTutorial.botao_hover(self)

        TelaTutorial.botao_hover2(self)

        TelaTutorial.botao_hover3(self)

        TelaTutorial.botao_voltar(self)
