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

class Atualizar(PlanoDeFundo):
    def __init__(self, imagem_fundo, root):
        super().__init__(imagem_fundo, root)

        self.sql = sqlComandos('DESKTOP-C10NOM4\SQLEXPRESS', 'PROJETO_MAUA')

    def inserindo_input_pergunta(self):

        '''
           COLOCANDO INPUT PERGUNTA 
        '''

        self.pergunta = Entry(self.root,
                             bg='white',
                             font=('Verdana', 10),
                             fg='black',
                             borderwidth=0,
                             )

        self.pergunta.pack()
        self.pergunta.place(width=510, height=25, x=360, y=187)


    def inserindo_input_a(self):

        '''
            COLOCANDO INPUT ALTERNATIVA A
        '''

        self.alternativa_a = Entry(self.root,
                             bg='white',
                             font=('Verdana', 10),
                             fg='black',
                             borderwidth=0,
                             )

        self.alternativa_a.pack()
        self.alternativa_a.place(width=510, height=25, x=410, y=246)

    
    def inserindo_input_b(self):

        '''
            COLOCANDO INPUT ALTERNATIVA B
        '''

        self.alternativa_b = Entry(self.root,
                             bg='white',
                             font=('Verdana', 10),
                             fg='black',
                             borderwidth=0,
                             )

        self.alternativa_b.pack()
        self.alternativa_b.place(width=510, height=25, x=410, y=294)

    
    def inserindo_input_c(self):

        '''
            COLOCANDO INPUT ALTERNATIVA C
        '''

        self.alternativa_c = Entry(self.root,
                             bg='white',
                             font=('Verdana', 10),
                             fg='black',
                             borderwidth=0,
                             )

        self.alternativa_c.pack()
        self.alternativa_c.place(width=510, height=25, x=410, y=340)


    def inserindo_input_d(self):

        '''
            COLOCANDO INPUT ALTERNATIVA D
        '''

        self.alternativa_d = Entry(self.root,
                             bg='white',
                             font=('Verdana', 10),
                             fg='black',
                             borderwidth=0,
                             )

        self.alternativa_d.pack()
        self.alternativa_d.place(width=510, height=25, x=410, y=387)


    def combobox_nivel(self):

        '''
            COLOCANDO COMBOBOX NIVEL
        '''

        lista_niveis = [1, 2, 3]
        self.nivel = ttk.Combobox(self.root,
                                  values=lista_niveis)
        self.nivel.pack()
        self.nivel.place(width=50, height=25, x=450, y=450)


    def combobox_resp(self):

        '''
            COLOCANDO COMBOBOX RESPOSTA
        '''

        lista_resp = ["A","B","C","D"]
        self.resp = ttk.Combobox(self.root,
                                  values=lista_resp)
        self.resp.pack()
        self.resp.place(width=50, height=25, x=850, y=450)


    def combobox_id(self):

        '''
            COLOCANDO COMBOBOX ID_PERGUNTA
        '''

        self.df.reset_index(inplace=True)
        self.df.rename(columns = {'ID_PERGUNTA':'ID_TEMPORARIO',
                                  'index':'ID_PERGUNTA'}, inplace=True)
        
        self.df['ID_PERGUNTA'] = self.df['ID_PERGUNTA'].apply(lambda x: int(x) + 1)
        
        lista_ids = list(self.df['ID_PERGUNTA'])
        self.id = ttk.Combobox(self.root,
                               values=lista_ids)
        self.id.pack()
        self.id.place(width=50, height=25, x=500, y=135)

    
    def botao_pesquisar(self):

        '''
            COLOCANDO BOTAO PESQUISAR
        '''

        self.btn_pesquisar = Button(text='Pesquisar',
                                    borderwidth=0,
                                    background='#4285f4',
                                    font = 'Arial 12 bold',
                                    fg = 'white',
                                    command=self.pesquisar_pergunta
                                    )
        self.btn_pesquisar.pack()
        self.btn_pesquisar.place(width=100, height=25, x=565, y=135)


    def pesquisar_pergunta(self):

        '''
            TRÁS A PERGUNTA E AS ALTERNATIVAS DO BANCO DE DADOS 
            PARA OS CAMPOS VAZIOS PARA SEREM ATUALIZADOS
        '''
        self.df['ID_PERGUNTA'] = self.df['ID_PERGUNTA'].apply(lambda x: str(x))
        self.id_real = self.df[self.df['ID_PERGUNTA'] == self.id.get()]['ID_TEMPORARIO'].values[0]
        self.df.drop(['ID_TEMPORARIO'], axis=1, inplace=True)
        if self.id.get() in list(self.df['ID_PERGUNTA']):
            dados = self.df[self.df['ID_PERGUNTA'] == self.id.get()]
            dados = list(dados.values[0])
            self.pergunta.delete(0,END)
            self.pergunta.insert(0,dados[1])
            self.alternativa_a.delete(0, END)
            self.alternativa_a.insert(0, dados[2])
            self.alternativa_b.delete(0, END)
            self.alternativa_b.insert(0, dados[3])
            self.alternativa_c.delete(0, END)
            self.alternativa_c.insert(0, dados[4])
            self.alternativa_d.delete(0, END)
            self.alternativa_d.insert(0, dados[5])
            self.nivel.delete(0, END)
            self.nivel.insert(0, dados[7])
            self.resp.delete(0, END)
            self.resp.insert(0, dados[6])

        else:
            mb = Messagebox.MessageboxErro('images/messagebox.png','ERRO','ID Pergunta inválido')
            mb.orquestradora()
        

    def botao_atualizar(self):

        '''
            COLOCANDO BOTÃO ATUALIZAR
        '''

        self.btn_atualizar = Button(self.root,
                                  text='ATUALIZAR',
                                  width=200,
                                  height=30,
                                  font=('Verdana',12, 'bold'),
                                  bg = '#08B4B8',
                                  fg = '#fff',
                                  borderwidth=0,
                                  command=self.atualizar_pergunta
                                  )
        self.btn_atualizar.pack()
        self.btn_atualizar.place(width=110, height=45, x=526, y=485)

    def armazena_dados(self):

        '''
            ARMAZENA OS DADOS EM UMA LISTA DE DADOS
        '''

        self.lista_dados = []
        try:
            pergunta = self.pergunta.get().replace('\'','\"')
        except:
            pass
        try:
            altA = self.alternativa_a.get().replace('\'','\"')
        except:
            pass
        try:
            altB = self.alternativa_b.get().replace('\'','\"')
        except:
            pass
        try:
            altC = self.alternativa_c.get().replace('\'','\"')
        except:
            pass
        try:
            altD = self.alternativa_d.get().replace('\'','\"')
        except:
            pass
        try:
            resp = self.resp.get().upper().replace('\'','\"')
        except:
            pass
        try:
            nivel = self.nivel.get().replace('\'','\"')
        except:
            pass
        self.lista_dados.append((pergunta, altA, altB, altC, altD, resp, nivel, str(self.id_real)))


    def atualizar_pergunta(self):

        '''
            VALIDAÇÃO DO BOTÃO ATUALIZAR
        '''

        
        try:
            if self.pergunta.get() == '' or self.pergunta.get() == 'Pergunta:' or self.alternativa_a.get() == '' or self.alternativa_a.get() == 'Alternativa A:' or self.alternativa_b.get() == '' or self.alternativa_b.get() == 'Alternativa B:' or self.alternativa_c.get() == '' or self.alternativa_c.get() == 'Alternativa C:'or self.alternativa_d.get() == '' or self.alternativa_d.get() == 'Alternativa D:':
                mb = Messagebox.MessageboxErro('images/messagebox.png','ERRO','Todos os campos são necessários')
                mb.orquestradora()
            else:
                if len(self.pergunta.get()) <= 100:
                    tamanho_ok = True
                    if len(self.alternativa_a.get()) <= 100:
                        if len(self.alternativa_b.get()) <= 100:
                            if len(self.alternativa_c.get()) <= 100:
                                if len(self.alternativa_d.get()) <= 100:
                                    if self.nivel.get().strip() == '1' or self.nivel.get().strip() == '2' or self.nivel.get().strip() == '3':
                                        nivel_valido = True
                                        if self.resp.get().upper().strip() == 'A' or self.resp.get().upper().strip() == 'B' or self.resp.get().upper().strip() == 'C' or self.resp.get().upper().strip() == 'D':
                                            query_update = f"""UPDATE TBL_PERGUNTA 
                                                SET PERGUNTA = ?,
                                                altA = ?,
                                                altB = ?,
                                                altC = ?,
                                                altD = ?,
                                                RESP = ?,
                                                NIVEL = ?
                                                WHERE ID_PERGUNTA = ?;
                                                """
                                            self.armazena_dados()
                                            print(self.lista_dados[0])
                                            self.sql.cursor.execute(query_update, self.lista_dados[0])
                                            self.sql.conexao.commit()
                                            mi = Messagebox.MessageboxInfo('images/messageboxinfo.png','ATUALIZADO','Pergunta atualizada com sucesso')
                                            mi.orquestradora()
                                            print('\033[1;34mDados Atualizados com sucesso\033[m')
                                            self.voltar_menu()
                                        else:
                                            mb = Messagebox.MessageboxErro('images/messagebox.png','ERRO','Selecione a resposta correta')
                                            mb.orquestradora()
                                    else:
                                        mb = Messagebox.MessageboxErro('images/messagebox.png','ERRO','Selecione o nível da pergunta')
                                        mb.orquestradora()
                                else:
                                    mb = Messagebox.MessageboxErro('images/messagebox.png','ERRO','Tamanho máximo permitido no campo\n Alternativa D: 100 caracteres')
                                    mb.orquestradora()
                            else:
                                mb = Messagebox.MessageboxErro('images/messagebox.png','ERRO','Tamanho máximo permitido no campo\n Alternativa C: 100 caracteres')
                                mb.orquestradora()
                        else:
                            mb = Messagebox.MessageboxErro('images/messagebox.png','ERRO','Tamanho máximo permitido no campo\n Alternativa :B 100 caracteres')
                            mb.orquestradora()
                    else:
                        mb = Messagebox.MessageboxErro('images/messagebox.png','ERRO','Tamanho máximo permitido no campo\n Alternativa A: 100 caracteres')
                        mb.orquestradora()
                else:
                    mb = Messagebox.MessageboxErro('images/messagebox.png','ERRO','Tamanho máximo permitido no campo\n Pergunta: 100 caracteres')
                    mb.orquestradora()


        except Exception as ex:
            print(ex) 


    def base_pergunta(self):

        '''
            LENDO TBL_PERGUNTA DO BANCO DE DADOS
        '''


        self.df = pd.read_sql_query('SELECT * FROM TBL_PERGUNTA', self.sql.conexao)


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

    def voltar_menu(self):

        '''
            VOLTA PARA A TELA PRINCIPAL DE ADM
        '''

        self.label_fundo.destroy()
        self.alternativa_a.destroy()
        self.alternativa_b.destroy()
        self.alternativa_c.destroy()
        self.alternativa_d.destroy()
        try:
            self.btn_criar.destroy()
        except:
            pass
        self.pergunta.destroy()
        self.nivel.destroy()
        self.resp.destroy()
        self.voltar.destroy()

        ta = Voltar_Tela_Adm.TelaAdm('images/Tela_adm.png', self.root)

        ta.orquestradora()
        

    def orquestradora(self):

        # CRIANDO CONEXAO COM SQL
        self.sql.criando_conexao_sql()

        # LENDO BASE PERGUNTA
        Atualizar.base_pergunta(self)

        # INSERINDO INPUT PERGUNTA
        Atualizar.inserindo_input_pergunta(self)

        # INSERINDO INPUT ALTERNATIVA A
        Atualizar.inserindo_input_a(self)

        # INSERINDO INPUT ALTERNATIVA B
        Atualizar.inserindo_input_b(self)

        # INSERINDO INPUT ALTERNATIVA C
        Atualizar.inserindo_input_c(self)

        # INSERINDO INPUT ALTERNATIVA D
        Atualizar.inserindo_input_d(self)

        # BOTÃO VOLTAR
        Atualizar.botao_voltar(self)
        
        # COLOCANDO COMBOBOX NIVEL
        Atualizar.combobox_nivel(self)

        # COLOCANDO COMBOBOX RESPOSTA
        Atualizar.combobox_resp(self)

        # COLOCANDO COMBOBOX ID_PERGUNTA
        Atualizar.combobox_id(self)

        # COLOCANDO BOTÃO PESQUISAR
        Atualizar.botao_pesquisar(self)

        # COLOCANDO BOTÃO ATUALIZAR
        Atualizar.botao_atualizar(self)