from service.PessoaService import PessoaService
from model.pessoa.Pessoa import Pessoa


class PessoaCLI:
    def __init__(self, pessoa_service: PessoaService):
        self.pessoa_service = pessoa_service

    def buscar_ou_criar(self) -> Pessoa:
        cpf = input("CPF (11 dígitos, sem pontuação): ").strip()
        pessoa = self.pessoa_service.buscar_por_cpf(cpf)
        if pessoa is None:
            nome = input("Nome: ").strip()
            pessoa = self.pessoa_service.criar(nome, cpf)
            print(f"Pessoa criada: {pessoa}")
        return pessoa
