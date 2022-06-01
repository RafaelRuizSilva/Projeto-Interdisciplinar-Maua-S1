from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from numpy import true_divide
import pandas as pd
from pip import main
from Tela_Nivel_Perguntas import TelaNivelPerguntas
import Tela_Login
import Tela_Nivel_Perguntas
import Sobre
import Tela_Tutorial


class TelaPrincipal():
    def __init__(self, imagem_fundo):
        self.principal = Tk()

        # Definindo a dimensão da interface
        self.principal.geometry('989x570')

        # Definindo título para a interface
        self.principal.title('SQL World')

        # Restringindo para não mecher nas dimensões da tela
        self.principal.resizable(False, False)

        # Colocando fundo
        self.fundo = ImageTk.PhotoImage(Image.open(imagem_fundo))

        # Criando label para colocar o fundo
        self.label_fundo = Label(self.principal, image=self.fundo)
        self.label_fundo.pack()


    def centralizar_interface(self):

        '''
            Centraliza a tela de cadastro no meio do monitor
        '''

        largura = 989
        altura = 570
        largura_screen = self.principal.winfo_screenwidth()
        altura_screen = self.principal.winfo_screenheight()
        posx = largura_screen/2 - largura/2
        posy = altura_screen/2 - altura/2
        self.principal.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))



    def botao_jogar(self):
        self.btn_jogar = Button(self.principal,
                                 text='Jogar',
                                 font='Copper 20 bold',
                                 fg='white',
                                 bg='#08B4B8',
                                 borderwidth=False,
                                 height=45,
                                 width=105,
                                 activebackground='#08B4B8',
                                 command=self.abrir_tela_niveis
                                 )
        self.btn_jogar.pack()
        self.btn_jogar.place(width=205, height=70, x=210, y=455)


    def botao_tutorial(self):
        self.btn_tutorial = Button(self.principal,
                                 text='Tutorial',
                                 font='Copper 20 bold',
                                 fg='white',
                                 bg='orange',
                                 borderwidth=False,
                                 height=45,
                                 width=105,
                                 activebackground='orange',
                                 command = self.abrir_tutorial
                                 )
        self.btn_tutorial.pack()
        self.btn_tutorial.place(width=205, height=70, x=580, y=455)


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

        tt = Tela_Tutorial.TelaTutorial('images/TelaModulosTutorial.png', self.principal)

        tt.orquestradora()


    def hover_botao(self, botao, cor_enter, cor_leave):
        botao.bind("<Enter>", func=lambda e: botao.config( 
        background=cor_enter)) 
  
    
        botao.bind("<Leave>", func=lambda e: botao.config( 
        background=cor_leave)) 
   

    def label_bemvindo(self):
        texto = StringVar()
        texto.set(f'Que tal \n aprender SQL? ')
        self.bem_vindo = Label(self.principal,
                          font = 'Arial 14',
                          fg = 'black',
                          bg = 'white',
                          textvariable = texto,
                        )
        self.bem_vindo.pack()
        self.bem_vindo.place(x=120, y=40)


    def label_sobre(self):
        self.sobre = Button(self.principal,
                                font = 'Arial 16',
                                fg = 'white',
                                bg = '#002240',
                                text = 'Sobre',
                                borderwidth = 0,
                                activebackground='#002240'
                                )
        self.sobre.pack()
        self.sobre.bind('<Enter>', self.button_hover)
        self.sobre.bind('<Leave>', self.button_leave)
        self.sobre.place(x=860, y=48)

    
    def button_hover(self, e):
        self.sobre['fg'] = '#a725e7'


    def button_leave(self, e):
        self.sobre['fg'] = 'white'


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
        tn = Tela_Nivel_Perguntas.TelaNivelPerguntas('images/TelaNivelPerguntas.png', self.principal)

        # Rodando orquestradora
        tn.orquestradora()


    def botao_sobre(self):
        self.sobre = Button(self.principal,
                                font = 'Arial 16',
                                fg = 'white',
                                bg = '#002240',
                                text = 'Sobre',
                                borderwidth = 0,
                                activebackground='#002240',
                                command = self.abrir_sobre
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

        sb = Sobre.Sobre('images/sobre.png', self.principal)

        sb.orquestradora()
        

    def executar(self):
        
        self.principal.mainloop()


    def botao_logout(self):
        sair = Button(self.principal,
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
        self.principal.destroy()

        login = Tela_Login.Login('images/TelaLogin.png')

        login.orquestradora()

    def orquestrador(self):

        TelaPrincipal.centralizar_interface(self)

        TelaPrincipal.botao_jogar(self)

        TelaPrincipal.botao_tutorial(self)

        TelaPrincipal.hover_botao(self, self.btn_jogar,'#00b8ff', '#08B4B8')

        TelaPrincipal.hover_botao(self, self.btn_tutorial, '#ff8f00','#e99c10')

        TelaPrincipal.label_bemvindo(self)

        TelaPrincipal.label_sobre(self)

        TelaPrincipal.botao_sobre(self)

        TelaPrincipal.botao_logout(self)

        TelaPrincipal.executar(self)

        

        
