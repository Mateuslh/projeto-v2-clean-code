import csv
import os

from config.Caminhos import PASTA_BANCO_DADOS
from model.reserva.Reserva import Reserva
from model.reserva.ReservaBuilder import ReservaBuilder
from model.reserva.StatusReserva import StatusReserva
from model.reserva.TipoQuarto import TipoQuarto

_ENCODING = "utf-8"
_ARQUIVO = os.path.join(PASTA_BANCO_DADOS, "Reservas.txt")
_CABECALHO = [
    "identificador", "status", "titular_id",
    "quantidade_pessoas", "numero_diarias",
    "tipo_quarto", "valor"
]


class ReservaRepository:
    @classmethod
    def salvar_ou_atualizar(cls, reserva: Reserva):
        reservas = cls.listar_todas()

        for i, existente in enumerate(reservas):
            if existente.identificador == reserva.identificador:
                reservas[i] = reserva
                break
        else:
            nova_reserva = (
                ReservaBuilder(reserva)
                .identificador(cls._proximo_id(reservas))
                .skip_validate_()
                .build()
            )
            reservas.append(nova_reserva)

    @classmethod
    def listar_todas(cls) -> list[Reserva]:
        if not os.path.exists(_ARQUIVO):
            return []
        with open(_ARQUIVO, newline="", encoding=_ENCODING) as file:
            leitor = csv.DictReader(file, fieldnames=_CABECALHO)
            return [cls._linha_para_reserva(l) for l in leitor]

    @staticmethod
    def _proximo_id(reservas: list[Reserva]) -> int:
        return max((r.identificador for r in reservas), default=0) + 1

    @staticmethod
    def _linha_para_reserva(dados: dict) -> Reserva:
        return (
            ReservaBuilder()
            .identificador(int(dados["identificador"]))
            .status(StatusReserva(dados["status"]))
            .titular_identificador(int(dados["titular_id"]))
            .quantidade_pessoas(int(dados["quantidade_pessoas"]))
            .numero_diarias(int(dados["numero_diarias"]))
            .tipo_quarto(TipoQuarto(dados["tipo_quarto"]))
            .calcular_valor()
            .skip_validate_()
            .build()
        )

    @classmethod
    def _escrever_todas(cls, reservas: list[Reserva]):
        with open(_ARQUIVO, "w", newline="", encoding=_ENCODING) as file:
            escritor = csv.writer(file)
            for r in reservas:
                escritor.writerow(
                    [
                        r.identificador,
                        r.status_reserva.value,
                        r.titular_identificador,
                        r.quantidade_pessoas,
                        r.numero_diarias,
                        r.tipo_quarto.value,
                        f"{r.valor_reserva:.2f}",
                    ]
                )
