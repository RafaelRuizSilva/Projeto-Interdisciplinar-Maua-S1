from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
from Planodefundo import PlanoDeFundo
import Voltar_Tela_Principal
import pygame

class Slide1(PlanoDeFundo):

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
                                 activebackground='#28948A',
                                 command=self.abrir_slide2
                                 )
        self.btn_proximo.pack()
        borda_btn.pack()
        borda_btn.place(width=150, height=44, x=812, y = 500) 


    def botao_hover(self):
        self.btn_proximo.bind('<Enter>', self.button_hover)
        self.btn_proximo.bind('<Leave>', self.button_leave)    


    def button_hover(self, e):
        self.btn_proximo['fg'] = 'black'
        self.btn_proximo['bg'] = '#148378'

    def button_leave(self, e):
        self.btn_proximo['fg'] = 'white'
        self.btn_proximo['bg'] = '#28948A'

    
    def abrir_slide2(self):
        try:
            self.btn_proximo.destroy()
        except:
            pass
        try:
            self.label_fundo.destroy()
        except:
            pass

        slide2 = Slide2('slidesTutorial/', self.root)

        slide2.orquestradora()

    def orquestradora(self):

        Slide1.botao_proximo(self)

        Slide1.botao_hover(self)


class Slide2(PlanoDeFundo):

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
                                 activebackground='#28948A',
                                 command=self.abrir_slide3
                                 )
        self.btn_proximo.pack()
        borda_btn.pack()
        borda_btn.place(width=150, height=44, x=812, y = 500)


    def botao_hover(self):
        self.btn_proximo.bind('<Enter>', self.button_hover)
        self.btn_proximo.bind('<Leave>', self.button_leave)    


    def button_hover(self, e):
        self.btn_proximo['fg'] = 'black'
        self.btn_proximo['bg'] = '#148378'


    def button_leave(self, e):
        self.btn_proximo['fg'] = 'white'
        self.btn_proximo['bg'] = '#28948A'

    
    def abrir_slide3(self):
        try:
            self.btn_proximo.destroy()
        except:
            pass
        try:
            self.label_fundo.destroy()
        except:
            pass

        slide3 = Slide3('slidesTutorial/', self.root)

        slide3.orquestradora()


    def orquestradora(self):

        Slide2.botao_proximo(self)

        Slide2.botao_hover(self)

class Slide3(PlanoDeFundo):

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
                                 activebackground='#28948A',
                                 command=self.abrir_slide4
                                 )
        self.btn_proximo.pack()
        borda_btn.pack()
        borda_btn.place(width=150, height=44, x=812, y = 500) 


    def botao_hover(self):
        self.btn_proximo.bind('<Enter>', self.button_hover)
        self.btn_proximo.bind('<Leave>', self.button_leave)    


    def button_hover(self, e):
        self.btn_proximo['fg'] = 'black'
        self.btn_proximo['bg'] = '#148378'

    def button_leave(self, e):
        self.btn_proximo['fg'] = 'white'
        self.btn_proximo['bg'] = '#28948A'

    
    def abrir_slide4(self):
        try:
            self.btn_proximo.destroy()
        except:
            pass
        try:
            self.label_fundo.destroy()
        except:
            pass

        slide4 = Slide4('slidesTutorial/', self.root)

        slide4.orquestradora()

    def orquestradora(self):

        Slide3.botao_proximo(self)

        Slide3.botao_hover(self)


class Slide4(PlanoDeFundo):

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
                                 activebackground='#28948A',
                                 command=self.abrir_slide5
                                 )
        self.btn_proximo.pack()
        borda_btn.pack()
        borda_btn.place(width=150, height=44, x=812, y = 500) 


    def botao_hover(self):
        self.btn_proximo.bind('<Enter>', self.button_hover)
        self.btn_proximo.bind('<Leave>', self.button_leave)    


    def button_hover(self, e):
        self.btn_proximo['fg'] = 'black'
        self.btn_proximo['bg'] = '#148378'

    def button_leave(self, e):
        self.btn_proximo['fg'] = 'white'
        self.btn_proximo['bg'] = '#28948A'

    
    def abrir_slide5(self):
        try:
            self.btn_proximo.destroy()
        except:
            pass
        try:
            self.label_fundo.destroy()
        except:
            pass

        slide5 = Slide5('slidesTutorial/', self.root)

        slide5.orquestradora()

    def orquestradora(self):

        Slide4.botao_proximo(self)

        Slide4.botao_hover(self)


class Slide5(PlanoDeFundo):

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
                                 activebackground='#28948A',
                                 command=self.abrir_slide6
                                 )
        self.btn_proximo.pack()
        borda_btn.pack()
        borda_btn.place(width=150, height=44, x=812, y = 500) 


    def botao_hover(self):
        self.btn_proximo.bind('<Enter>', self.button_hover)
        self.btn_proximo.bind('<Leave>', self.button_leave)    


    def button_hover(self, e):
        self.btn_proximo['fg'] = 'black'
        self.btn_proximo['bg'] = '#148378'

    def button_leave(self, e):
        self.btn_proximo['fg'] = 'white'
        self.btn_proximo['bg'] = '#28948A'

    
    def abrir_slide6(self):
        try:
            self.btn_proximo.destroy()
        except:
            pass
        try:
            self.label_fundo.destroy()
        except:
            pass

        slide6 = Slide6('slidesTutorial/', self.root)

        slide6.orquestradora()

    def orquestradora(self):

        Slide5.botao_proximo(self)

        Slide5.botao_hover(self)


class Slide6(PlanoDeFundo):

    def botao_voltar_menu(self):

        borda_btn = Frame(self.root,
                          highlightthickness=1,
                          highlightbackground="#ffffff",)


        self.btn_proximo = Button(borda_btn,
                                 text='Voltar Menu',
                                 font='Copper 16 bold',
                                 fg='white',
                                 borderwidth=False,
                                 bg='#4285f4',
                                 height=45,
                                 width=105,
                                 activebackground='#4285f4',
                                 command=self.voltar_menu
                                 )
        self.btn_proximo.pack()
        borda_btn.pack()
        borda_btn.place(width=150, height=44, x=812, y = 500)

    def voltar_menu(self):
        self.label_fundo.destroy()

        self.tocar_audio()

        vp = Voltar_Tela_Principal.TelaPrincipal('images/tela_principal.png', self.root)

        vp.orquestrador()


    def botao_hover(self):
        self.btn_proximo.bind('<Enter>', self.button_hover)
        self.btn_proximo.bind('<Leave>', self.button_leave)    


    def button_hover(self, e):
        self.btn_proximo['fg'] = 'black'
        self.btn_proximo['bg'] = '#4285f4'


    def button_leave(self, e):
        self.btn_proximo['fg'] = 'white'
        self.btn_proximo['bg'] = '#4285f4'

    def tocar_audio(self):
        pygame.init()
        pygame.mixer.music.load('audios/posso_dormir_em_paz.mp3')
        pygame.mixer.music.play()
        pygame.event.wait()

    def orquestradora(self):

        Slide6.botao_voltar_menu(self)

        Slide6.botao_hover(self)