import os
from model.reserva.Reserva import Reserva
from model.reserva.ReservaBuilder import ReservaBuilder


class ReservaRepository:
    FILE_PATH = 'Reservas.txt'
    SEPARATOR = ','
    EXPECTED_FIELDS = 8
    DEFAULT_ID = 0
    NEW_LINE = '\n'

    @classmethod
    def save_or_update(cls, reserva: Reserva):
        reservas = cls.listar_todas()

        for i, r in enumerate(reservas):
            if r.id == reserva.id:
                reservas[i] = reserva
                break
        else:
            reserva = ReservaBuilder(reserva).id(cls._next_id(reservas)).skip_validate_().build()
            reservas.append(reserva)

        with open(cls.FILE_PATH, 'w', encoding='utf-8') as file:
            file.writelines(cls._format(r) + cls.NEW_LINE for r in reservas)

    @classmethod
    def listar_todas(cls) -> list[Reserva]:
        if not os.path.exists(cls.FILE_PATH):
            return []
        with open(cls.FILE_PATH, 'r', encoding='utf-8') as file:
            return [cls._parse(line) for line in file if cls._valid_line(line)]

    @staticmethod
    def _next_id(reservas: list[Reserva]) -> int:
        return max((r.id for r in reservas), default=ReservaRepository.DEFAULT_ID) + 1

    @classmethod
    def _valid_line(cls, line: str) -> bool:
        return len(line.strip().split(cls.SEPARATOR)) == cls.EXPECTED_FIELDS

    @classmethod
    def _parse(cls, line: str) -> Reserva:
        dados = line.strip().split(cls.SEPARATOR)
        return ReservaBuilder() \
            .id(int(dados[0])) \
            .statusReserva(dados[1]) \
            .idTitular(dados[2]) \
            .qntPessoas(int(dados[4])) \
            .diarias(int(dados[5])) \
            .tipoQuarto(dados[6]) \
            .valorReserva(float(dados[7])) \
            .skip_validate_() \
            .build()

    @staticmethod
    def _format(reserva: Reserva) -> str:
        return f"{reserva.id},{reserva.statusReserva},{reserva.idTitular},{reserva.idTitular},{reserva.qntPessoas},{reserva.diarias},{reserva.tipoQuarto},{reserva.valorReserva:.2f}"
