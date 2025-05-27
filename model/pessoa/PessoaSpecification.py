import re
from model.pessoa.Pessoa import Pessoa

_CPF_PURO        = re.compile(r"^\d{11}$")
_CPF_FORMATADO   = re.compile(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$")
_NOME_VALIDO     = re.compile(r"^[A-Za-zÀ-ÖØ-öø-ÿ ]+$")


class PessoaSpecification:

    @staticmethod
    def validar(pessoa: Pessoa):
        PessoaSpecification._validar_identificador(pessoa)
        PessoaSpecification._validar_nome(pessoa)
        PessoaSpecification._validar_cpf(pessoa)

    @staticmethod
    def _validar_identificador(pessoa: Pessoa):
        # Identificador pode ser None até que o repositório persista a entidade
        if pessoa.identificador is not None and pessoa.identificador <= 0:
            raise ValueError("Identificador deve ser positivo.")

    @staticmethod
    def _validar_nome(pessoa: Pessoa):
        if not pessoa.nome or not _NOME_VALIDO.match(pessoa.nome):
            raise ValueError("Nome deve conter apenas letras e espaços.")

    @staticmethod
    def _validar_cpf(pessoa: Pessoa):
        if not pessoa.cpf or not (_CPF_PURO.match(pessoa.cpf)
                                  or _CPF_FORMATADO.match(pessoa.cpf)):
            raise ValueError("CPF deve ter 11 dígitos (com ou sem pontuação).")
