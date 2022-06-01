from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pandas as pd
from pip import main
from Planodefundo import PlanoDeFundo
import Tela_Login
import Tela_Nivel_Perguntas
import Sobre
import Tela_Tutorial 

class TelaPrincipal(PlanoDeFundo):

    def botao_jogar(self):
        self.btn_jogar = Button(self.root,
                                 text='Jogar',
                                 font='Copper 20 bold',
                                 fg='white',
                                 bg='#08B4B8',
                                 borderwidth=False,
                                 height=45,
                                 width=105,
                                 command=self.abrir_tela_niveis,
                                 activebackground='#08B4B8'
                                 )
        self.btn_jogar.pack()
        self.btn_jogar.place(width=205, height=70, x=210, y=455)


    def abrir_tela_niveis(self):
        try:
            self.btn_jogar.destroy()
        except:
            pass
        try:
            self.btn_tutorial.destroy()
        except:
            pass
        try:
            self.bem_vindo.destroy()
        except:
            pass
        try:
            self.label_fundo.destroy()
        except:
            pass
        try:
            self.sobre.destroy()
        except:
            pass

        # Abrindo Tela de nivel das perguntas
        tn = Tela_Nivel_Perguntas.TelaNivelPerguntas('images/TelaNivelPerguntas.png', self.root)

        # Rodando orquestradora
        tn.orquestradora()


    def abrir_tutorial(self):
        try:
            self.btn_jogar.destroy()
        except:
            pass
        try:
            self.btn_tutorial.destroy()
        except:
            pass
        try:
            self.bem_vindo.destroy()
        except:
            pass
        try:
            self.label_fundo.destroy()
        except:
            pass
        try:
            self.sobre.destroy()
        except:
            pass

        tt = Tela_Tutorial.TelaTutorial('images/TelaModulosTutorial.png', self.root)

        tt.orquestradora()


    def botao_tutorial(self):
        self.btn_tutorial = Button(self.root,
                                 text='Tutorial',
                                 font='Copper 20 bold',
                                 fg='white',
                                 bg='orange',
                                 borderwidth=False,
                                 height=45,
                                 width=105,
                                 activebackground='orange',
                                 command=self.abrir_tutorial
                                 )
        self.btn_tutorial.pack()
        self.btn_tutorial.place(width=205, height=70, x=580, y=455)


    def hover_botao(self, botao, cor_enter, cor_leave):
        botao.bind("<Enter>", func=lambda e: botao.config( 
        background=cor_enter)) 
  
    
        botao.bind("<Leave>", func=lambda e: botao.config( 
        background=cor_leave)) 
   

    def label_bemvindo(self):
        texto = StringVar()
        texto.set(f'Que tal \n aprender SQL? ')
        self.bem_vindo = Label(self.root,
                          font = 'Arial 14',
                          fg = 'black',
                          bg = 'white',
                          textvariable = texto)
        self.bem_vindo.pack()
        self.bem_vindo.place(x=120, y=40)


    def botao_sobre(self):
        self.sobre = Button(self.root,
                                font = 'Arial 16',
                                fg = 'white',
                                bg = '#002240',
                                text = 'Sobre',
                                borderwidth = 0,
                                command = self.abrir_sobre,
                                activebackground='#002240'
                                )
        self.sobre.pack()
        self.sobre.bind('<Enter>', self.button_hover)
        self.sobre.bind('<Leave>', self.button_leave)
        self.sobre.place(x=860, y=48)


    def abrir_sobre(self):
        try:
            self.btn_jogar.destroy()
        except:
            pass
        try:
            self.btn_tutorial.destroy()
        except:
            pass
        try:
            self.bem_vindo.destroy()
        except:
            pass
        try:
            self.label_fundo.destroy()
        except:
            pass
        try:
            self.sobre.destroy()
        except:
            pass

        sb = Sobre.Sobre('images/sobre.png', self.root)

        sb.orquestradora()


    def button_hover(self, e):
        self.sobre['fg'] = '#a725e7'


    def button_leave(self, e):
        self.sobre['fg'] = 'white'

    def botao_logout(self):
        sair = Button(self.root,
                      text = 'Log Out',
                      bg = '#002240',
                      font= 'verdana 13',
                      activebackground='#002240',
                      fg = 'white',
                      borderwidth = 0,
                      command = self.voltar_login
                      )
        sair.pack()
        sair.place(x = 40, y = 520)

    def voltar_login(self):
        self.root.destroy()

        login = Tela_Login.Login('images/TelaLogin.png')

        login.orquestradora()

    def orquestrador(self):

        TelaPrincipal.botao_jogar(self)

        TelaPrincipal.botao_tutorial(self)

        TelaPrincipal.hover_botao(self, self.btn_jogar,'#00b8ff', '#08B4B8')

        TelaPrincipal.hover_botao(self, self.btn_tutorial, '#ff8f00','#e99c10')

        TelaPrincipal.label_bemvindo(self)

        TelaPrincipal.botao_sobre(self)

        TelaPrincipal.botao_logout(self)
