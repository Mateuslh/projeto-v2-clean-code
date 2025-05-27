import os
from config.Caminhos import PASTA_BANCO_DADOS
from model.pessoa.Pessoa import Pessoa
from model.pessoa.PessoaBuilder import PessoaBuilder

_ARQUIVO = os.path.join(PASTA_BANCO_DADOS, "Pessoas.txt")
_SEPARADOR = ","
_CAMPOS_ESPERADOS = 3
_NOVA_LINHA = "\n"
_ENCODING = "utf-8"


class PessoaRepository:
    @classmethod
    def salvar_ou_atualizar(cls, pessoa: Pessoa):
        pessoas = cls.listar_todas()

        for i, existente in enumerate(pessoas):
            if existente.identificador == pessoa.identificador:
                pessoas[i] = pessoa
                break
        else:
            pessoa = (
                PessoaBuilder(pessoa)
                .identificador(cls._proximo_id(pessoas))
                .build()
            )
            pessoas.append(pessoa)

        with open(_ARQUIVO, "w", encoding=_ENCODING) as arquivo:
            arquivo.writelines(cls._formatar(p) + _NOVA_LINHA for p in pessoas)

    @classmethod
    def buscar_por_cpf(cls, cpf: str) -> Pessoa | None:
        return next((p for p in cls.listar_todas() if p.cpf == cpf), None)

    @classmethod
    def listar_todas(cls) -> list[Pessoa]:
        if not os.path.exists(_ARQUIVO):
            return []
        with open(_ARQUIVO, "r", encoding=_ENCODING) as arquivo:
            return [
                cls._parse(line) for line in arquivo
                if cls._linha_valida(line)
            ]

    @staticmethod
    def _proximo_id(pessoas: list[Pessoa]) -> int:
        return max((p.identificador for p in pessoas), default=0) + 1

    @staticmethod
    def _linha_valida(linha: str) -> bool:
        return len(linha.strip().split(_SEPARADOR)) == _CAMPOS_ESPERADOS

    @staticmethod
    def _parse(linha: str) -> Pessoa:
        identificador, nome, cpf = linha.strip().split(_SEPARADOR)
        return (
            PessoaBuilder()
            .identificador(int(identificador))
            .nome(nome)
            .cpf(cpf)
            .skip_validate_()
            .build()
        )

    @staticmethod
    def _formatar(pessoa: Pessoa) -> str:
        return f"{pessoa.identificador},{pessoa.nome},{pessoa.cpf}"
