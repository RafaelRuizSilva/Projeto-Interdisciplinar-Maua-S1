from tkinter import *
from PIL import ImageTk, Image
import datetime
import pyodbc
from tkinter import messagebox
import pandas as pd
from placeholder import add_placeholder_to
from Sql_Conexao import sqlComandos
import Tela_Login
import warnings
import Criar
from Planodefundo import PlanoDeFundo
import Listar
import Atualizar
import Deletar
import Ranking

class TelaAdm(PlanoDeFundo):
    def __init__(self, imagem_fundo, root):
        super().__init__(imagem_fundo, root)


    def centralizando_menu_adm(self):

        '''
            Centraliza a tela de LOGIN no meio do monitor
        '''

        largura = 989
        altura = 570
        largura_screen = self.root.winfo_screenwidth()
        altura_screen = self.root.winfo_screenheight()
        posx = largura_screen / 2 - largura / 2
        posy = altura_screen / 2 - altura / 2
        self.root.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))

    
    def inserindo_botao_criar(self):

        self.borda_btn_criar = Frame(self.root,
                          highlightthickness=1,
                          highlightbackground="white",)

        self.btn_criar = Button(self.borda_btn_criar,
                                 text='CRIAR',
                                 font='Verdana 14 bold',
                                 fg='white',
                                 bg='#5b46c7',
                                 borderwidth=False,
                                 height=45,
                                 width=105,
                                 activebackground='#5b46c7',
                                 command=self.criar_pergunta
                                 )
        self.btn_criar.pack()
        self.borda_btn_criar.pack()
        self.borda_btn_criar.place(width=135, height=48, x=320, y=200)


    def inserindo_botao_listar(self):

        self.borda_btn_listar = Frame(self.root,
                                    highlightthickness=1,
                                    highlightbackground="white",)

        self.btn_listar = Button(self.borda_btn_listar,
                                 text='LISTAR',
                                 font='Verdana 14 bold',
                                 fg='white',
                                 bg='#43b7b7',
                                 borderwidth=False,
                                 height=45,
                                 width=105,
                                 activebackground='#43b7b7',
                                 command=self.listar_pergunta
                                 )
        self.btn_listar.pack()
        self.borda_btn_listar.pack()
        self.borda_btn_listar.place(width=135, height=48, x=490, y=200)

    def inserindo_botao_atualizar(self):
        self.borda_btn_atualizar = Frame(self.root,
                                    highlightthickness=1,
                                    highlightbackground="white",)

        self.btn_atualizar = Button(self.borda_btn_atualizar,
                                 text='ATUALIZAR',
                                 font='Verdana 14 bold',
                                 fg='white',
                                 bg='#4285f4',
                                 borderwidth=False,
                                 height=45,
                                 width=105,
                                 activebackground='#4285f4',
                                 command = self.atualizar_pergunta
                                 )
        self.btn_atualizar.pack()
        self.borda_btn_atualizar.pack()
        self.borda_btn_atualizar.place(width=135, height=48, x=670, y=200)

    
    def inserindo_botao_deletar(self):
        self.borda_btn_deletar = Frame(self.root,
                                    highlightthickness=1,
                                    highlightbackground="white",)

        self.btn_deletar = Button(self.borda_btn_deletar,
                                 text='DELETAR',
                                 font='Verdana 14 bold',
                                 fg='white',
                                 bg='#ea4335',
                                 borderwidth=False,
                                 height=45,
                                 width=105,
                                 activebackground='#ea4335',
                                 command=self.deletar_pergunta
                                 )
        self.btn_deletar.pack()
        self.borda_btn_deletar.pack()
        self.borda_btn_deletar.place(width=135, height=48, x=845, y=200)


    def inserindo_botao_pontuacao(self):
        self.borda_btn_pontuacao = Frame(self.root,
                                    highlightthickness=1,
                                    highlightbackground="white",)

        self.btn_pontuacao = Button(self.borda_btn_pontuacao,
                                 text='RANKING',
                                 font='Verdana 14 bold',
                                 fg='white',
                                 bg='#fbbc05',
                                 borderwidth=False,
                                 height=45,
                                 width=105,
                                 activebackground='#fbbc05',
                                 command=self.ranking
                                 )
        self.btn_pontuacao.pack()
        self.borda_btn_pontuacao.pack()
        self.borda_btn_pontuacao.place(width=135, height=48, x=340, y=510)

    def label_ranking(self):
        self.label_rank = Label(text='Ranking Quiz',
                                bg = 'white',
                                borderwidth=0,
                                font='Verdana 13 bold')
        self.label_rank.pack()
        self.label_rank.place(x=340, y=485)


    def ranking(self):
        self.label_fundo.destroy()
        
        rank = Ranking.Ranking('images/Ranking.png', self.root)

        rank.orquestradora()


    def deletar_pergunta(self):
        self.label_fundo.destroy()

        delet = Deletar.Deletar('images/deletar.png', self.root)

        delet.orquestradora()


    def atualizar_pergunta(self):
        self.label_fundo.destroy()

        atualizar = Atualizar.Atualizar('images/Atualizar.png', self.root)

        atualizar.orquestradora()


    def listar_pergunta(self):
        self.label_fundo.destroy()
        self.borda_btn_criar.destroy()
        self.btn_criar.destroy()
        self.borda_btn_listar.destroy()
        self.btn_listar.destroy()

        listar = Listar.ListarPerguntas('images/listar.png', self.root)

        listar.orquestradora()

    def criar_pergunta(self):
        self.label_fundo.destroy()
        self.borda_btn_criar.destroy()
        self.btn_criar.destroy()
        self.borda_btn_listar.destroy()
        self.btn_listar.destroy()
        
        criar = Criar.Criar('images/perguntas.png', self.root)

        criar.orquestradora()


    def botao_logout(self):

        self.borda_btn_sair = Frame(self.root,
                                    highlightthickness=1,
                                    highlightbackground="#71E8EB",)

        self.btn_sair = Button(self.borda_btn_sair,
                      text = 'Log Out',
                      bg = '#71E8EB',
                      font= 'verdana 13',
                      activebackground='#71E8EB',
                      fg = 'black',
                      borderwidth = 0,
                      command = self.voltar_login,
                      )
        self.btn_sair.pack()
        self.borda_btn_sair.pack()
        self.borda_btn_sair.place(x = 210, y = 520)


    def voltar_login(self):
        self.root.destroy()

        login = Tela_Login.Login('images/TelaLogin.png')

        login.orquestradora()


    def orquestradora(self):

        TelaAdm.centralizando_menu_adm(self)

        TelaAdm.inserindo_botao_criar(self)

        TelaAdm.inserindo_botao_listar(self)

        TelaAdm.inserindo_botao_atualizar(self)

        TelaAdm.inserindo_botao_deletar(self)

        TelaAdm.inserindo_botao_pontuacao(self)

        TelaAdm.label_ranking(self)

        TelaAdm.botao_logout(self)
