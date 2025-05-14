import os
from model.pessoa.Pessoa import Pessoa
from model.pessoa.PessoaBuilder import PessoaBuilder


class PessoaRepository:
    FILE_PATH = 'Pessoas.txt'
    SEPARATOR = ','
    EXPECTED_FIELDS = 3
    DEFAULT_ID = 0
    NEW_LINE = '\n'

    @classmethod
    def save_or_update(cls, pessoa: Pessoa):
        pessoas = cls.listar_todas()

        for i, p in enumerate(pessoas):
            if p.id == pessoa.id:
                pessoas[i] = pessoa
                break
        else:
            pessoa = PessoaBuilder(pessoa).id(cls._next_id(pessoas)).skip_validate_().build()
            pessoas.append(pessoa)

        with open(cls.FILE_PATH, 'w', encoding='utf-8') as file:
            file.writelines(cls._format(p) + cls.NEW_LINE for p in pessoas)

    @classmethod
    def buscar_por_id(cls, id_pessoa: int) -> Pessoa:
        pessoas = cls.listar_todas()
        for pessoa in pessoas:
            if pessoa.id == id_pessoa:
                return pessoa
        raise ValueError(f"Pessoa com id {id_pessoa} não encontrada.")

    @classmethod
    def listar_todas(cls) -> list[Pessoa]:
        if not os.path.exists(cls.FILE_PATH):
            return []
        with open(cls.FILE_PATH, 'r', encoding='utf-8') as file:
            return [cls._parse(line) for line in file if cls._valid_line(line)]

    @staticmethod
    def _next_id(pessoas: list[Pessoa]) -> int:
        return max((p.id for p in pessoas), default=PessoaRepository.DEFAULT_ID) + 1

    @classmethod
    def _valid_line(cls, line: str) -> bool:
        return len(line.strip().split(cls.SEPARATOR)) == cls.EXPECTED_FIELDS

    @classmethod
    def _parse(cls, line: str) -> Pessoa:
        dados = line.strip().split(cls.SEPARATOR)
        return PessoaBuilder() \
            .id(int(dados[0])) \
            .nome(dados[1]) \
            .cpf(dados[2]) \
            .skip_validate_() \
            .build()

    @staticmethod
    def _format(pessoa: Pessoa) -> str:
        return f"{pessoa.id},{pessoa.nome},{pessoa.cpf}"
