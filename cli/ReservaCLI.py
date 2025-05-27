import time as t

from cli.PessoaCLI import PessoaCLI
from model.reserva.StatusReserva import StatusReserva
from model.reserva.TipoQuarto import TipoQuarto
from service.ReservaService import ReservaService
from service.RelatorioService import RelatorioService

COL_WIDTHS = (6, 12, 22)


def _linha(*valores):
    return "  ".join(str(v).ljust(w) for v, w in zip(valores, COL_WIDTHS))


class ReservaCLI:
    def __init__(self, reserva_service: ReservaService, pessoa_cli: PessoaCLI):
        self.reserva_service = reserva_service
        self.pessoa_cli = pessoa_cli

    # ---------- helpers ----------
    @staticmethod
    def _exibir_menu_tipo_quarto():
        print("\nTipo de Quarto")
        print(_linha("Código", "Descrição", "Tarifa (pessoa/noite)"))
        print(_linha("-" * 5, "-" * 10, "-" * 20))
        print(_linha("S", "Standard", "R$ 100,00"))
        print(_linha("D", "Deluxe", "R$ 200,00"))
        print(_linha("P", "Premium", "R$ 300,00"))
        print()

    @staticmethod
    def _capturar_tipo_quarto() -> TipoQuarto:
        ReservaCLI._exibir_menu_tipo_quarto()
        codigo = input("Tipo de quarto [S/D/P]: ").strip().upper()
        while codigo not in {"S", "D", "P"}:
            codigo = input("Inválido. Informe S, D ou P: ").strip().upper()
        return {"S": TipoQuarto.STANDARD,
                "D": TipoQuarto.DELUXE,
                "P": TipoQuarto.PREMIUM}[codigo]

    # ---------- opção 1 ----------
    def cadastrar_reserva(self):
        pessoa = self.pessoa_cli.buscar_ou_criar()
        quantidade = int(input("Quantidade de pessoas   : "))
        diarias = int(input("Número de diárias       : "))
        tipo_quarto = self._capturar_tipo_quarto()

        reserva = self.reserva_service.criar(
            pessoa.identificador, quantidade, diarias, tipo_quarto
        )
        print(f"\nReserva criada: {reserva}")
        t.sleep(1.2)

    # ---------- opção 2 ----------
    def check_in(self):
        entrada = input("CPF (11 dígitos) ou ID numérico do titular: ").strip()
        if len(entrada) == 11 and entrada.isdigit():  # CPF
            pessoa = self.pessoa_cli.pessoa_service.buscar_por_cpf(entrada)
            if not pessoa:
                print("CPF não encontrado.")
                return
            titular_id = pessoa.identificador
        else:  # ID
            titular_id = int(entrada)

        pendentes = [
            r for r in self.reserva_service.listar_por_titular(titular_id)
            if r.status_reserva == StatusReserva.RESERVADO
        ]
        if not pendentes:
            print("Nenhuma reserva aguardando check-in.")
            return
        for r in pendentes:
            print(r)
        reserva_id = int(input("ID para check-in: "))
        self.reserva_service.mudar_status(reserva_id, StatusReserva.ATIVO)
        print("Check-in concluído.")
        t.sleep(1)

    # ---------- opção 3 ----------
    def check_out(self):
        entrada = input("CPF (11 dígitos) ou ID numérico do titular: ").strip()
        if len(entrada) == 11 and entrada.isdigit():
            pessoa = self.pessoa_cli.pessoa_service.buscar_por_cpf(entrada)
            if not pessoa:
                print("CPF não encontrado.")
                return
            titular_id = pessoa.identificador
        else:
            titular_id = int(entrada)

        ativos = [
            r for r in self.reserva_service.listar_por_titular(titular_id)
            if r.status_reserva == StatusReserva.ATIVO
        ]
        if not ativos:
            print("Nenhuma reserva em hospedagem.")
            return
        for r in ativos:
            print(r)
        reserva_id = int(input("ID para check-out: "))
        self.reserva_service.mudar_status(reserva_id, StatusReserva.FINALIZADO)
        print("Check-out concluído.")
        t.sleep(1)

    # ---------- opção 4 ----------
    def alterar_reserva(self):
        entrada = input("CPF (11 dígitos) ou ID numérico do titular: ").strip()
        if len(entrada) == 11 and entrada.isdigit():
            pessoa = self.pessoa_cli.pessoa_service.buscar_por_cpf(entrada)
            if not pessoa:
                print("CPF não encontrado.")
                return
            titular_id = pessoa.identificador
        else:
            titular_id = int(entrada)

        editaveis = [
            r for r in self.reserva_service.listar_por_titular(titular_id)
            if r.status_reserva == StatusReserva.RESERVADO
        ]
        if not editaveis:
            print("Nenhuma reserva alterável.")
            return
        for r in editaveis:
            print(r)
        reserva_id = int(input("ID para alterar/cancelar: "))
        acao = input("[C]ancelar | [E]ditar: ").strip().upper()

        if acao == "C":
            self.reserva_service.mudar_status(reserva_id, StatusReserva.CANCELADO)
            print("Reserva cancelada.")
        else:
            quantidade = int(input("Nova quantidade pessoas : "))
            diarias = int(input("Novo número de diárias : "))
            tipo_quarto = self._capturar_tipo_quarto()
            self.reserva_service.alterar_reserva(
                reserva_id, quantidade, diarias, tipo_quarto
            )
            print("Reserva atualizada.")
        t.sleep(1)

    # ---------- opção 5 ----------
    def relatorios(self):
        print("\nRelatórios disponíveis")
        print("1 - Reservas R (Reservado)")
        print("2 - Reservas C (Cancelado)")
        print("3 - Reservas A (Ativo)")
        print("4 - Reservas F (Finalizado)")
        print("5 - Total recebido")
        print("6 - Reservas por titular\n")

        escolha = input("Opção: ").strip()

        if escolha in {"1", "2", "3", "4"}:
            status = {
                "1": StatusReserva.RESERVADO,
                "2": StatusReserva.CANCELADO,
                "3": StatusReserva.ATIVO,
                "4": StatusReserva.FINALIZADO,
            }[escolha]
            caminho = RelatorioService.reservas_por_status(status)
        elif escolha == "5":
            caminho = RelatorioService.total_recebido()
        else:
            titular_id = int(input("Titular ID: "))
            caminho = RelatorioService.reservas_por_titular(titular_id)

        print(f"Arquivo gerado em: {caminho}")
        t.sleep(2)
