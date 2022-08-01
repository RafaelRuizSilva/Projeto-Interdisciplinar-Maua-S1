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

class Criar(PlanoDeFundo):

    # INICIALIZANDO A PARTIR DA HERANÇA PlanoDeFundo
    def __init__(self, imagem_fundo, root):
        super().__init__(imagem_fundo, root)


        # CRIANDO CONEXÃO COM BANCO DE DADOS 
        self.sql = sqlComandos()

    def inserindo_input_pergunta(self):
        
        '''
            COLOCANDO BOTÃO PERGUNTA
        '''

        self.pergunta = Entry(self.root,
                             bg='white',
                             font=('Verdana', 10),
                             fg='black',
                             borderwidth=0,
                             )
        add_placeholder_to(self.pergunta, 'Pergunta:', 'black')
        self.pergunta.pack()
        self.pergunta.place(width=510, height=25, x=380, y=137)


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
        add_placeholder_to(self.alternativa_a, 'Alternativa A:', 'black')
        self.alternativa_a.pack()
        self.alternativa_a.place(width=510, height=25, x=410, y=208)

    
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
        add_placeholder_to(self.alternativa_b, 'Alternativa B:', 'black')
        self.alternativa_b.pack()
        self.alternativa_b.place(width=510, height=25, x=410, y=254)

    
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
        add_placeholder_to(self.alternativa_c, 'Alternativa C:', 'black')
        self.alternativa_c.pack()
        self.alternativa_c.place(width=510, height=25, x=410, y=300)


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
        add_placeholder_to(self.alternativa_d, 'Alternativa D:', 'black')
        self.alternativa_d.pack()
        self.alternativa_d.place(width=510, height=25, x=410, y=350)


    def botao_criar(self):

        '''
            COLOCANDO BOTÃO CRIAR
        '''

        self.btn_criar = Button(self.root,
                                  text='CRIAR',
                                  width=200,
                                  height=30,
                                  font=('Verdana',14, 'bold'),
                                  bg = '#08B4B8',
                                  fg = '#fff',
                                  borderwidth=0,
                                  command=self.valida_criar_pergunta,
                                  activebackground='#08B4B8')
        self.btn_criar.pack()
        self.btn_criar.place(width=100, height=45, x=526, y=485)


    def combobox_nivel(self):

        '''
            COLOCANDO COMBOBOX NÍVEL
        '''

        lista_niveis = [1, 2, 3]
        self.nivel = ttk.Combobox(self.root,
                                  values=lista_niveis)
        self.nivel.pack()
        self.nivel.place(width=50, height=25, x=450, y=425)


    def combobox_resp(self):

        '''
            COLOCANDO COMBOBOX RESP
        '''

        lista_resp = ["A","B","C","D"]
        self.resp = ttk.Combobox(self.root,
                                  values=lista_resp)
        self.resp.pack()
        self.resp.place(width=50, height=25, x=850, y=425)


    def base_pergunta(self):

        '''
            LENDO TBL_ PERGUNTA DO BANCO DE DADOS
        '''

        self.df = pd.read_sql_query('SELECT * FROM TBL_PERGUNTA', self.sql.conexao)


    def inserindo_pergunta_sql(self):

        '''
            INSERINDO A PERGUNTA NO SQL
        '''
        
        try:
            comando = f"""
            INSERT INTO TBL_PERGUNTA(PERGUNTA, altA, altB, altC, altD, RESP, NIVEL) VALUES {self.lista_dados[0]}"""
            self.sql.cursor.execute(comando)
            print('\033[1;32mDados inseridos com sucesso\033[m')
            self.sql.cursor.commit()
            

        except Exception as ex:
            print(ex)
            print('ERRO')

    
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
        self.lista_dados.append((pergunta, altA, altB, altC, altD, resp, nivel))
            

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
            FUNÇÃO DE VOLTAR PARA O MENU PRINCIPAL DE ADM
        '''

        self.label_fundo.destroy()
        self.alternativa_a.destroy()
        self.alternativa_b.destroy()
        self.alternativa_c.destroy()
        self.alternativa_d.destroy()
        self.btn_criar.destroy()
        self.pergunta.destroy()
        self.nivel.destroy()
        self.resp.destroy()
        self.voltar.destroy()

        ta = Voltar_Tela_Adm.TelaAdm('images/Tela_adm.png', self.root)

        ta.orquestradora()



    def valida_criar_pergunta(self):

        '''
            FUNÇÃO QUE VALIDA A CRIAÇÃO DE PERGUNTA 
        '''

        nivel_valido = False
        tamanho_OK = False
        tamanho_OK_alt = False
        nivel = self.nivel.get()
        nivel = str(nivel) + ' '

        try:
            # VALIDA SE O QUIZ JÁ POSSUI 10 PERGUNTAS
            if len(self.df[self.df['NIVEL'] == nivel]) < 10:
                # VALIDA ESPAÇOS EM BRANCO
                if self.pergunta.get() == '' or self.pergunta.get() == 'Pergunta:' or self.alternativa_a.get() == '' or self.alternativa_a.get() == 'Alternativa A:' or self.alternativa_b.get() == '' or self.alternativa_b.get() == 'Alternativa B:' or self.alternativa_c.get() == '' or self.alternativa_c.get() == 'Alternativa C:'or self.alternativa_d.get() == '' or self.alternativa_d.get() == 'Alternativa D:':
                    mb = Messagebox.MessageboxErro('images/messagebox.png','ERRO','Todos os campos são necessários')
                    mb.orquestradora()
                else:
                    # VALIDA TAMANHO MÁXIMO DE PERGUNTA
                    if len(self.pergunta.get()) <= 100:
                        tamanho_ok = True

                        # VALIDA TAMANHO MÁXIMO DE ALTERNATIVA A
                        if len(self.alternativa_a.get()) <= 100:

                            # VALIDA TAMANHO MÁXIMO DE ALTERNATIVA B
                            if len(self.alternativa_b.get()) <= 100:

                                # VALIDA TAMANHO MÁXIMO DE ALTERNATIVA C
                                if len(self.alternativa_c.get()) <= 100:

                                    # VALIDA TAMANHO MÁXIMO DE ALTERNATIVA D
                                    if len(self.alternativa_d.get()) <= 100:

                                        # VALIDA OPÇÕES DE NIVEL
                                        if self.nivel.get() == '1' or self.nivel.get() == '2' or self.nivel.get() == '3':

                                            nivel_valido = True
                                            # VALIDA OPÇÕES DE RESPOSTA
                                            if self.resp.get().upper() == 'A' or self.resp.get().upper() == 'B' or self.resp.get().upper() == 'C' or self.resp.get().upper() == 'D':
                                                mi = Messagebox.MessageboxInfo('images/messageboxinfo.png','SUCESSO', 'Pergunta criada com êxito!')
                                                mi.orquestradora()

                                                self.armazena_dados()
                                                self.inserindo_pergunta_sql()
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
            else:
                mb = Messagebox.MessageboxErro('images/messagebox.png','ERRO','Já existem 10 perguntas desse nível')
                mb.orquestradora()
                              
        except Exception as ex:
            print(ex)
            pass


    def orquestradora(self):
        self.sql.criando_conexao_sql()

        Criar.base_pergunta(self)

        Criar.inserindo_input_pergunta(self)

        Criar.inserindo_input_a(self)

        Criar.inserindo_input_b(self)

        Criar.inserindo_input_c(self)

        Criar.inserindo_input_d(self)

        Criar.botao_criar(self)

        Criar.botao_voltar(self)
        
        Criar.combobox_nivel(self)

        Criar.combobox_resp(self)


