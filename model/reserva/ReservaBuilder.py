from common.AbstractBuilder import AbstractBuilder
from model.reserva.Reserva import Reserva
from model.reserva.ReservaSpecification import ReservaSpecification


class ReservaBuilder(AbstractBuilder):
    def create_entity(self):
        return Reserva()

    def id(self, id: int):
        self.entity._id = id
        return self

    def idTitular(self, idTitular: int):
        self.entity._idTitular = idTitular
        return self

    def statusReserva(self, status: str):
        self.entity._statusReserva = status
        return self

    def qntPessoas(self, qnt: int):
        self.entity._qntPessoas = qnt
        return self

    def diarias(self, diarias: int):
        self.entity._diarias = diarias
        return self

    def tipoQuarto(self, tipo: str):
        self.entity._tipoQuarto = tipo
        return self

    def valorReserva(self, valor: float):
        self.entity._valorReserva = valor
        return self

    def validate(self):
        reserva = self.entity
        ReservaSpecification.validar_id_titular(reserva)
        ReservaSpecification.validar_status(reserva)
        ReservaSpecification.validar_quantidade_pessoas(reserva)
        ReservaSpecification.validar_diarias(reserva)
        ReservaSpecification.validar_tipo_quarto(reserva)
        ReservaSpecification.validar_valor_reserva(reserva)
