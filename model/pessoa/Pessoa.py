class Pessoa:
    __slots__ = ('_id', '_nome', '_cpf')

    def __init__(self):
        self._id = None
        self._nome = None
        self._cpf = None

    @property
    def id(self): return self._id

    @property
    def nome(self): return self._nome

    @property
    def cpf(self): return self._cpf

    def __repr__(self):
        return f"Pessoa(id={self.id}, nome='{self.nome}', cpf='{self.cpf}')"
