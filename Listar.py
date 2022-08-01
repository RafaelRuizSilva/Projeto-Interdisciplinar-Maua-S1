from cgitb import text
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
import Voltar_Tela_Adm 

class ListarPerguntas(PlanoDeFundo):
    def __init__(self, imagem_fundo, root):
        super().__init__(imagem_fundo, root)

        self.sql = sqlComandos()


    def botao_listar(self):
        self.btn_listar = Button(self.root,
                                  text='LISTAR',
                                  width=200,
                                  height=30,
                                  font=('Verdana',14, 'bold'),
                                  bg = '#08B4B8',
                                  fg = '#fff',
                                  borderwidth=0)
        self.btn_listar.pack()
        self.btn_listar.place(width=100, height=45, x=526, y=485)


    def base_pergunta(self):
        self.df = pd.read_sql_query('SELECT * FROM TBL_PERGUNTA', self.sql.conexao)


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
        self.voltar.destroy()

        ta = Voltar_Tela_Adm.TelaAdm('images/Tela_adm.png', self.root)

        ta.orquestradora()


    def tabela(self):
        '''
            Criando tabela que mostrará as questões 
            existentes no Banco de dados

        '''
        s = ttk.Style()
        s.configure('Treeview',
                    rowheight=22,
                    background = '#92f5ec'
                    )

        s.map('Treeview',background=[('selected','#4285f4')])
        
        # CRIANDO LABEL PARA ARMAZENAR TABELA
        frame_tabela = LabelFrame(self.root,
                                  bg='white',
                                  borderwidth=0
                                  )
        frame_tabela.pack()
        frame_tabela.place(width=580, height=460, x=340, y=80)

        # LISTA DE COLUNAS
        colunas = ['column1','column2','column3','column4','column5','column6','column7','column8']

        # CRIANDO TREEVIEW
        tabela = ttk.Treeview(frame_tabela, columns=colunas, show='headings', height=460,)
        
        # DEFININDO LARGURA DAS COLUNAS
        tabela.column("column1", width=100, minwidth=50)
        tabela.column("column2", width=170, minwidth=50)
        tabela.column("column3", width=50, minwidth=50)
        tabela.column("column4", width=50, minwidth=50)
        tabela.column("column5", width=50, minwidth=50)
        tabela.column("column6", width=50, minwidth=50)
        tabela.column("column7", width=50, minwidth=50)
        tabela.column("column8", width=50, minwidth=50)

        # ALTERANDO NOME DAS COLUNAS
        tabela.heading('column1', text='ID_PERGUNTA')
        tabela.heading('column2', text='PERGUNTA')
        tabela.heading('column3', text='altA')
        tabela.heading('column4', text='altB')
        tabela.heading('column5', text='altC')
        tabela.heading('column6', text='altD')
        tabela.heading('column7', text='RESP')
        tabela.heading('column8', text='NIVEL')

        tabela.pack()
    

        tabela.tag_configure('linha_par', background='#cccccc')
        tabela.tag_configure('linha_impar', background='#92f5ec')
        # Alimentando a tabela com os dados da base do BD
        self.df.drop(['ID_PERGUNTA'], axis=1, inplace=True)
        self.df.reset_index(inplace=True)
        self.df.rename(columns = {'index':'ID_PERGUNTA'}, inplace=True)
        self.df['ID_PERGUNTA'] = self.df['ID_PERGUNTA'].apply(lambda x: int(x) + 1)

        lista_dados = list(zip(list(self.df['ID_PERGUNTA']), list(self.df['PERGUNTA']), list(self.df['altA']), list(self.df['altB']), list(self.df['altC']), list(self.df['altD']), list(self.df['RESP']), list(self.df['NIVEL'])))
        count = 0
        for v in lista_dados:
            if count % 2 == 0:
                tabela.insert(parent='', index='end',values=(v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7]), tags=('linha_par',))
            else:
                tabela.insert(parent='', index='end',values=(v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7]), tags=('linha_impar',))
            count += 1


    def orquestradora(self):
        self.sql.criando_conexao_sql()

        ListarPerguntas.base_pergunta(self)

        ListarPerguntas.botao_voltar(self)

        ListarPerguntas.tabela(self)
        