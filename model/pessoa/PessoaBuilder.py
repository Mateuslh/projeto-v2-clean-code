from common.AbstractBuilder import AbstractBuilder
from model.pessoa.Pessoa import Pessoa
from model.pessoa.PessoaSpecification import PessoaSpecification


class PessoaBuilder(AbstractBuilder):
    def _create_entity(self):
        return Pessoa()

    def identificador(self, identificador: int):
        self.entity._identificador = identificador
        return self

    def nome(self, nome: str):
        self.entity._nome = nome
        return self

    def cpf(self, cpf: str):
        self.entity._cpf = cpf
        return self

    def validate(self):
        PessoaSpecification.validar(self.entity)
