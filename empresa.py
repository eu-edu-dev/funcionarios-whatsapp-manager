from typing import Dict
import pandas as pd
from envia_whatsapp import WhatsappManager
from funcionario import Funcionario


class Empresa:
    def __init__(self, nome, planilha=''):
        self.nome = nome
        self.planilha = planilha
        if planilha:
            self.funcionarios: "Dict[int, Funcionario]" = {}
            self.criar_funcionarios()

    def criar_funcionarios(self):
        self.df = pd.read_excel(self.planilha)
        
        for index, row in self.df.iterrows():
            funcionario = Funcionario(
                index, row['Nome'], row['Cargo'],
                row['Aniversário'], row['Telefone'],
                row['Email'], self.df
            )
            self.funcionarios[index] = funcionario

        return self.funcionarios

    def salvar_alteracoes(self):
        self.df.to_excel(self.planilha, index=False)

    def enviar_mensagens_para_todos(self, mensagem):
        mensagens = [
            {"message": mensagem, "phone":f.telefone}
            for f in self.funcionarios
        ]
        WhatsappManager(mensagens)
