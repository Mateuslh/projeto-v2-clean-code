from model.reserva.StatusReserva import StatusReserva
from model.reserva.TipoQuarto import TipoQuarto


class Reserva:
    __slots__ = ("_identificador", "_titular_identificador", "_status_reserva", "_quantidade_pessoas",
                 "_numero_diarias", "_tipo_quarto", "_valor_reserva")

    def __init__(self):
        self._identificador: int | None = None
        self._titular_identificador: int | None = None
        self._status_reserva: StatusReserva = StatusReserva.RESERVADO
        self._quantidade_pessoas: int = 1
        self._numero_diarias: int = 1
        self._tipo_quarto: TipoQuarto = TipoQuarto.STANDARD
        self._valor_reserva: float = 0.0  # calculado no builder


    @property
    def identificador(self): return self._identificador

    @property
    def titular_identificador(self): return self._titular_identificador

    @property
    def status_reserva(self): return self._status_reserva

    @property
    def quantidade_pessoas(self): return self._quantidade_pessoas

    @property
    def numero_diarias(self): return self._numero_diarias

    @property
    def tipo_quarto(self): return self._tipo_quarto

    @property
    def valor_reserva(self): return self._valor_reserva


    def __repr__(self):
        return (f"Reserva(identificador={self.identificador}, "
                f"titular={self.titular_identificador}, "
                f"status={self.status_reserva}, "
                f"pessoas={self.quantidade_pessoas}, "
                f"diarias={self.numero_diarias}, "
                f"quarto={self.tipo_quarto}, "
                f"valor={self.valor_reserva:.2f})\")")
