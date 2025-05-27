from repository.PessoaRepository import PessoaRepository
from model.pessoa.PessoaBuilder import PessoaBuilder


class PessoaService:
    def buscar_por_cpf(self, cpf: str):
        return PessoaRepository.buscar_por_cpf(cpf)

    def criar(self, nome: str, cpf: str):
        pessoa = PessoaBuilder() \
            .nome(nome) \
            .cpf(cpf) \
            .build()
        PessoaRepository.salvar_ou_atualizar(pessoa)
        return pessoa
