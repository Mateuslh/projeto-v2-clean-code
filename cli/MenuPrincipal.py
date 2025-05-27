from service.PessoaService import PessoaService
from service.ReservaService import ReservaService
from cli.PessoaCLI import PessoaCLI
from cli.ReservaCLI import ReservaCLI


class MenuPrincipal:
    OPCOES = {
        "1": "Cadastrar uma reserva",
        "2": "Entrada do cliente (Check in)",
        "3": "Saída do cliente (Check out)",
        "4": "Alterar reserva",
        "5": "Relatórios",
        "6": "Sair"
    }

    @classmethod
    def exibir_menu(cls):
        pessoa_service = PessoaService()
        reserva_service = ReservaService()
        pessoa_cli = PessoaCLI(pessoa_service)
        reserva_cli = ReservaCLI(reserva_service, pessoa_cli)

        while True:
            print("\nMENU PRINCIPAL")
            for chave, descricao in cls.OPCOES.items():
                print(f"{chave} - {descricao}")

            escolha = input("\nEscolha > ").strip()

            match escolha:
                case "1":
                    reserva_cli.cadastrar_reserva()
                case "2":
                    reserva_cli.check_in()
                case "3":
                    reserva_cli.check_out()
                case "4":
                    reserva_cli.alterar_reserva()
                case "5":
                    reserva_cli.relatorios()
                case "6":
                    cls.sair()
                case _:
                    print("Opção inválida.")

    @staticmethod
    def sair():
        exit()


if __name__ == "__main__":
    MenuPrincipal.exibir_menu()
