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
import Messagebox


class Deletar(PlanoDeFundo):
    def __init__(self, imagem_fundo, root):
        super().__init__(imagem_fundo, root)

        self.sql = sqlComandos('DESKTOP-C10NOM4\SQLEXPRESS', 'PROJETO_MAUA')
        

    def botao_deletar(self):
        self.btn_deletar = Button(self.root,
                                  text='DELETAR',
                                  width=200,
                                  height=30,
                                  font=('Verdana',12, 'bold'),
                                  bg = '#ea4335',
                                  fg = '#fff',
                                  borderwidth=0,
                                  command=self.deletar_pergunta
                                  )
        self.btn_deletar.pack()
        self.btn_deletar.place(width=110, height=45, x=576, y=485)


    def deletar_pergunta(self):
        
        try:
            item_selecionado = self.tabela.selection()[0]
            valores = self.tabela.item(item_selecionado, 'values')
            query_deletar = '''DELETE TBL_PERGUNTA WHERE PERGUNTA = ?'''
            deseja_deletar = messagebox.askyesno('DELETAR',f'Deseja deletar a questão número {valores[0]}?')
            print('\033[1;35mPergunta deletada com sucesso\033[m')
            if deseja_deletar:
                self.sql.cursor.execute(query_deletar, valores[1])
                self.sql.conexao.commit()
                self.voltar_menu()
                self.tabela.delete(item_selecionado)
            else:
                pass
        except:
            mi = Messagebox.MessageboxErro('images/messagebox.png','ERRO', 'Selecione um item da tabela')
            mi.orquestradora()
        

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
        try:
            self.alternativa_a.destroy()
            self.alternativa_b.destroy()
            self.alternativa_c.destroy()
            self.alternativa_d.destroy()
        except:
            pass
        try:
            self.btn_criar.destroy()
        except:
            pass
        try:
            self.pergunta.destroy()
            self.nivel.destroy()
            self.resp.destroy()
        except:
            pass
        try:
            self.voltar.destroy()
        except:
            pass

        ta = Voltar_Tela_Adm.TelaAdm('images/Tela_adm.png', self.root)

        ta.orquestradora()
        

    def insere_tabela(self):
        '''
            Criando tabela que mostrará as questões 
            existentes no Banco de dados

        '''
        s = ttk.Style()
        s.configure('Treeview',
                    rowheight=22,
                    background = '#92f5ec',
                    
                    )

        s.map('Treeview',background=[('selected','#4285f4')])
        
        # CRIANDO LABEL PARA ARMAZENAR TABELA
        frame_tabela = LabelFrame(self.root,
                                  bg='white',
                                  borderwidth=0
                                  )
        frame_tabela.pack()
        frame_tabela.place(width=580, height=400, x=340, y=80)

        # LISTA DE COLUNAS
        colunas = ['column1','column2','column3','column4','column5','column6','column7','column8']

        # CRIANDO TREEVIEW
        self.tabela = ttk.Treeview(frame_tabela, columns=colunas, show='headings', height=460,)
        
        # DEFININDO LARGURA DAS COLUNAS
        self.tabela.column("column1", width=100, minwidth=50)
        self.tabela.column("column2", width=170, minwidth=50)
        self.tabela.column("column3", width=50, minwidth=50)
        self.tabela.column("column4", width=50, minwidth=50)
        self.tabela.column("column5", width=50, minwidth=50)
        self.tabela.column("column6", width=50, minwidth=50)
        self.tabela.column("column7", width=50, minwidth=50)
        self.tabela.column("column8", width=50, minwidth=50)

        # ALTERANDO NOME DAS COLUNAS
        self.tabela.heading('column1', text='ID_PERGUNTA')
        self.tabela.heading('column2', text='PERGUNTA')
        self.tabela.heading('column3', text='altA')
        self.tabela.heading('column4', text='altB')
        self.tabela.heading('column5', text='altC')
        self.tabela.heading('column6', text='altD')
        self.tabela.heading('column7', text='RESP')
        self.tabela.heading('column8', text='NIVEL')

        self.tabela.pack()
    

        self.tabela.tag_configure('linha_par', background='#cccccc')
        self.tabela.tag_configure('linha_impar', background='#92f5ec')
        # Alimentando a tabela com os dados da base do BD
        self.df.drop(['ID_PERGUNTA'], axis=1, inplace=True)
        self.df.reset_index(inplace=True)
        self.df.rename(columns = {'index':'ID_PERGUNTA'}, inplace=True)
        self.df['ID_PERGUNTA'] = self.df['ID_PERGUNTA'].apply(lambda x: int(x) + 1)

        lista_dados = list(zip(list(self.df['ID_PERGUNTA']), list(self.df['PERGUNTA']), list(self.df['altA']), list(self.df['altB']), list(self.df['altC']), list(self.df['altD']), list(self.df['RESP']), list(self.df['NIVEL'])))
        count = 0
        for v in lista_dados:
            if count % 2 == 0:
                self.tabela.insert(parent='', index='end',values=(v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7]), tags=('linha_par',))
            else:
                self.tabela.insert(parent='', index='end',values=(v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7]), tags=('linha_impar',))
            count += 1


    def orquestradora(self):
        self.sql.criando_conexao_sql()

        Deletar.base_pergunta(self)

        Deletar.botao_voltar(self)

        Deletar.botao_deletar(self)

        Deletar.insere_tabela(self)