class Reserva:
    __slots__ = ("_id", "_idTitular", "_statusReserva", "_qntPessoas", "_diarias", "_tipoQuarto", "_valorReserva")

    def __init__(self):
        self._id = None
        self._idTitular = None
        self._statusReserva = None
        self._qntPessoas = None
        self._diarias = None
        self._tipoQuarto = None
        self._valorReserva = None

    @property
    def id(self): return self._id

    @property
    def idTitular(self): return self._idTitular

    @property
    def statusReserva(self): return self._statusReserva

    @property
    def qntPessoas(self): return self._qntPessoas

    @property
    def diarias(self): return self._diarias

    @property
    def tipoQuarto(self): return self._tipoQuarto

    @property
    def valorReserva(self): return self._valorReserva

    def __repr__(self):
        return (f"Reserva(id={self.id}, idTitular={self.idTitular}, status='{self.statusReserva}', "
                f"qntPessoas={self.qntPessoas}, diarias={self.diarias}, tipoQuarto='{self.tipoQuarto}', "
                f"valorReserva={self.valorReserva:.2f})")
