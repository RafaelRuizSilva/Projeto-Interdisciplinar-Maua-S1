from tkinter import *
from tokenize import String
from PIL import ImageTk, Image
import pandas as pd

class MessageboxErro():
    def __init__(self, imagem_fundo, mensagem_titulo, mensagem_principal):
        
        # CRIANDO TOPLEVEL
        self.root = Toplevel()

        self.root.grab_set()
        self.root.withdraw()

        # geometria da tela
        self.root.geometry('400x250')

        # LENDO IMAGEM  DE FUNDO
        self.fundo = ImageTk.PhotoImage(Image.open(imagem_fundo))

        # Criando label para colocar o fundo
        self.label_fundo = Label(self.root, image=self.fundo)
        self.label_fundo.pack()

        # COLOCANDO TÍTULO
        self.root.title(mensagem_titulo)

        # MENSAGEM
        self.mensagem = mensagem_principal

        # COLOCANDO ICONE
        self.root.iconbitmap('images/erro.ico')

        # RETIRANDO A POSSIBILIDADE DO USUARIO DE MEXER
        self.root.resizable(False, False)


    def centralizar_tela(self):
        
        self.root.withdraw()
        largura = 450
        altura = 250
        largura_screen = self.root.winfo_screenwidth()
        altura_screen = self.root.winfo_screenheight()
        posx = largura_screen / 2 - largura / 2
        posy = altura_screen / 2 - altura / 2
        self.root.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))
        self.root.deiconify()

    def label_texto_principal(self):

        self.texto = Label(self.root,
                           text = self.mensagem,
                           font = 'verdana 13',
                           bg = 'white')
        self.texto.pack()
        self.texto.place(x = 90, y = 90)


    def botao_ok(self):

        self.borda_btn_ok = Frame(self.root,
                          highlightthickness=1,
                          highlightbackground="black",)

        self.ok = Button(self.borda_btn_ok,
                        text = 'OK',
                        bg = 'red',
                        fg = 'white',
                        font = 'verdana 18 bold',
                        command = self.fechar,
                        borderwidth= 0,
                        activebackground='red',
                        width=100, height=32, activeforeground='white')
        self.ok.pack()
        self.borda_btn_ok.pack()
        self.borda_btn_ok.place(x = 175, y = 200, width=100, height=32)


    def fechar(self):
        self.root.destroy()
        

    def executar(self):
        self.root.mainloop()


    def orquestradora(self):
        
        MessageboxErro.centralizar_tela(self)

        MessageboxErro.label_texto_principal(self)

        MessageboxErro.botao_ok(self)
        


class MessageboxInfo():
    def __init__(self, imagem_fundo, mensagem_titulo, mensagem_principal):
        
        
        # CRIANDO TOPLEVEL
        self.root = Toplevel()

        self.root.grab_set()
        self.root.withdraw()
        # geometria da tela
        self.root.geometry('400x250')

        self.fundo = ImageTk.PhotoImage(Image.open(imagem_fundo))

        # Criando label para colocar o fundo
        self.label_fundo = Label(self.root, image=self.fundo)
        self.label_fundo.pack()

        # criando titulo
        self.root.title(mensagem_titulo)

        # mensagem do corpo do box
        self.mensagem = mensagem_principal

        # colocando icone
        self.root.iconbitmap('images/info.ico')

        # RETIRANDO A POSSIBILIDADE DO USUARIO DE MEXER
        self.root.resizable(False, False)


    def centralizar_tela(self):
        
        
        largura = 450
        altura = 250
        largura_screen = self.root.winfo_screenwidth()
        altura_screen = self.root.winfo_screenheight()
        posx = largura_screen / 2 - largura / 2
        posy = altura_screen / 2 - altura / 2
        self.root.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))
        self.root.deiconify()
    def label_texto_principal(self):

        self.texto = Label(self.root,
                           text = self.mensagem,
                           font = 'verdana 13',
                           bg = 'white')
        self.texto.pack()
        self.texto.place(x = 100, y = 90)


    def botao_ok(self):

        self.borda_btn_ok = Frame(self.root,
                          highlightthickness=1,
                          highlightbackground="black",)

        self.ok = Button(self.borda_btn_ok,
                        text = 'OK',
                        bg = '#03c5ff',
                        fg = 'white',
                        font = 'verdana 18 bold',
                        command = self.fechar,
                        borderwidth= 0,
                        activebackground='#03c5ff',
                        width=100, height=32, activeforeground='white')
        self.ok.pack()
        self.borda_btn_ok.pack()
        self.borda_btn_ok.place(x = 175, y = 200, width=100, height=32)


    def fechar(self):
        self.root.destroy()
        

    def executar(self):
        self.root.mainloop()


    def orquestradora(self):
        
        MessageboxInfo.centralizar_tela(self)

        MessageboxInfo.label_texto_principal(self)

        MessageboxInfo.botao_ok(self)
        


# if __name__ == '__main__':

#     mb = Messagebox('images/messagebox.png')

#     mb.orquestradora()