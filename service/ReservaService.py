from repository.ReservaRepository import ReservaRepository
from model.reserva.ReservaBuilder import ReservaBuilder
from model.reserva.StatusReserva import StatusReserva
from model.reserva.TipoQuarto import TipoQuarto
from model.reserva.ReservaSpecification import ReservaSpecification


class ReservaService:
    def criar(self, titular_id: int, quantidade_pessoas: int,
              numero_diarias: int, tipo_quarto: TipoQuarto):
        reserva = (
            ReservaBuilder()
            .titular_identificador(titular_id)
            .quantidade_pessoas(quantidade_pessoas)
            .numero_diarias(numero_diarias)
            .tipo_quarto_e_valor(tipo_quarto)
            .build()
        )
        ReservaRepository.salvar_ou_atualizar(reserva)
        return reserva

    def listar_por_cpf_e_status(self, cpf: str, status_conjunto: set[StatusReserva]):
        return [
            r for r in ReservaRepository.listar_todas()
            if r.status_reserva in status_conjunto and r.titular_identificador == cpf
        ]

    def listar_por_titular(self, titular_id: int):
        return [
            r for r in ReservaRepository.listar_todas()
            if r.titular_identificador == titular_id
        ]

    def buscar_por_id(self, reserva_id: int):
        return next(
            (r for r in ReservaRepository.listar_todas()
             if r.identificador == reserva_id),
            None
        )

    def mudar_status(self, reserva_id: int, novo_status: StatusReserva):
        reserva_antiga = self.buscar_por_id(reserva_id)
        ReservaSpecification.validar_transicao_status(
            reserva_antiga.status_reserva, novo_status
        )

        reserva_nova = (
            ReservaBuilder(reserva_antiga)
            .status(novo_status)
            .build()
        )
        ReservaRepository.salvar_ou_atualizar(reserva_nova)

    def alterar_reserva(self, reserva_id: int, quantidade_pessoas: int,
                        numero_diarias: int, tipo_quarto: TipoQuarto):
        reserva_antiga = self.buscar_por_id(reserva_id)
        if reserva_antiga.status_reserva != StatusReserva.RESERVADO:
            raise ValueError("Apenas reservas com status R podem ser alteradas.")

        reserva_nova = (
            ReservaBuilder(reserva_antiga)
            .quantidade_pessoas(quantidade_pessoas)
            .numero_diarias(numero_diarias)
            .tipo_quarto(tipo_quarto)
            .calcular_valor()
            .build()
        )
        ReservaRepository.salvar_ou_atualizar(reserva_nova)

    def somatorio_finalizado(self):
        return sum(
            r.valor_reserva for r in ReservaRepository.listar_todas()
            if r.status_reserva == StatusReserva.FINALIZADO
        )

    def reservas_por_status(self, status: StatusReserva):
        return [
            r for r in ReservaRepository.listar_todas()
            if r.status_reserva == status
        ]
