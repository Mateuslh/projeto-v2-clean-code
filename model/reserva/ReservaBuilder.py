from __future__ import annotations

from common.AbstractBuilder import AbstractBuilder
from model.reserva.Reserva import Reserva
from model.reserva.ReservaSpecification import ReservaSpecification
from model.reserva.TipoQuarto import TipoQuarto


class ReservaBuilder(AbstractBuilder):
    def __init__(self, reserva_original: "Reserva" | None = None):
        super().__init__(reserva_original)

    def _create_entity(self):
        return Reserva()

    def identificador(self, identificador: int):
        self.entity._identificador = identificador
        return self

    def titular_identificador(self, titular_identificador: int):
        self.entity._titular_identificador = titular_identificador
        return self

    def status(self, status):
        self.entity._status_reserva = status
        return self

    def quantidade_pessoas(self, quantidade: int):
        self.entity._quantidade_pessoas = quantidade
        return self

    def numero_diarias(self, diarias: int):
        self.entity._numero_diarias = diarias
        return self

    def tipo_quarto(self, tipo: TipoQuarto):
        self.entity._tipo_quarto = tipo
        return self

    def calcular_valor(self):
        reserva = self.entity
        reserva._valor_reserva = (
                reserva.tipo_quarto.tarifa
                * reserva.quantidade_pessoas
                * reserva.numero_diarias
        )
        return self

    def tipo_quarto_e_valor(self, tipo: TipoQuarto):
        return self.tipo_quarto(tipo).calcular_valor()

    def validate(self):
        ReservaSpecification.validar(self.entity)
