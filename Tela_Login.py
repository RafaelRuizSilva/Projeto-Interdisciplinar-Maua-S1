from tkinter import *
import tkinter
from PIL import ImageTk, Image
import datetime
import pyodbc
from tkinter import messagebox
import pandas as pd
from placeholder import add_placeholder_to
import Tela_Cadastro_Principal
from Sql_Conexao import sqlComandos
import Tela_Principal
import Tela_Adm
import Messagebox


class Login:
    def __init__(self, imagem_fundo):
        # Iniciando interface
        self.menu_login = Tk()

        # Definindo a dimensão da interface
        self.menu_login.geometry('989x570')

        # Definindo título para a interface
        self.menu_login.title('TELA DE LOGIN')

        # Restringindo para não mecher nas dimensões da tela
        self.menu_login.resizable(False, False)

        # Colocando fundo
        self.fundo = ImageTk.PhotoImage(Image.open(imagem_fundo))

        # Criando label para colocar o fundo
        self.label_fundo = Label(self.menu_login, image=self.fundo)
        self.label_fundo.pack()

        self.sql = sqlComandos('DESKTOP-C10NOM4\SQLEXPRESS', 'PROJETO_MAUA')


    def centralizando_menu_login(self):

        '''
            Centraliza a tela de LOGIN no meio do monitor
        '''

        largura = 989
        altura = 570
        largura_screen = self.menu_login.winfo_screenwidth()
        altura_screen = self.menu_login.winfo_screenheight()
        posx = largura_screen / 2 - largura / 2
        posy = altura_screen / 2 - altura / 2
        self.menu_login.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))


    def executar_menu_login(self):

        '''
            Executa a tela de login
        '''

        self.menu_login.mainloop()


    def colocando_input_usuario_login(self):

        '''
            Insere um input pedindo ao usuário que digite
            um Username para seu cadastro
        '''

        self.usuario = Entry(self.menu_login,
                             bg='#ffffff',
                             font=('Verdana', 10),
                             fg='black',
                             borderwidth=0,
                             )
        add_placeholder_to(self.usuario, 'Enter username: ')
        self.usuario.pack()
        self.usuario.place(width=210, height=25, x=663, y=219)
        

    def colocando_input_senha_login(self):

        '''
            Insere um input pedindo ao usuário que digite
            um Username para seu cadastro
        '''

        vsenha = StringVar()
        
        self.senha = Entry(self.menu_login,
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


    def toggle(self):

        '''
            
        '''

        if self.checkbutton.var.get():
            self.senha.config(show = "*")
        else:
            self.senha.config(show = "")


    def inserindo_checkbutton_senha(self):

        self.checkbutton = Checkbutton(self.menu_login, 
                                text='Mostrar senha',
                                borderwidth=0,
                                bg='white',
                                onvalue=False,
                                offvalue=True,
                                command=self.toggle
                                )
        self.checkbutton.var = tkinter.BooleanVar(value=True)
        self.checkbutton['variable'] = self.checkbutton.var
        self.checkbutton.pack()
        self.checkbutton.place(x=658, y=323)

    
    def inserindo_botao_login(self):

        borda_btn = Frame(self.menu_login,
                          highlightthickness=1,
                          highlightbackground="white",)

        self.btn_logar = Button(borda_btn,
                                 text='Logar',
                                 font='Verdana 13 bold',
                                 fg='white',
                                 bg='#08B4B8',
                                 borderwidth=False,
                                 height=45,
                                 width=105,
                                 command=self.validando_login
                                 )
        self.btn_logar.pack()
        borda_btn.pack()
        borda_btn.place(width=105, height=45, x=700, y=370)


    def inserindo_botao_criar_conta(self):

        borda_btn = Frame(self.menu_login,
                          highlightthickness=1,
                          highlightbackground="white",)

        self.btn_criar_conta = Button(borda_btn,
                                 text='Criar conta',
                                 font='Verdana 10 bold',
                                 fg='black',
                                 bg='white',
                                 borderwidth=False,
                                 height=45,
                                 width=105,
                                 command=self.abrir_cadastro
                                 )
        self.btn_criar_conta.pack()
        self.btn_criar_conta.bind('<Enter>', self.button_hover)
        self.btn_criar_conta.bind('<Leave>', self.button_leave)
        borda_btn.pack()
        borda_btn.place(width=105, height=25, x=620, y=480)


    def button_hover(self, e):
        self.btn_criar_conta['fg'] = '#016c6c'


    def button_leave(self, e):
        self.btn_criar_conta['fg'] = 'black'


    def abrir_cadastro(self):
        self.menu_login.destroy()
        self.cadastro = Tela_Cadastro_Principal.TelaCadastro('images/TelaCadastroNova.png')
        self.cadastro.orquestradora()


    def base_sql(self):
        try:
            self.df = pd.read_sql("SELECT * FROM TBL_CADASTRO;", self.sql.conexao)
        except:
            try:
                self.df = pd.read_sql("SELECT * FROM PROJETO_MAUA.TBL_CADASTRO;", self.sql.conexao)
            except:
                try:
                    self.df = pd.read_sql("SELECT * FROM PROJETO_MAUA.dbo.TBL_CADASTRO;", self.sql.conexao)
                except:
                    print('Erro ao ler base TBL_CADASTRO do SQL')
        

    def abrir_principal(self):
        self.menu_login.destroy()
        self.principal = Tela_Principal.TelaPrincipal('images/Tela_principal.png')
        self.principal.orquestrador()


    def abrir_admin(self):
        self.menu_login.destroy()
        self.adm = Tela_Adm.TelaAdm('images/Tela_adm.png')
        self.adm.orquestradora()
        

    def validando_login(self):

        self.df_filtro = self.df[(self.df['USUARIO'] == f'{self.usuario.get().capitalize()}') & (self.df['SENHA'] == f'{self.senha.get()}')]

        try:
            if self.usuario.get() == '' or self.senha.get() == '' or self.usuario.get() == 'Enter username: ' or self.senha.get() == '*******' or self.senha.get() == 'Senha: ':
                mb = Messagebox.MessageboxErro('images/messagebox.png','ERRO','Todos os campos são necessários')
                mb.orquestradora()
            else:

                if self.usuario.get().capitalize() == 'Admin' and self.senha.get() == 'pass1234':
                    self.abrir_admin()

                elif self.usuario.get().capitalize() in list(self.df_filtro['USUARIO']) and self.senha.get() in list(self.df_filtro['SENHA']):
                    self.abrir_principal()

                else:
                    mb = Messagebox.MessageboxErro('images/messagebox.png','Erro de Login','Username ou senha inválidos')
                    mb.orquestradora()

        except Exception as ex:
            print(ex)
            print('Erro ao validar login!')


    def get_usuario(self):
        return self.usuario.get()
        
    def executar(self):
        self.menu_login.mainloop()


    def orquestradora(self):

        Login.centralizando_menu_login(self)

        Login.colocando_input_usuario_login(self)

        Login.colocando_input_senha_login(self)

        Login.inserindo_botao_login(self)

        Login.inserindo_botao_criar_conta(self)

        Login.inserindo_checkbutton_senha(self)

        self.sql.criando_conexao_sql()

        Login.base_sql(self)

        Login.executar(self)
        


if __name__ == "__main__":

    login = Login('images/TelaLogin.png')

    login.orquestradora()
