import os
import csv
import datetime as dt

from config.Caminhos import PASTA_RELATORIOS
from model.reserva.StatusReserva import StatusReserva
from repository.ReservaRepository import ReservaRepository


class RelatorioService:
    @staticmethod
    def _caminho(nome: str) -> str:
        return os.path.join(PASTA_RELATORIOS, nome)

    @classmethod
    def reservas_por_status(cls, status: StatusReserva) -> str:
        caminho = cls._caminho(f"Reservas_{status.value}.csv")
        reservas = [
            r for r in ReservaRepository.listar_todas()
            if r.status_reserva == status
        ]
        cls._escrever_reservas_csv(caminho, reservas)
        return caminho

    @classmethod
    def reservas_por_titular(cls, titular_id: int) -> str:
        caminho = cls._caminho(f"Titular_{titular_id}.csv")
        reservas = [
            r for r in ReservaRepository.listar_todas()
            if r.titular_identificador == titular_id
        ]
        cls._escrever_reservas_csv(caminho, reservas)
        return caminho

    @classmethod
    def total_recebido(cls) -> str:
        caminho = cls._caminho("Total_Recebido.txt")
        total = sum(
            r.valor_reserva for r in ReservaRepository.listar_todas()
            if r.status_reserva == StatusReserva.FINALIZADO
        )
        with open(caminho, "w", encoding='utf-8') as arq:
            arq.write(f"Gerado em {dt.datetime.now():%d/%m/%Y %H:%M:%S}\n")
            arq.write(f"Total recebido: {total:.2f}\n")
        return caminho

    @staticmethod
    def _escrever_reservas_csv(caminho: str, reservas: list):
        with open(caminho, "w", newline="", encoding='utf-8') as file:
            escritor = csv.writer(file)
            escritor.writerow(
                [
                    "ID", "Status", "Titular", "Pessoas",
                    "Diárias", "Quarto", "Valor"
                ]
            )
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
