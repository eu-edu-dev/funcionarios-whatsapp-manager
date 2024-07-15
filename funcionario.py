class Funcionario:
    def __init__(self, index, nome, cargo, aniversario, telefone, email, df):
        self.index = index
        self._nome = nome
        self._cargo = cargo
        self._aniversario = aniversario
        self._telefone = telefone
        self._email = email
        self._df = df

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value
        self._df.at[self.index, 'Nome'] = value

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, value):
        self._cargo = value
        self._df.at[self.index, 'Cargo'] = value

    @property
    def aniversario(self):
        return self._aniversario

    @aniversario.setter
    def aniversario(self, value):
        self._aniversario = value
        self._df.at[self.index, 'Aniversário'] = value

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, value):
        self._telefone = value
        self._df.at[self.index, 'Telefone'] = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
        self._df.at[self.index, 'Email'] = value

    def __repr__(self):
        return f"Funcionario(nome={self.nome}, cargo={self.cargo})"