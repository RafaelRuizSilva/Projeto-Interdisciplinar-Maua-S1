from tkinter import *
from PIL import ImageTk, Image
import datetime
import pyodbc
from tkinter import messagebox
import pandas as pd
from placeholder import add_placeholder_to
from Planodefundo import PlanoDeFundo
from tkinter import ttk
import Voltar_Tela_Principal
from Sql_Conexao import sqlComandos


class Resultado(PlanoDeFundo):
    def __init__(self, imagem_fundo, root):
        super().__init__(imagem_fundo, root)

        self.sql = sqlComandos('DESKTOP-C10NOM4\SQLEXPRESS', 'PROJETO_MAUA')

    def botao_voltar(self):
        borda_btn = Frame(self.root,
                          highlightthickness=1,
                          highlightbackground="black",)

        self.voltar = Button(borda_btn,
                             text = 'Voltar Menu',
                             font = 'Ariel 16',
                             borderwidth = 0,
                             fg = 'black',
                             bg = '#50f0ff',
                             command = self.voltar_menu
                             )
        self.voltar.pack()
        borda_btn.pack()
        borda_btn.place(x=620, y=340)

        
    def voltar_menu(self):
        self.label_fundo.destroy()

        tp = Voltar_Tela_Principal.TelaPrincipal('images/Tela_principal.png', self.root)

        tp.orquestrador()


    def orquestradora(self):
        
        self.sql.criando_conexao_sql()

        Resultado.botao_voltar(self)
        