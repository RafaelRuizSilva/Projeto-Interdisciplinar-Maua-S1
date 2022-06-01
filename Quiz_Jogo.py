from cgitb import text
from email.mime import application
from msilib.schema import Font
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image
import datetime
import pyodbc
from tkinter import messagebox
import pandas as pd
from setuptools import Command
from placeholder import add_placeholder_to
from Sql_Conexao import sqlComandos
from Planodefundo import PlanoDeFundo
from tkinter import ttk
import Voltar_Tela_Principal
from time import sleep
import Resultado
import Tela_inicio_Quiz
import Messagebox



class QuizJogo(PlanoDeFundo):
    def __init__(self, imagem_fundo, root, nivel, ra):
        super().__init__(imagem_fundo, root)
        
        nivel = str(nivel) + ' '
        self.nivel = nivel
        self.sql = sqlComandos('DESKTOP-G2A0PO4\SQLEXPRESS', 'PROJETO_MAUA')
        self.ra = ra
        self.update_time = ''
        self.running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        sleep(1)
        self.criando_label()
        self.start()

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
        aviso = messagebox.askyesno('AVISO', 'Deseja sair? todo progresso será deletado!')
        if aviso:
            self.label_fundo.destroy()
            
            tp = Voltar_Tela_Principal.TelaPrincipal('images/Tela_principal.png', self.root)

            tp.orquestrador()

        else:
            pass


    def perguntas_nivel_especifico(self):

        '''
            DATAFRAME COM PERGUNTAS SOMENTE DE NIVEL ESPECIFICO
        '''
        
        self.df_nv = self.df[self.df['NIVEL'] == self.nivel]

    

    def label_pergunta(self, indice_pergunta):
      
        lista_perguntas = list(self.df_nv['PERGUNTA'])
        
        self.texto_pergunta = StringVar()

        self.texto_pergunta.set(f'{indice_pergunta + 1}. {lista_perguntas[indice_pergunta]}')

        self.pergunta = Label(textvariable = self.texto_pergunta,
                                bg = 'white',
                                fg = 'black',
                                borderwidth = 0,
                                font = 'verdana 11'
                                )
        self.pergunta.pack()
        self.pergunta.place(x = 50, y = 100)


    def lista_resposta_usuario(self):
        self.lista = []


    def resposta_usuario(self):
        
        if self.selecionado.get() == 'vazio':
            mi = Messagebox.MessageboxInfo('images/messagebox.png','AVISO', 'Selecione uma alternativa')
            mi.orquestradora()
        else:
            self.lista.append(self.selecionado.get())
            self.label.destroy()
            self.a.destroy()
            self.b.destroy()
            self.c.destroy()
            self.d.destroy()
            self.pergunta.destroy()
            self.label_pergunta(1)
            self.colocando_alternativas(1)
            self.btn_proximo['command'] = self.abrir_3
            self.voltar['command'] = self.voltar_menu

    def abrir_3(self):
        if self.selecionado.get() == 'vazio':
            mi = Messagebox.MessageboxInfo('images/messagebox.png','AVISO', 'Selecione uma alternativa')
            mi.orquestradora()
        else:
            self.lista.append(self.selecionado.get())
            self.label.destroy()
            self.a.destroy()
            self.b.destroy()
            self.c.destroy()
            self.d.destroy()
            self.pergunta.destroy()
            self.label_pergunta(2)
            self.colocando_alternativas(2)
            self.btn_proximo['command'] = self.abrir_4
            self.voltar['command'] = self.voltar_menu

    def abrir_4(self):
        
        if self.selecionado.get() == 'vazio':
            mi = Messagebox.MessageboxInfo('images/messageboxinfo.png','AVISO', 'Selecione uma alternativa')
            mi.orquestradora()
        else:
            self.lista.append(self.selecionado.get())
            self.label.destroy()
            self.a.destroy()
            self.b.destroy()
            self.c.destroy()
            self.d.destroy()
            self.pergunta.destroy()
            self.label_pergunta(3)
            self.colocando_alternativas(3)
            self.btn_proximo['command'] = self.abrir_5
            self.voltar['command'] = self.voltar_menu
        
    def abrir_5(self):

        if self.selecionado.get() == 'vazio':
            mi = Messagebox.MessageboxInfo('images/messagebox.png','AVISO', 'Selecione uma alternativa')
            mi.orquestradora()
        else:
            self.lista.append(self.selecionado.get())
            self.label.destroy()
            self.a.destroy()
            self.b.destroy()
            self.c.destroy()
            self.d.destroy()
            self.pergunta.destroy()
            self.label_pergunta(4)
            self.colocando_alternativas(4)
            self.btn_proximo['command'] = self.abrir_6
            self.voltar['command'] = self.voltar_menu
        
    def abrir_6(self):
        
        if self.selecionado.get() == 'vazio':
            mi = Messagebox.MessageboxInfo('images/messagebox.png','AVISO', 'Selecione uma alternativa')
            mi.orquestradora()
        else:
            self.lista.append(self.selecionado.get())
            self.label.destroy()
            self.a.destroy()
            self.b.destroy()
            self.c.destroy()
            self.d.destroy()
            self.pergunta.destroy()
            self.label_pergunta(5)
            self.colocando_alternativas(5)
            self.btn_proximo['command'] = self.abrir_7
            self.voltar['command'] = self.voltar_menu
        
    def abrir_7(self):
        
        if self.selecionado.get() == 'vazio':
            mi = Messagebox.MessageboxInfo('images/messagebox.png','AVISO', 'Selecione uma alternativa')
            mi.orquestradora()
        else:
            self.lista.append(self.selecionado.get())
            self.label.destroy()
            self.a.destroy()
            self.b.destroy()
            self.c.destroy()
            self.d.destroy()
            self.pergunta.destroy()
            self.label_pergunta(6)
            self.colocando_alternativas(6)
            self.btn_proximo['command'] = self.abrir_8
            self.voltar['command'] = self.voltar_menu

    def abrir_8(self):
        
        if self.selecionado.get() == 'vazio':
            mi = Messagebox.MessageboxInfo('images/messagebox.png','AVISO', 'Selecione uma alternativa')
            mi.orquestradora()
        else:
            self.lista.append(self.selecionado.get())
            self.label.destroy()
            self.a.destroy()
            self.b.destroy()
            self.c.destroy()
            self.d.destroy()
            self.pergunta.destroy()
            self.label_pergunta(7)
            self.colocando_alternativas(7)
            self.btn_proximo['command'] = self.abrir_9
            self.voltar['command'] = self.voltar_menu

    def abrir_9(self):
        
        if self.selecionado.get() == 'vazio':
            mi = Messagebox.MessageboxInfo('images/messagebox.png','AVISO', 'Selecione uma alternativa')
            mi.orquestradora()
        else:
            self.lista.append(self.selecionado.get())
            self.label.destroy()
            self.a.destroy()
            self.b.destroy()
            self.c.destroy()
            self.d.destroy()
            self.pergunta.destroy()
            self.label_pergunta(8)
            self.colocando_alternativas(8)
            self.btn_proximo['command'] = self.abrir_10
            self.voltar['command'] = self.voltar_menu
            
    def abrir_10(self):
        
        if self.selecionado.get() == 'vazio':
            mi = Messagebox.MessageboxInfo('images/messagebox.png','AVISO', 'Selecione uma alternativa')
            mi.orquestradora()
        else:
            self.lista.append(self.selecionado.get())
            self.label.destroy()
            self.a.destroy()
            self.b.destroy()
            self.c.destroy()
            self.d.destroy()
            self.pergunta.destroy()
            self.label_pergunta(9)
            self.colocando_alternativas(9)
            self.btn_proximo['bg'] = '#4285f4'
            self.btn_proximo['command'] = self.finalizar
            self.btn_proximo['text'] = 'Finalizar'
            self.voltar['command'] = self.voltar_menu


    def finalizar(self):
        self.lista_acertos = []
        self.lista_resultado = []
        self.lista.append(self.selecionado.get())
        
        valida_resposta = list(zip(self.lista, list(self.df_nv['RESP']))) 
        for v in valida_resposta:
            if v[0] + ' ' == v[1]:
                self.lista_resultado.append('CORRETO')
            else:
                self.lista_resultado.append('INCORRETO')

        for v in self.lista_resultado:
            if v == 'CORRETO':
                self.lista_acertos.append(v)
            else:
                pass

        self.acerto = str(len(self.lista_acertos))
        self.label_fundo.destroy()
        
        result = Resultado.Resultado('images/resultado.png', self.root)
        
        self.label_res = Label(text = self.acerto + '/' + '10',
                               background='white',
                               fg='black',
                               font = 'verdana 13')
        self.label_res.pack()
        self.label_res.place(x = 700, y = 210)

        tempo = self.stopwatch_label['text']

        self.label_tempo = Label(text = tempo,
                               background='white',
                               fg='black',
                               font = 'verdana 13')
        self.label_tempo.pack()
        self.label_tempo.place(x = 700, y = 275)

        query_update = '''UPDATE TBL_JOGADOR 
                          SET PONTUACAO = ?, TEMPO = ?
                          WHERE RA_JOGADOR = ?
        '''
        self.sql.cursor.execute(query_update, self.acerto, tempo, self.ra)
        self.sql.conexao.commit()
        result.orquestradora()


    def sel(self):

        self.texto = f'Você selecionou a alternativa {str(self.selecionado.get())}'
        self.label.config(text = self.texto)


    def colocando_alternativas(self, indice_pergunta):

        alternativas = self.df_nv[['altA','altB','altC','altD']].values[indice_pergunta]
        

        self.selecionado = StringVar(None, 'vazio')
        self.selecionado.set('vazio')

        self.a = Radiobutton(self.root, value='A' ,variable=self.selecionado,text=alternativas[0], borderwidth=0, bg = 'white', fg='black', font='verdana 11', command=self.sel)
        self.b = Radiobutton(self.root, value='B' ,variable=self.selecionado,text=alternativas[1], borderwidth=0, bg = 'white', fg='black', font='verdana 11', command=self.sel)
        self.c = Radiobutton(self.root, value='C' ,variable=self.selecionado,text=alternativas[2], borderwidth=0, bg = 'white', fg='black', font='verdana 11', command=self.sel)
        self.d = Radiobutton(self.root, value='D' ,variable=self.selecionado,text=alternativas[3], borderwidth=0, bg = 'white', fg='black', font='verdana 11', command=self.sel)

        self.a.pack()
        self.b.pack()
        self.c.pack()
        self.d.pack()

        self.a.place(x = 50, y = 200)
        self.b.place(x = 50, y = 260)
        self.c.place(x = 50, y = 320)
        self.d.place(x = 50, y = 380)

        self.label = Label(self.root, background = 'white', font='verdana 13')
        self.label.pack()
        self.label.place(x = 50, y = 440)


    def botao_proximo(self):

        borda_btn = Frame(self.root,
                          highlightthickness=1,
                          highlightbackground="#ffffff",)


        self.btn_proximo = Button(borda_btn,
                                 text='Próximo',
                                 font='Copper 16 bold',
                                 fg='white',
                                 borderwidth=False,
                                 bg='#28948A',
                                 height=45,
                                 width=105,
                                 command=self.resposta_usuario
                                 )
        self.btn_proximo.pack()
        borda_btn.pack()
        borda_btn.place(width=150, height=44, x=812, y = 500) 


    def criando_label(self):
        self.stopwatch_label = Label(self.root, text='00:00', font='verdana 15', bg='white')
        self.stopwatch_label.pack()
        self.stopwatch_label.place(x = 880, y = 125)


    def start(self):
        if not self.running:
            self.stopwatch_label.after(1000)
            self.update()
            self.running = True
    

    def reset(self):
        if self.running:
            self.stopwatch_label.after_cancel(self.update_time)
            self.running = False
        self.hours, self.minutes, self.seconds = 0, 0, 0
        self.stopwatch_label.config(text='00:00')


    def pause(self):
        if self.running:
            self.stopwatch_label.after_cancel(self.update_time)
            self.running = False


    def update(self):
        self.seconds += 1
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
        if self.minutes == 60:
            self.hours += 1
            self.minutes = 0
        hours_string = f'{self.hours}' if self.hours > 9 else f'0{self.hours}'
        minutes_string = f'{self.minutes}' if self.minutes > 9 else f'0{self.minutes}'
        seconds_string = f'{self.seconds}' if self.seconds > 9 else f'0{self.seconds}'
        self.stopwatch_label.config(text=minutes_string + ':' + seconds_string)
        self.update_time = self.stopwatch_label.after(1000, self.update)
    

    def orquestradora(self):
        self.sql.criando_conexao_sql()

        QuizJogo.lista_resposta_usuario(self)

        QuizJogo.base_pergunta(self)

        QuizJogo.perguntas_nivel_especifico(self)

        QuizJogo.botao_voltar(self)

        QuizJogo.botao_proximo(self)

        QuizJogo.label_pergunta(self, 0)

        QuizJogo.criando_label(self)

        QuizJogo.colocando_alternativas(self, indice_pergunta=0)
       
