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
import Messagebox
from time import sleep


warnings.filterwarnings('ignore')

# ==================================
# TELA DE CADASTRO PROJETO GAME MAUA
# ==================================


class TelaCadastro:

    def __init__(self, imagem_fundo):
        # Iniciando interface
        self.menu_cadastro = Tk()

        # Definindo a dimensão da interface
        self.menu_cadastro.geometry('989x570')

        # Definindo título para a interface
        self.menu_cadastro.title('CADASTRO')

        # Restringindo para não mecher nas dimensões da tela
        self.menu_cadastro.resizable(False, False)

        # Colocando fundo
        self.fundo = ImageTk.PhotoImage(Image.open(imagem_fundo))

        # Criando label para colocar o fundo
        self.label_fundo = Label(self.menu_cadastro, image=self.fundo)
        self.label_fundo.pack()

        self.sql = sqlComandos('DESKTOP-C10NOM4\SQLEXPRESS', 'PROJETO_MAUA')

    def centralizar_interface_menu_cadastro(self):

        '''
            Centraliza a tela de cadastro no meio do monitor
        '''

        largura = 989
        altura = 570
        largura_screen = self.menu_cadastro.winfo_screenwidth()
        altura_screen = self.menu_cadastro.winfo_screenheight()
        posx = largura_screen/2 - largura/2
        posy = altura_screen/2 - altura/2
        self.menu_cadastro.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))


    def colocando_input_usuario(self):

        '''
            Insere um input pedindo ao usuário que digite
            um Username para seu cadastro
        '''

        self.usuario = Entry(self.menu_cadastro,
                             bg='#ffffff',
                             font=('Verdana', 10),
                             fg='black',
                             borderwidth=0,
                             )
        add_placeholder_to(self.usuario, 'Enter username: ')
        self.usuario.pack()
        self.usuario.place(width=210, height=25, x=663, y=219)
        

    def colocando_input_senha(self):

        '''
            Insere um input pedindo ao usuário que digite
            um Username para seu cadastro
        '''
        vsenha = StringVar()
        
        self.senha = Entry(self.menu_cadastro,
                             bg='#ffffff',
                             font=('Verdana', 10),
                             textvariable=vsenha,
                             show='*',
                             fg='black',
                             borderwidth=0
                             )
        add_placeholder_to(self.senha, 'Senha: ')  
        self.senha.pack()
        self.senha.place(width=210, height=25, x=663, y=293)


    def colocando_input_email(self):

        '''
            Insere um input pedindo ao usuário que digite
            um Username para seu cadastro
        '''

        self.email = Entry(self.menu_cadastro,
                             bg='#ffffff',
                             font=('Verdana', 10),
                             fg='black',
                             borderwidth=0
                             )
        add_placeholder_to(self.email, 'Enter email: ')  
        self.email.pack()
        self.email.place(width=210, height=25, x=663, y=367)


    def inserindo_botao_cadastrar(self):

        '''
            Insere o botão cadastrar que ao clicar irá
            executar a função inserir_codigo.

            OBS: O esquema para deixá-lo com borda colorida, é criar um quadro da cor desejada
            e nele inserir o botão.
            
        '''
        borda_btn = Frame(self.menu_cadastro,
                          highlightthickness=1,
                          highlightbackground="#ffffff",)

        self.btn_signup = Button(borda_btn,
                                 text='Cadastrar',
                                 font='Verdana 13 bold',
                                 fg='white',
                                 bg='#298A97',
                                 borderwidth=False,
                                 height=45,
                                 command=self.inserir_codigo)
        self.btn_signup.pack()
        borda_btn.pack()
        borda_btn.place(width=105, height=45, x=633, y=437)
        
        
    def inserindo_botao_logar(self):

        '''
            Insere o botão Login que ao clicar irá
            para a tela de Login.

            OBS: O esquema para deixá-lo com borda colorida, é criar um quadro da cor desejada
            e nele inserir o botão.
            
        '''
        label_login = Label(self.menu_cadastro,
                            text='Já possui cadastro?',
                            font='Verdana 9 bold',
                            bg='white'
                                )
        label_login.pack()
        label_login.place(x=755, y=412)


        borda_btn = Frame(self.menu_cadastro,
                          highlightthickness=1,
                          highlightbackground="#ffffff",)

        self.btn_logar = Button(borda_btn,
                                 text='Logar',
                                 font='Verdana 13 bold',
                                 fg='white',
                                 bg='#08B4B8',
                                 borderwidth=False,
                                 height=45,
                                 width=105,
                                 activebackground='#08B4B8',
                                 command=self.abrir_login)
        self.btn_logar.pack()
        borda_btn.pack()
        borda_btn.place(width=105, height=45, x=765, y=437)


    def abrir_login(self):
        self.menu_cadastro.destroy()
        self.login = Tela_Login.Login('images/TelaLogin.png')
        self.login.orquestradora()


    def check_function(self):

        '''
            Função que valida os dados de entrada do usuário
        '''
        email_valido = False
        lista_emails_aceitaveis = ['gmail.com','gmail.com.br','hotmail.com','hotmail.com.br', 'outlook.com', 'outlook.com.br','yahoo.com.br'
        'yahoo.com','uol.com.br','maua.br']

        if self.usuario.get() == "" or self.senha.get() == "" or self.email.get() == "" or self.usuario.get() == 'Enter username: ' or self.senha.get() == "Senha: " or self.email.get() == 'Enter email: ' or self.senha.get() == '*******':
            mi = Messagebox.MessageboxErro('images/messagebox.png','ERRO', 'Todos os campos são necessários')
            mi.orquestradora()
        else:
            if len(self.usuario.get()) > 20:
                mi = Messagebox.MessageboxErro('images/messagebox.png','ERRO', 'Tamanho máximo de usuário:\n20 caracters')
                mi.orquestradora()
            else:
                if len(self.senha.get()) > 16:
                    mi = Messagebox.MessageboxErro('images/messagebox.png','ERRO', 'Tamanho máximo de senha:\n16 caracters')
                    mi.orquestradora()
                else:
                    if '\'' in self.usuario.get() or '\'' in self.senha.get() or '\'' in self.email.get():
                        mi = Messagebox.MessageboxErro('images/messagebox.png','ERRO', 'Caracter \' não é aceitável')
                        mi.orquestradora()
                    else:
                        if self.usuario.get().capitalize() in list(self.df['USUARIO']):
                            mi = Messagebox.MessageboxErro('images/messagebox.png','ERRO', f'Usuário {self.usuario.get()} já é cadastrado')
                            mi.orquestradora()
                        else:
                            try:
                                tipo_email = self.email.get().split('@')[1].lower()
                                email_valido = True
                                if email_valido == True:
                                    if tipo_email not in lista_emails_aceitaveis:
                                        mi = Messagebox.MessageboxErro('images/messagebox.png','ERRO', f'Formato de email inválido')
                                        mi.orquestradora()
                                    else:
                                        if self.email.get() in list(self.df['EMAIL']):
                                            mi = Messagebox.MessageboxErro('images/messagebox.png','ERRO', f'Este e-mail já possui cadastro')
                                            mi.orquestradora()
                                        else:
                                            messagebox.showinfo('SUCESSO',f'Usuário {self.usuario.get()} cadastrado com sucesso')
                                            self.inserindo_sql()
                                            self.abrir_login()

                            except Exception as ex:
                                print(ex)
                                try:
                                    if tipo_email in lista_emails_aceitaveis:
                                        pass
                                    else:
                                        mi = Messagebox.MessageboxErro('images/messagebox.png','ERRO', f'Formato de email inválido')
                                        mi.orquestradora()
                                except:
                                    mi = Messagebox.MessageboxErro('images/messagebox.png','ERRO', f'Formato de email inválido')
                                    mi.orquestradora()
                    

    def inserir_codigo(self):

        '''
            Função que cria uma tupla dos dados digitados pelo usuario
            e executa a função check_function, responsável por validar
            os dados de entrada do usuário
        '''

        # Criando lista vazia para receber os dados
        self.lista_codigos = []
        
        # Armazenando os dados do usuário
        campo_usuario = self.usuario.get().capitalize()
        campo_senha = self.senha.get()
        campo_email = self.email.get()
        
        # Pegando data atual
        data_criacao = datetime.datetime.now()
        
        # Transformando data em formato string
        data_criacao = data_criacao.strftime('%d/%m/%Y %H:%M')
        
        # Adicionando dados na tupla
        self.lista_codigos.append((len(self.df) + 1,campo_usuario, campo_senha, campo_email, f'{data_criacao}'))
        self.check_function()


    def executar(self):

        # Executando menu cadastro
        self.menu_cadastro.mainloop()


    def base_sql(self):
        try:
            self.df = pd.read_sql("SELECT * FROM PROJETO_MAUA.dbo.TBL_CADASTRO;", self.sql.conexao)
        except:
            try:
                self.df = pd.read_sql("SELECT * FROM PROJETO_MAUA.TBL_CADASTRO;", self.sql.conexao)
            except:
                try:
                    self.df = pd.read_sql("SELECT * FROM PROJETO_MAUA.dbo.TBL_CADASTRO;", self.sql.conexao)
                except:
                    print('Erro ao ler base TBL_CADASTRO do SQL')


    
    def inserindo_sql(self):


         '''
             Insere os valores digitados pelo usuário na
             tabela do banco de dados chamada TBL_CADASTRO
         '''

         comando = f"""INSERT INTO TBL_CADASTRO(ID_USUARIO, USUARIO, SENHA, EMAIL, DATA_CRIADA) VALUES {self.lista_codigos[0]}"""
         self.sql.cursor.execute(comando)
         self.sql.cursor.commit()


    def orquestradora(self):

        # Centralizando mennu cadastro
        TelaCadastro.centralizar_interface_menu_cadastro(self)

        # Colocando input Usuário
        TelaCadastro.colocando_input_usuario(self)

        # Colocando input senha
        TelaCadastro.colocando_input_senha(self)
        
        # Colocando input email
        TelaCadastro.colocando_input_email(self)

        # Inserindo botão Cadastrar
        TelaCadastro.inserindo_botao_cadastrar(self)

        # Inserindo botão Logar
        TelaCadastro.inserindo_botao_logar(self)
        
        # Conecta-se ao SQL server
        self.sql.criando_conexao_sql()

        # Lendo base do sql
        TelaCadastro.base_sql(self)

        # Executando menu cadastro
        TelaCadastro.executar(self)





