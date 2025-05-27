class Pessoa:
    __slots__ = ("_identificador", "_nome", "_cpf")

    def __init__(self):
        self._identificador: int | None = None
        self._nome:           str | None = None
        self._cpf:            str | None = None

    @property
    def identificador(self):
        return self._identificador

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    def __repr__(self):
        return (f"Pessoa(identificador={self.identificador}, "
                f"nome='{self.nome}', cpf='{self.cpf}')")
