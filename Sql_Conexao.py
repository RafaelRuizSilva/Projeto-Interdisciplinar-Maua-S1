import pyodbc
import pandas as pd
'''
            Função que cria a conexão do python com o SQL Server

            # Arguments:
                    hostname = Nome do seu computador (pode ser encontrado
                    digitando no cmd "hostname" sem as aspas)

                    banco_de_dados = Nome do banco de dados que deseja
                    estabelecer a conexão

            # Return:
                    conexão bem sucedida
        '''

class sqlComandos():
    def __init__(self, hostname, banco_de_dados):
        self.server = hostname
        self.database = banco_de_dados
    

    def criando_conexao_sql(self):
        try:
            self.conexao = pyodbc.connect('DRIVER={SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';')
            self.cursor = self.conexao.cursor()
            print('Conexão bem sucedida!!!')
        except:
            print('Erro ao criar conexão com o SQL')
        

    def conexao(self):
        return self.conexao


    def cursor(self):
        return self.cursor



    
    