from model.reserva.Reserva import Reserva
from model.reserva.StatusReserva import StatusReserva
from model.reserva.TipoQuarto import TipoQuarto

# Mapa de transições permitidas
_TRANSICOES = {
    StatusReserva.RESERVADO:  {StatusReserva.ATIVO, StatusReserva.CANCELADO},
    StatusReserva.ATIVO:      {StatusReserva.FINALIZADO},
    StatusReserva.FINALIZADO: set(),
    StatusReserva.CANCELADO:  set(),
}


class ReservaSpecification:
    @staticmethod
    def validar(reserva: Reserva):
        ReservaSpecification._validar_titular(reserva)
        ReservaSpecification._validar_status(reserva)
        ReservaSpecification._validar_quantidade_pessoas(reserva)
        ReservaSpecification._validar_numero_diarias(reserva)
        ReservaSpecification._validar_tipo_quarto(reserva)
        ReservaSpecification._validar_valor(reserva)

    @staticmethod
    def validar_transicao_status(status_atual: StatusReserva,
                                 novo_status: StatusReserva):
        if novo_status not in _TRANSICOES[status_atual]:
            raise ValueError(
                f"Transição de {status_atual} para {novo_status} não permitida."
            )


    @staticmethod
    def _validar_titular(reserva: Reserva):
        if reserva.titular_identificador is None:
            raise ValueError("Titular da reserva é obrigatório.")

    @staticmethod
    def _validar_status(reserva: Reserva):
        if not isinstance(reserva.status_reserva, StatusReserva):
            raise ValueError("Status da reserva inválido.")

    @staticmethod
    def _validar_quantidade_pessoas(reserva: Reserva):
        if reserva.quantidade_pessoas < 1:
            raise ValueError("Quantidade de pessoas deve ser >= 1.")

    @staticmethod
    def _validar_numero_diarias(reserva: Reserva):
        if reserva.numero_diarias < 1:
            raise ValueError("Número de diárias deve ser >= 1.")

    @staticmethod
    def _validar_tipo_quarto(reserva: Reserva):
        if not isinstance(reserva.tipo_quarto, TipoQuarto):
            raise ValueError("Tipo de quarto inválido.")

    @staticmethod
    def _validar_valor(reserva: Reserva):
        if reserva.valor_reserva < 0:
            raise ValueError("Valor da reserva deve ser não negativo.")
