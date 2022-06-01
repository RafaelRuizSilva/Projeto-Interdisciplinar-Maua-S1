from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
from Planodefundo import PlanoDeFundo
import Voltar_Tela_Principal
import Tela_inicio_Quiz

class TelaNivelPerguntas(PlanoDeFundo):
    
    
    def nivel1(self):
        self.btn_nivel1 = Button(self.root,
                                 text='Nível 1 - Básico ',
                                 font='Verdana 14',
                                 fg='black',
                                 bg='#33C8EB',
                                 borderwidth=False,
                                 height=45,
                                 width=105,
                                 activebackground='#33C8EB',
                                 command = self.abrir_quiz_nivel1
                                 )
        self.btn_nivel1.pack()
        self.btn_nivel1.place(width=320, height=57, x=325, y=260)


    def nivel2(self):
        self.btn_nivel2 = Button(self.root,
                                 text='Nível 2 - Intermediário',
                                 font='Verdana 14',
                                 fg='black',
                                 bg='#3D97E1',
                                 borderwidth=False,
                                 height=45,
                                 width=105,
                                 activebackground='#3D97E1',
                                 command=self.abrir_quiz_nivel2
                                 )
        self.btn_nivel2.pack()
        self.btn_nivel2.place(width=320, height=62, x=325, y=350)

    
    def nivel3(self):
        self.btn_nivel3 = Button(self.root,
                                 text='Nível 3 - Avançado',
                                 font='Verdana 14',
                                 fg='black',
                                 bg='#5B30D4',
                                 borderwidth=False,
                                 height=45,
                                 width=105,
                                 activebackground='#5B30D4',
                                 command=self.abrir_quiz_nivel3
                                 )
        self.btn_nivel3.pack()
        self.btn_nivel3.place(width=320, height=62, x=325, y=445)


    def voltar_menu(self):
        self.btn_nivel1.destroy()
        self.btn_nivel2.destroy()
        self.btn_nivel3.destroy()
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
                             command = self.voltar_menu,
                             activebackground='#002240'
                             )
        self.voltar.pack()
        self.voltar.place(x=50, y=510)

    def botao_hover(self):
        self.btn_nivel1.bind('<Enter>', self.button_hover)
        self.btn_nivel1.bind('<Leave>', self.button_leave)    


    def button_hover(self, e):
        self.btn_nivel1['fg'] = 'white'

    def button_leave(self, e):
        self.btn_nivel1['fg'] = 'black'

    def botao_hover2(self):
        self.btn_nivel2.bind('<Enter>', self.button_hover2)
        self.btn_nivel2.bind('<Leave>', self.button_leave2)  


    def button_hover2(self, e):
        self.btn_nivel2['fg'] = 'white'

    def button_leave2(self, e):
        self.btn_nivel2['fg'] = 'black'

    def botao_hover3(self):
        self.btn_nivel3.bind('<Enter>', self.button_hover3)
        self.btn_nivel3.bind('<Leave>', self.button_leave3)  


    def button_hover3(self, e):
        self.btn_nivel3['fg'] = 'white'

    def button_leave3(self, e):
        self.btn_nivel3['fg'] = 'black'

        
    def abrir_quiz_nivel1(self):
        self.label_fundo.destroy()

        q = Tela_inicio_Quiz.Quiz('images/quiz.png', self.root, 1, 1)

        q.orquestradora()


    def abrir_quiz_nivel2(self):
        self.label_fundo.destroy()

        q = Tela_inicio_Quiz.Quiz('images/quiz.png', self.root, 2, 2)

        q.orquestradora()

    
    def abrir_quiz_nivel3(self):
        self.label_fundo.destroy()

        q = Tela_inicio_Quiz.Quiz('images/quiz.png', self.root, 3, 3)

        q.orquestradora()

    def orquestradora(self):

        TelaNivelPerguntas.nivel1(self)

        TelaNivelPerguntas.nivel2(self)
        
        TelaNivelPerguntas.nivel3(self)

        TelaNivelPerguntas.botao_hover(self)

        TelaNivelPerguntas.botao_hover2(self)

        TelaNivelPerguntas.botao_hover3(self)

        TelaNivelPerguntas.botao_voltar(self)





