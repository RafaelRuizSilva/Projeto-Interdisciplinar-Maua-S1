from tkinter import *
from PIL import ImageTk, Image
import pandas as pd


class PlanoDeFundo:
    def __init__(self, imagem_fundo, root):
        self.root = root
        # Colocando fundo
        self.fundo = ImageTk.PhotoImage(Image.open(imagem_fundo))

        # Criando label para colocar o fundo
        self.label_fundo = Label(self.root, image=self.fundo)
        self.label_fundo.pack()