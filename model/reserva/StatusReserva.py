from enum import Enum


class StatusReserva(str, Enum):
    RESERVADO = "R"
    ATIVO = "A"
    FINALIZADO = "F"
    CANCELADO = "C"
