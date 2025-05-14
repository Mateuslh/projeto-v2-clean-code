from model.pessoa.Pessoa import Pessoa


class PessoaSpecification:

    @staticmethod
    def validar(pessoa: Pessoa):
        PessoaSpecification.validar_nome(pessoa)
        PessoaSpecification.validar_cpf(pessoa)

    @staticmethod
    def validar_nome(pessoa: Pessoa):
        if not pessoa.nome or not pessoa.nome.isalpha():
            raise ValueError("O nome da pessoa deve conter apenas letras e não pode ser vazio.")

    @staticmethod
    def validar_cpf(pessoa: Pessoa):
        if not pessoa.cpf.isdigit() or len(pessoa.cpf) != 11:
            raise ValueError("O CPF deve conter exatamente 11 dígitos numéricos.")
