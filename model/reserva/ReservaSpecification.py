from model.reserva.Reserva import Reserva


class ReservaSpecification:

    @staticmethod
    def validar_id_titular(reserva: Reserva):
        if reserva.idTitular is None:
            raise ValueError("O campo 'idTitular' é obrigatório.")

    @staticmethod
    def validar_status(reserva: Reserva):
        if reserva.statusReserva not in ("PENDENTE", "CONFIRMADA", "CANCELADA"):
            raise ValueError("O status da reserva deve ser 'PENDENTE', 'CONFIRMADA' ou 'CANCELADA'.")

    @staticmethod
    def validar_quantidade_pessoas(reserva: Reserva):
        if reserva.qntPessoas is None or reserva.qntPessoas < 1:
            raise ValueError("A quantidade de pessoas deve ser maior ou igual a 1.")

    @staticmethod
    def validar_diarias(reserva: Reserva):
        if reserva.diarias is None or reserva.diarias < 1:
            raise ValueError("O número de diárias deve ser maior ou igual a 1.")

    @staticmethod
    def validar_tipo_quarto(reserva: Reserva):
        if not reserva.tipoQuarto:
            raise ValueError("O tipo de quarto é obrigatório.")

    @staticmethod
    def validar_valor_reserva(reserva: Reserva):
        if reserva.valorReserva is None or reserva.valorReserva < 0:
            raise ValueError("O valor da reserva deve ser maior ou igual a 0.")
