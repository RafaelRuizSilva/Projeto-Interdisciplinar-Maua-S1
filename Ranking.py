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

class Ranking(PlanoDeFundo):

    # INICIALIZANDO A PARTIR DA HERANÇA PlanoDeFundo
    def __init__(self, imagem_fundo, root):
        super().__init__(imagem_fundo, root)


        # CRIANDO CONEXÃO COM BANCO DE DADOS 
        self.sql = sqlComandos('DESKTOP-C10NOM4\SQLEXPRESS', 'PROJETO_MAUA')


    def base_jogador(self):
        self.df_jogador = pd.read_sql_query('SELECT * FROM TBL_JOGADOR', self.sql.conexao)

    def inserindo_tabela(self):
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
        frame_tabela.place(width=580, height=290, x=340, y=240)

        # LISTA DE COLUNAS
        colunas = ['column2','column3','column4','column5']

        # CRIANDO TREEVIEW
        self.tabela = ttk.Treeview(frame_tabela, columns=colunas, show='headings', height=300,)
        
        # DEFININDO LARGURA DAS COLUNAS
        self.tabela.column("column2", width=120, minwidth=50)
        self.tabela.column("column3", width=120, minwidth=50)
        self.tabela.column("column4", width=120, minwidth=50)
        self.tabela.column("column5", width=100, minwidth=50)
        

        # ALTERANDO NOME DAS COLUNAS
        self.tabela.heading('column2', text='RA_JOGADOR')
        self.tabela.heading('column3', text='PONTUACAO')
        self.tabela.heading('column4', text='TEMPO')
        self.tabela.heading('column5', text='NIVEL')

        self.tabela.pack()
    

        self.tabela.tag_configure('linha_par', background='#cccccc')
        self.tabela.tag_configure('linha_impar', background='#92f5ec')
        # Alimentando a tabela com os dados da base do BD
        
        self.df_jogador.sort_values(by=['PONTUACAO','TEMPO'], ascending=False, inplace=True)
        self.df_jogador.drop(['ID_JOGADOR'], axis=1, inplace=True)
        

        lista_dados = list(zip(list(self.df_jogador['RA_JOGADOR']), list(self.df_jogador['PONTUACAO']), list(self.df_jogador['TEMPO']), list(self.df_jogador['NIVEL'])))
        count = 0
        for v in lista_dados:
            if count % 2 == 0:
                self.tabela.insert(parent='', index='end',values=(v[0], v[1], v[2], v[3]), tags=('linha_par',))
            else:
                self.tabela.insert(parent='', index='end',values=(v[0], v[1], v[2], v[3]), tags=('linha_impar',))
            count += 1


    def combobox_nivel(self):

        '''
            COLOCANDO COMBOBOX NÍVEL
        '''

        lista_niveis = [1, 2, 3]
        self.nivel = ttk.Combobox(self.root,
                                  values=lista_niveis)
        self.nivel.pack()
        self.nivel.place(width=50, height=25, x=840, y=96)

    def inserindo_input_ra(self):
        self.input_ra = Entry(borderwidth=0,
                              bg = 'white',
                              font = 'verdana 10')
        self.input_ra.pack()
        self.input_ra.place(width= 100,x = 500, y=96)
        add_placeholder_to(self.input_ra, 'RA:')

    def botao_voltar(self):
        '''
            COLOCANDO BOTÃO VOLTAR    
        '''

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

    def botao_filtrar(self):
        self.borda_btn_filtrar = Frame(self.root,
                                    highlightthickness=1,
                                    highlightbackground="white",)

        self.btn_filtrar = Button(self.borda_btn_filtrar,
                                 text='Filtrar',
                                 font='Verdana 11 bold',
                                 fg='white',
                                 bg='#4285f4',
                                 borderwidth=False,
                                 height=45,
                                 width=105,
                                 activebackground='#4285f4',
                                 command=self.filtro_aplicado
                                 )
        self.btn_filtrar.pack()
        self.borda_btn_filtrar.pack()
        self.borda_btn_filtrar.place(width=110, height=35, x=385, y=145)


    def filtro_aplicado(self):
        nivel_ok = False
        nivel = self.nivel.get()
        nivel = nivel + ' '
        df_filtrado_nivel = self.df_jogador[self.df_jogador['NIVEL'] == nivel]
        lista_dados = list(zip(list(df_filtrado_nivel['RA_JOGADOR']), list(df_filtrado_nivel['PONTUACAO']), list(df_filtrado_nivel['TEMPO']), list(df_filtrado_nivel['NIVEL'])))
        if self.input_ra.get() == 'RA:' or self.input_ra.get() == '':
            if self.nivel.get() == '1' or self.nivel.get() == '2' or self.nivel.get() == '3':
                nivel_ok = True
                for item in self.tabela.get_children():
                    self.tabela.delete(item)
                count = 0
                for v in lista_dados:
                    if count % 2 == 0:
                        self.tabela.insert(parent='', index='end',values=(v[0], v[1], v[2], v[3]), tags=('linha_par',))
                    else:
                        self.tabela.insert(parent='', index='end',values=(v[0], v[1], v[2], v[3]), tags=('linha_impar',))
                    count += 1
            
            else:
                if self.nivel.get() == '':
                    lista_dados = list(zip(list(self.df_jogador['RA_JOGADOR']), list(self.df_jogador['PONTUACAO']), list(self.df_jogador['TEMPO']), list(self.df_jogador['NIVEL'])))
                    count = 0
                    for item in self.tabela.get_children():
                        self.tabela.delete(item)
                    for v in lista_dados:
                        if count % 2 == 0:
                            self.tabela.insert(parent='', index='end',values=(v[0], v[1], v[2], v[3]), tags=('linha_par',))
                        else:
                            self.tabela.insert(parent='', index='end',values=(v[0], v[1], v[2], v[3]), tags=('linha_impar',))
                        count += 1
                else:
                    mi = Messagebox.MessageboxErro('images/messagebox.png', 'ERRO', 'Nível inválido')
                    mi.orquestradora()

            
        else:
            if len(self.input_ra.get()) == 10:
                if self.nivel.get() == '1' or self.nivel.get() == '2' or self.nivel.get() == '3':
                    df_filtrado_ra_nivel = self.df_jogador[self.df_jogador['RA_JOGADOR'] == self.input_ra.get()]
                    df_filtrado_ra_nivel = df_filtrado_ra_nivel[df_filtrado_ra_nivel['NIVEL'] == nivel]
                    lista_dados = list(zip(list(df_filtrado_ra_nivel['RA_JOGADOR']), list(df_filtrado_ra_nivel['PONTUACAO']), list(df_filtrado_ra_nivel['TEMPO']), list(df_filtrado_ra_nivel['NIVEL'])))
                    count = 0
                    for item in self.tabela.get_children():
                        self.tabela.delete(item)
                    for v in lista_dados:
                        if count % 2 == 0:
                            self.tabela.insert(parent='', index='end',values=(v[0], v[1], v[2], v[3]), tags=('linha_par',))
                        else:
                            self.tabela.insert(parent='', index='end',values=(v[0], v[1], v[2], v[3]), tags=('linha_impar',))
                        count += 1
                else:
                    if self.nivel.get() == '':
                        df_filtrado_ra = self.df_jogador[self.df_jogador['RA_JOGADOR'] == self.input_ra.get()]
                        lista_dados = list(zip(list(df_filtrado_ra['RA_JOGADOR']), list(df_filtrado_ra['PONTUACAO']), list(df_filtrado_ra['TEMPO']), list(df_filtrado_ra['NIVEL'])))
                        for item in self.tabela.get_children():
                            self.tabela.delete(item)
                        count = 0
                        for v in lista_dados:
                            if count % 2 == 0:
                                self.tabela.insert(parent='', index='end',values=(v[0], v[1], v[2], v[3]), tags=('linha_par',))
                            else:
                                self.tabela.insert(parent='', index='end',values=(v[0], v[1], v[2], v[3]), tags=('linha_impar',))
                            count += 1
                    else:
                        mi = Messagebox.MessageboxErro('images/messagebox.png', 'ERRO', 'Nível inválido')
                        mi.orquestradora()
            else:
                mi = Messagebox.MessageboxErro('images/messagebox.png', 'ERRO', 'RA inválido')
                mi.orquestradora()
            
           
            



    def voltar_menu(self):

        '''
            FUNÇÃO DE VOLTAR PARA O MENU PRINCIPAL DE ADM
        '''

        self.label_fundo.destroy()
        self.voltar.destroy()

        ta = Voltar_Tela_Adm.TelaAdm('images/Tela_adm.png', self.root)

        ta.orquestradora()

    def inserindo_botao_deletar(self):
        self.borda_btn_deletar = Frame(self.root,
                                    highlightthickness=1,
                                    highlightbackground="white",)

        self.btn_deletar = Button(self.borda_btn_deletar,
                                 text='Deletar',
                                 font='Verdana 12 bold',
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
        self.borda_btn_deletar.place(width=110, height=35, x=500, y=145)

    def deletar_pergunta(self):
        try:
            item_selecionado = self.tabela.focus()
            valores = self.tabela.item(item_selecionado, 'values')
            print(valores)
            query_deletar = '''DELETE TBL_JOGADOR WHERE RA_JOGADOR = ?'''
            deseja_deletar = messagebox.askyesno('DELETAR',f'Deseja deletar o registro RA: {valores[0]}?')
            if deseja_deletar:
                self.sql.cursor.execute(query_deletar, valores[0])
                self.sql.conexao.commit()
                self.tabela.delete(item_selecionado)
                self.voltar_menu()
            else:
                pass
        except:
            messagebox.showwarning('PERIGO', 'Você está prestes a deletar todos os registros, caso queira deletar um específico, selecione na tabela')
            excluir = messagebox.askyesno('PERIGO','Você deseja deletar todos registros existentes na tabela?')
            if excluir:
                delete = 'DELETE TBL_JOGADOR'
                for item in self.tabela.get_children():
                    self.tabela.delete(item)
                self.sql.cursor.execute(delete)
                self.sql.conexao.commit()
                self.voltar_menu()

    def orquestradora(self):
        self.sql.criando_conexao_sql()

        Ranking.base_jogador(self)

        Ranking.botao_voltar(self)

        Ranking.inserindo_tabela(self)

        Ranking.combobox_nivel(self)

        Ranking.inserindo_input_ra(self)

        Ranking.botao_filtrar(self)

        Ranking.inserindo_botao_deletar(self)
        