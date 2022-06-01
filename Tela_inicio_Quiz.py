from tkinter import *
from PIL import ImageTk, Image
import datetime
import pyodbc
from tkinter import messagebox
import pandas as pd
from placeholder import add_placeholder_to
from Sql_Conexao import sqlComandos
from Planodefundo import PlanoDeFundo
from tkinter import ttk
import Voltar_Tela_Principal
import Quiz_Jogo
import Messagebox

class Quiz(PlanoDeFundo):
    def __init__(self, imagem_fundo, root, nivel, nivel_num):
        super().__init__(imagem_fundo, root)

        self.nivel_num = nivel_num
        nivel = str(nivel) + ' '
        self.nivel = nivel
        self.sql = sqlComandos('DESKTOP-C10NOM4\SQLEXPRESS', 'PROJETO_MAUA')


    def base_pergunta_nivel(self, nivel):
        self.df = pd.read_sql_query('SELECT * FROM TBL_PERGUNTA', self.sql.conexao)
        self.df = self.df[self.df['NIVEL'] == nivel]


    def botao_voltar(self):
        self.voltar = Button(self.root,
                             text = 'Voltar',
                             font = 'Ariel 16',
                             borderwidth = 0,
                             fg = 'black',
                             bg = '#fff',
                             command = self.voltar_menu
                             )
        self.voltar.pack()
        self.voltar.place(x=60, y=510)

    def voltar_menu(self):
        self.label_fundo.destroy()
        try:
            self.alternativa_a.destroy()
            self.alternativa_b.destroy()
            self.alternativa_c.destroy()
            self.alternativa_d.destroy()
            self.btn_criar.destroy()
            self.pergunta.destroy()
            self.nivel.destroy()
            self.resp.destroy()
        except:
            pass
        try:
            self.voltar.destroy()
        except:
            pass

        tp = Voltar_Tela_Principal.TelaPrincipal('images/Tela_principal.png', self.root)

        tp.orquestrador()
        

    def inserindo_botao_começar(self):

        self.start = Button(self.root,
                             text = 'COMEÇAR',
                             font = 'Ariel 12',
                             borderwidth = 0,
                             fg = 'black',
                             bg = '#4285f4',
                             activebackground= '#4285f4',
                             command=self.valida_dados
                             )
        self.start.pack()
        self.start.place(width=100,height=30,x=840, y=515)


    def base_jogador(self):
        
        self.df_jogador = pd.read_sql_query('SELECT * FROM TBL_JOGADOR', self.sql.conexao)


    def inserindo_sql(self):
        query_insert = '''INSERT INTO TBL_JOGADOR(RA_JOGADOR, PONTUACAO, TEMPO, NIVEL)
                          VALUES (?, ?, ?, ?)
                        '''
        self.sql.cursor.execute(query_insert,  self.ra.get(), 0, '0', self.nivel)
        self.sql.conexao.commit()


    def valida_dados(self):
        try:
            if len(self.df['ID_PERGUNTA']) == 10:
                tam_valido = False
                if self.ra.get() == '' or self.ra.get() == 'RA: 00.00000-0:':
                    mb = Messagebox.MessageboxErro('images/messagebox.png','ERRO','Todos os campos são necessários')
                    mb.orquestradora()
                else:
                    if self.ra.get() in list(self.df_jogador['RA_JOGADOR']) and self.nivel in list(self.df_jogador[self.df_jogador['RA_JOGADOR'] == self.ra.get()]['NIVEL']):
                        mb = Messagebox.MessageboxErro('images/messagebox.png','ERRO','O RA digitado já realizaou esse Quiz')
                        mb.orquestradora()
                    else:
                        if len(self.ra.get()) != 10:
                            mb = Messagebox.MessageboxErro('images/messagebox.png','ERRO','O RA deve conter 10 caracters')
                            mb.orquestradora()
                        else:
                            self.inserindo_sql()
                            self.start_quiz_nivel(self.nivel_num)
                            print('RA INSERIDO COM SUCESSO')
            else:
                mb = Messagebox.MessageboxErro('images/messagebox.png','ERRO','Só pode iniciar o Quiz\ncom 10 perguntas')
                mb.orquestradora()

        except Exception as ex:
            print(ex)


    def start_quiz_nivel(self, nivel_num):
        self.label_fundo.destroy()

        qj = Quiz_Jogo.QuizJogo('images/quiz_jogo.png', self.root, nivel_num, self.get_ra())

        qj.orquestradora()


    def botao_hover(self):
        self.start.bind('<Enter>', self.button_hover)
        self.start.bind('<Leave>', self.button_leave)    


    def button_hover(self, e):
        self.start['fg'] = 'black'
        self.start['bg'] = '#50f0ff'
        

    def button_leave(self, e):
        self.start['fg'] = 'black'
        self.start['bg'] = '#4285f4'


    def input_nome_completo(self):
        self.ra = Entry(bg = 'white',
                          borderwidth=0,
                          width=42,
                          font='verdana 10'
                          )
        self.ra.pack()
        self.ra.place(x=100, y = 475)
        add_placeholder_to(self.ra,'RA: 00.00000-0:')

    def get_ra(self):
        return self.ra.get()

    def get_nivel(self):
        return self.nivel.get()

    def orquestradora(self):

        self.sql.criando_conexao_sql()

        Quiz.base_jogador(self)

        Quiz.base_pergunta_nivel(self, self.nivel)

        Quiz.input_nome_completo(self)

        Quiz.inserindo_botao_começar(self)

        Quiz.botao_hover(self)

        Quiz.botao_voltar(self)
        
   