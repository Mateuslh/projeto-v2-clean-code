'''
Projeto final de programação
Alunos: Luigi Milanez, Vinicius Milanez e Nicolas Kaminski

'''

import time as t  # Importando a biblioteca time 
from os import remove, rename  # Utilizado no CheckIn


def cadastroReserva():
    nomeTitular = input('Digite o nome do titular da reserva > ').title()  # Deixa as primeiras letras maiúsculas
    while nomeTitular.isalpha() == False:  # Somente o primeiro nome do titular
        print()
        print('Dado inválido. Insira novamente!')
        nomeTitular = input('Digite o nome do titular da reserva > ').title()
    else:
        nomeTitular = nomeTitular + ','
    
    cpf = input('Digite o CPF do titular da reserva (sem pontuação) > ')
    while (not cpf.isdigit()) or (len(cpf) != 11):
        print()
        print('Dado inválido!')
        cpf = input('Digite o CPF do titular (sem pontuação) > ')
    else:
        cpf = cpf[0:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9] + cpf[10] + ','
    
    qntPessoas = input('Digite a quantidade de pessoas dessa reserva > ')
    while (not qntPessoas.isdigit()) or (int(qntPessoas) < 1):
        print()
        print('Dado inválido')
        qntPessoas = input('Digite a quantidade de pessoas dessa reserva > ')
    else:
        qntPessoas = int(qntPessoas)

    diarias = input('Digite o número de diárias dessa reserva > ')
    while (not diarias.isdigit()) or (int(diarias) < 1):
        print()
        print('Dado inválido')
        diarias = input('Digite o número de diárias dessa reserva > ')
    else:
        diarias = int(diarias)
        
    print()
    opcoes = ('1', '2', '3')
    print('TIPOS DE QUARTOS')
    print('[1] - Standard -> R$100,00/pessoa p/diária')
    print('[2] - Deluxe -> R$200,00/pessoa p/diária')
    print('[3] - Premium -> R$300,00/pessoa p/diária')
    print()
    tipoQuarto = input('Digite o tipo de quarto para a reserva > ')
    print()
        
    while tipoQuarto not in opcoes:
            
        print()
            
        print('Dado inválido. Insira novamente!')
        tipoQuarto = input('Digite o tipo de quarto para a reserva > ')
    else:
        ...

    if tipoQuarto == opcoes[0]:
        tipoQuarto = 'S'
        valorReserva = (diarias * qntPessoas * 100)
    elif tipoQuarto == opcoes[1]:
        tipoQuarto = 'D'
        valorReserva = (diarias * qntPessoas * 200)
    elif tipoQuarto == opcoes[2]:
        tipoQuarto = 'P'
        valorReserva = (diarias * qntPessoas * 300)
    
    tipoQuarto = tipoQuarto + ','

    print()
    print(f'VALOR TOTAL DA RESERVA: R${valorReserva},00')

    id = ' ,'
    statusReserva = 'R' + ','
    qntPessoas = str(qntPessoas) + ','
    diarias = str(diarias) + ','
    valorReserva = str(valorReserva)

    try:
        arquivo = open('Reservas.txt', 'r')
        leitura = arquivo.readlines()
        arquivo.close()
        for dados in leitura:
            id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')

            lista = list()
            lista.append(id1)

            id1 = int(lista[0])
            id1 += 1  # Conversão 
            id1 = str(id1) + ','

            id = id1

    except:
        ...

    reserva = id + statusReserva + nomeTitular + cpf + qntPessoas + diarias + tipoQuarto + valorReserva

    arquivo = open('Reservas.txt', 'a')
    arquivo.writelines(f'{reserva}\n')
    arquivo.close()

    # LEITURA
    arquivo = open('Reservas.txt', 'r')
    leitura = arquivo.readlines()
    arquivo.close()
    for dados in leitura:  # Código para abertura do TXT
        id, statusReserva, nomeTitular, cpf, qntPessoas, diarias, tipoQuarto, valorReserva = dados.split(',')
        if id == ' ':
            id = str('1')
            id0 = id + ',' + statusReserva + ',' + nomeTitular + ',' + cpf + ',' + qntPessoas + ',' + diarias + ',' + tipoQuarto + ',' + valorReserva
            dados = id0  # Se eu tirar essa variável dará erro
            arquivo = open('Reservas.txt', 'w')
            leitura = arquivo.write(f'{dados}')
            arquivo.close()

    print()
    print('Cadastro realizado com sucesso!')
    t.sleep(1.5)
    print()


def cadastroCheckIn():
    try:
        arquivo = open('Reservas.txt', 'r')
        leitura = arquivo.readlines()
        arquivo.close()

        cpfReservado = input('Digite o CPF do titular da reserva (sem pontuação) > ')
        while (not cpfReservado.isdigit()) or (len(cpfReservado) != 11):
            print()
            print('Dado inválido!')
            cpfReservado = input('Digite o CPF do titular (sem pontuação) > ')
        else:
            cpfReservado = cpfReservado[0:3] + '.' + cpfReservado[3:6] + '.' + cpfReservado[6:9] + '-' + cpfReservado[9] + cpfReservado[10]
        print()
        arquivo = open('Reservas.txt', 'r')
        leitura = arquivo.readlines()
        arquivo.close()

        for dados in leitura:
            id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
            if cpfReservado == cpf1:
                if statusReserva1 == 'R':
                    arquivo = open('checkinR.txt', 'a')
                    arquivo.writelines(dados)
                    arquivo.close()
                else:
                    ...

        arquivo = open('checkinR.txt', 'r')
        leitura = arquivo.readlines()
        arquivo.close()

        for dados in leitura:
            id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
            if statusReserva1 == 'R':
                print(f' ID: {id1}\n',
                        f'Status: {statusReserva1}\n',
                        f'Titular: {nomeTitular1}\n',
                        f'CPF: {cpf1}\n',
                        f'NPessoas: {qntPessoas1}\n',
                        f'Diárias: {diarias1}\n',
                        f'TipoDeQuarto: {tipoQuarto1}\n',
                        f'Valor: {valorReserva1}'
                    )

            else:
                print()
                print('Não há reservas para realizar CheckIn!')
                t.sleep(2)
                print()
                break
        
        arquivo = open('checkinR.txt', 'r')
        leitura = arquivo.readlines()
        arquivo.close()

        entrada = input('Digite o ID para realizar o CheckIn > ')
        for dados in leitura:
            id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
            if id1 == entrada:
                arquivo = open('Reservas.txt', 'r')
                leitura = arquivo.readlines()
                arquivo.close()

                arquivo = open('Reservas2.txt', 'w')
                for dados in leitura:
                    id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
                    dados = id1 + ',' + statusReserva1 + ',' + nomeTitular1 + ',' + cpf1 + ',' + qntPessoas1 + ',' + diarias1 + ',' + tipoQuarto1 + ',' + valorReserva1
                    if id1 == entrada:
                        statusReserva1 = 'A'
                        dados = id1 + ',' + statusReserva1 + ',' + nomeTitular1 + ',' + cpf1 + ',' + qntPessoas1 + ',' + diarias1 + ',' + tipoQuarto1 + ',' + valorReserva1
                        leitura = arquivo.writelines(f'{dados}')  # Caso exista mais de 1 linha no txt
                    else:
                        leitura = arquivo.writelines(f'{dados}')  # Caso não exista mais de 1 linha no txt
                arquivo.close()
                break
            else:
                continue
        else:
            while entrada not in id1:
                print()
                print('Dado inválido')
                entrada = input('Digite o ID para realizar o CheckIn > ')
            else:
                for dados in leitura:
                    id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
                    if id1 == entrada:
                        arquivo = open('Reservas.txt', 'r')
                        leitura = arquivo.readlines()
                        arquivo.close()

                        arquivo = open('Reservas2.txt', 'w')
                        for dados in leitura:
                            id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
                            dados = id1 + ',' + statusReserva1 + ',' + nomeTitular1 + ',' + cpf1 + ',' + qntPessoas1 + ',' + diarias1 + ',' + tipoQuarto1 + ',' + valorReserva1
                            if id1 == entrada:
                                statusReserva1 = 'A'
                                dados = id1 + ',' + statusReserva1 + ',' + nomeTitular1 + ',' + cpf1 + ',' + qntPessoas1 + ',' + diarias1 + ',' + tipoQuarto1 + ',' + valorReserva1
                                leitura = arquivo.writelines(f'{dados}')  # Caso exista mais de 1 linha no txt
                            else:
                                leitura = arquivo.writelines(f'{dados}')  # Caso não exista mais de 1 linha no txt
                        arquivo.close()
                        break

        remove('checkinR.txt')
        remove('Reservas.txt')  # Deleta o arquivo antigo
        rename('Reservas2.txt', 'Reservas.txt')  # Renomeia o código do novo arquivo para poder reutilizar no código

        print()
        print('CheckIn realizado com sucesso!')
        t.sleep(1.5)
        print()

    except:
        print()
        print('Nada consta em nosso banco de dados!')
        t.sleep(2)
        print()


def saidaCheckOut():
    try:
        arquivo = open('Reservas.txt', 'r')
        leitura = arquivo.readlines()
        arquivo.close()

        cpfReservado = input('Digite o CPF do titular da reserva (sem pontuação) > ')
        while (not cpfReservado.isdigit()) or (len(cpfReservado) != 11):
            print()
            print('Dado inválido!')
            cpfReservado = input('Digite o CPF do titular (sem pontuação) > ')
        else:
            cpfReservado = cpfReservado[0:3] + '.' + cpfReservado[3:6] + '.' + cpfReservado[6:9] + '-' + cpfReservado[9] + cpfReservado[10]
        print()
        arquivo = open('Reservas.txt', 'r')
        leitura = arquivo.readlines()
        arquivo.close()

        for dados in leitura:
            id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
            if cpfReservado == cpf1:
                if statusReserva1 == 'A':
                    arquivo = open('checkoutA.txt', 'a')
                    arquivo.writelines(dados)
                    arquivo.close()
                else:
                    ...

        arquivo = open('checkoutA.txt', 'r')
        leitura = arquivo.readlines()
        arquivo.close()

        for dados in leitura:
            id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
            if statusReserva1 == 'A':
                print(f' ID: {id1}\n',
                        f'Status: {statusReserva1}\n',
                        f'Titular: {nomeTitular1}\n',
                        f'CPF: {cpf1}\n',
                        f'NPessoas: {qntPessoas1}\n',
                        f'Diárias: {diarias1}\n',
                        f'TipoDeQuarto: {tipoQuarto1}\n',
                        f'Valor: {valorReserva1}'
                    )

            else:
                print()
                print('Não há reservas para realizar CheckOut!')
                t.sleep(2)
                print()
                break
        
        arquivo = open('checkoutA.txt', 'r')
        leitura = arquivo.readlines()
        arquivo.close()

        saida = input('Digite o ID para realizar o CheckOut > ')
        for dados in leitura:
            id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
            if id1 == saida:
                arquivo = open('Reservas.txt', 'r')
                leitura = arquivo.readlines()
                arquivo.close()

                arquivo = open('Reservas2.txt', 'w')
                for dados in leitura:
                    id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
                    dados = id1 + ',' + statusReserva1 + ',' + nomeTitular1 + ',' + cpf1 + ',' + qntPessoas1 + ',' + diarias1 + ',' + tipoQuarto1 + ',' + valorReserva1
                    if id1 == saida:
                        statusReserva1 = 'F'
                        dados = id1 + ',' + statusReserva1 + ',' + nomeTitular1 + ',' + cpf1 + ',' + qntPessoas1 + ',' + diarias1 + ',' + tipoQuarto1 + ',' + valorReserva1
                        leitura = arquivo.writelines(f'{dados}')  # Caso exista mais de 1 linha no txt
                    else:
                        leitura = arquivo.writelines(f'{dados}')  # Caso não exista mais de 1 linha no txt
                arquivo.close()
                break
            else:
                continue
        else:
            while saida not in id1:
                print()
                print('Dado inválido')
                saida = input('Digite o ID para realizar o CheckOut > ')
            else:
                for dados in leitura:
                    id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
                    if id1 == saida:
                        arquivo = open('Reservas.txt', 'r')
                        leitura = arquivo.readlines()
                        arquivo.close()

                        arquivo = open('Reservas2.txt', 'w')
                        for dados in leitura:
                            id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
                            dados = id1 + ',' + statusReserva1 + ',' + nomeTitular1 + ',' + cpf1 + ',' + qntPessoas1 + ',' + diarias1 + ',' + tipoQuarto1 + ',' + valorReserva1
                            if id1 == saida:
                                statusReserva1 = 'F'
                                dados = id1 + ',' + statusReserva1 + ',' + nomeTitular1 + ',' + cpf1 + ',' + qntPessoas1 + ',' + diarias1 + ',' + tipoQuarto1 + ',' + valorReserva1
                                leitura = arquivo.writelines(f'{dados}')  # Caso exista mais de 1 linha no txt
                            else:
                                leitura = arquivo.writelines(f'{dados}')  # Caso não exista mais de 1 linha no txt
                        arquivo.close()
                        break

        remove('checkoutA.txt')
        remove('Reservas.txt')  # Deleta o arquivo antigo
        rename('Reservas2.txt', 'Reservas.txt')  # Renomeia o código do novo arquivo para poder reutilizar no código

        print()
        print('CheckOut realizado com sucesso!')
        t.sleep(1.5)
        print()

    except:
        print()
        print('Nada consta em nosso banco de dados!')
        t.sleep(2)
        print()


def alteracaoReserva():
    try:
        arquivo = open('Reservas.txt', 'r')
        leitura = arquivo.readlines()
        arquivo.close()

        cpfReservado = input('Digite o CPF do titular da reserva (sem pontuação) > ')
        while (not cpfReservado.isdigit()) or (len(cpfReservado) != 11):
            print()
            print('Dado inválido!')
            cpfReservado = input('Digite o CPF do titular (sem pontuação) > ')
        else:
            cpfReservado = cpfReservado[0:3] + '.' + cpfReservado[3:6] + '.' + cpfReservado[6:9] + '-' + cpfReservado[9] + cpfReservado[10]

        print()

        for dados in leitura:
            id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
            if cpfReservado == cpf1:
                if statusReserva1 == 'R':  # Mostra as reservas cadastradas com tal CPF
                    print(f' ID: {id1}\n',
                        f'Status: {statusReserva1}\n',
                        f'Titular: {nomeTitular1}\n',
                        f'CPF: {cpf1}\n',
                        f'NPessoas: {qntPessoas1}\n',
                        f'Diárias: {diarias1}\n',
                        f'TipoDeQuarto: {tipoQuarto1}\n',
                        f'Valor: {valorReserva1}'
                    )
            
        # print()

        opcao = ('S', 'N')
        alteracao = input('Digite o ID da reserva para alteração > ')
        # Realizar o cadastro da reserva
        cpfReservado += ','

        cancelamento = input('Deseja cancelar sua reserva? [s/n] > ').upper()
        while cancelamento not in opcao:
            print()
            print('Dado inválido. Insira novamente!')
            cancelamento = input('Deseja cancelar sua reserva? [s/n] > ').upper()   
        else:
            ...
        
        if cancelamento == opcao[0]:
            arquivo = open('Reservas2.txt', 'w')
            for dados in leitura:
                id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
                dados = id1 + ',' + statusReserva1 + ',' + nomeTitular1 + ',' + cpf1 + ',' + qntPessoas1 + ',' + diarias1 + ',' + tipoQuarto1 + ',' + valorReserva1
                if id1 == alteracao:
                    statusReserva1 = 'C'
                    dados = id1 + ',' + statusReserva1 + ',' + nomeTitular1 + ',' + cpf1 + ',' + qntPessoas1 + ',' + diarias1 + ',' + tipoQuarto1 + ',' + valorReserva1
                    leitura = arquivo.writelines(f'{dados}')  # Caso exista mais de 1 linha no txt
                else:
                    leitura = arquivo.writelines(f'{dados}')  # Caso não exista mais de 1 linha no txt
            arquivo.close()

            remove('Reservas.txt')  # Deleta o arquivo antigo
            rename('Reservas2.txt', 'Reservas.txt')  # Renomeia o código do novo arquivo para poder reutilizar no código
            
        elif cancelamento == opcao[1]:
            qntPessoasPergunta = input('Digite o número de pessoas desta reserva > ')
            while (not qntPessoasPergunta.isdigit()) or (int(qntPessoasPergunta) < 1):
                print()
                print('Dado inválido')
                qntPessoasPergunta = input('Digite a quantidade de pessoas dessa reserva > ')
            else:
                qntPessoasPergunta = int(qntPessoasPergunta)

            diariasPergunta = input('Digite o número de diárias dessa reserva > ')
            while (not diariasPergunta.isdigit()) or (int(diariasPergunta) < 1):
                print()
                print('Dado inválido')
                diariasPergunta = input('Digite o número de diárias dessa reserva > ')
            else:
                diariasPergunta = int(diariasPergunta)
            
            print()
            opcoes = ('1', '2', '3')
            print('TIPOS DE QUARTOS')
            print('[1] - Standard -> R$100,00/pessoa p/diária')
            print('[2] - Deluxe -> R$200,00/pessoa p/diária')
            print('[3] - Premium -> R$300,00/pessoa p/diária')
            print()
            tipoQuartoPergunta = input('Digite o tipo de quarto para a reserva > ')
            print()

            while tipoQuartoPergunta not in opcoes:

                print()

                print('Dado inválido. Insira novamente!')
                tipoQuartoPergunta = input('Digite o tipo de quarto para a reserva > ')
            else:
                ...

            if tipoQuartoPergunta == opcoes[0]:
                tipoQuartoPergunta = 'S'
                valorReservaPergunta = (diariasPergunta * qntPessoasPergunta * 100)
            elif tipoQuartoPergunta == opcoes[1]:
                tipoQuartoPergunta = 'D'
                valorReservaPergunta = (diariasPergunta * qntPessoasPergunta * 200)
            elif tipoQuartoPergunta == opcoes[2]:
                tipoQuartoPergunta = 'P'
                valorReservaPergunta = (diariasPergunta * qntPessoasPergunta * 300)

            tipoQuartoPergunta = tipoQuartoPergunta + ','

            print()
            print(f'VALOR TOTAL DA RESERVA: R${valorReservaPergunta},00')
        
            qntPessoasPergunta = str(qntPessoasPergunta) + ','
            diariasPergunta = str(diariasPergunta) + ','
            valorReservaPergunta = str(valorReservaPergunta)

            arquivo = open('Reservas2.txt', 'w')
            for dados in leitura:
                id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
                dados = id1 + ',' + statusReserva1 + ',' + nomeTitular1 + ',' + cpf1 + ',' + qntPessoas1 + ',' + diarias1 + ',' + tipoQuarto1 + ',' + valorReserva1
                if id1 == alteracao:
                    dados = alteracao + ',' + statusReserva1 + ',' + nomeTitular1 + ',' + cpf1 + ',' + qntPessoasPergunta + diariasPergunta + tipoQuartoPergunta + valorReservaPergunta
                    leitura = arquivo.writelines(f'{dados}\n')
                else:
                    leitura = arquivo.writelines(f'{dados}')
            arquivo.close()

            remove('Reservas.txt')  # Deleta o arquivo antigo
            rename('Reservas2.txt', 'Reservas.txt')  # Renomeia o código do novo arquivo para poder reutilizar no código

        print()
        print('Alteração realizada com sucesso!')
        print()

        t.sleep(1.5)

    except:
        print()
        print('Nada consta em nosso banco de dados!')
        t.sleep(2)
        print()


def mostrarRelatorios():
    opcoes = ('1', '2', '3', '4', '5', '6')
    print(' [1] - Relatório de todas as reservas com status R\n',
    '[2] - Relatório de todas as reservas com status C\n',
    '[3] - Relatório de todas as reservas com status A\n',
    '[4] - Relatório de todas as reservas com status F\n',
    '[5] - Relatório total recebido\n',  # Somar valor de todos os status F
    '[6] - Relatório de reserva por pessoa'
    )
    print()
    opcao = input('Digite a opção que deseja > ')
    print()
    while opcao not in opcoes:
        print('A opção digitada não existe, tente novamente!')
        opcao = input('Digite uma opção válida > ')
        print()
    else:
        ...
    if opcao == opcoes[0]:  # R
        try:
            try:  # Caso o arquivo não exista, ele irá executar a criação do arquivo
                arquivo = open('RelatorioR.txt', 'r')
                leitura = arquivo.readlines()
                arquivo.close()
            except:
                arquivo = open('Reservas.txt', 'r')
                leitura = arquivo.readlines()
                arquivo.close()
                for dados in leitura:
                    id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
                    if statusReserva1 == 'R':
                        arquivo = open('RelatorioR.txt', 'a')
                        arquivo.writelines(f'{dados}')
                        arquivo.close()
            arquivo = open('Reservas.txt', 'r')
            leitura = arquivo.readlines()
            arquivo.close()
            for dados in leitura:
                id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
                if statusReserva1 == 'R':
                    dados = id1 + ',' + statusReserva1 + ',' + nomeTitular1 + ',' + cpf1 + ',' + qntPessoas1 + ',' + diarias1 + ',' + tipoQuarto1 + ',' + valorReserva1
                    arquivo = open('RelatorioR2.txt', 'a')
                    arquivo.writelines(f'{dados}')
            arquivo.close()
            remove('RelatorioR.txt')  # Deleta o arquivo antigo
            rename('RelatorioR2.txt', 'RelatorioR.txt')  # Renomeia o código do novo arquivo para poder reutilizar no código
        
            print()
            print('Relatório gerado com sucesso!')
            t.sleep(1.5)
            print()
        
        except:
            print()
            print('Nada consta em nosso banco de dados!')
            t.sleep(2)
            print()

    elif opcao == opcoes[1]:  # C
        try:
            try:  # Caso o arquivo não exista, ele irá executar a criação do arquivo
                arquivo = open('RelatorioC.txt', 'r')
                leitura = arquivo.readlines()
                arquivo.close()
            except:
                arquivo = open('Reservas.txt', 'r')
                leitura = arquivo.readlines()
                arquivo.close()
                for dados in leitura:
                    id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
                    if statusReserva1 == 'C':
                        arquivo = open('RelatorioC.txt', 'a')
                        arquivo.writelines(f'{dados}')
                        arquivo.close()
            arquivo = open('Reservas.txt', 'r')
            leitura = arquivo.readlines()
            arquivo.close()
            for dados in leitura:
                id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
                if statusReserva1 == 'C':
                    dados = id1 + ',' + statusReserva1 + ',' + nomeTitular1 + ',' + cpf1 + ',' + qntPessoas1 + ',' + diarias1 + ',' + tipoQuarto1 + ',' + valorReserva1
                    arquivo = open('RelatorioC2.txt', 'a')
                    arquivo.writelines(f'{dados}')
            arquivo.close()
            remove('RelatorioC.txt')  # Deleta o arquivo antigo
            rename('RelatorioC2.txt', 'RelatorioC.txt')  # Renomeia o código do novo arquivo para poder reutilizar no código
        
            print()
            print('Relatório gerado com sucesso!')
            t.sleep(1.5)
            print()
        
        except:
            print()
            print('Nada consta em nosso banco de dados!')
            t.sleep(2)
            print()

    elif opcao == opcoes[2]:  # A
        try:
            try:  # Caso o arquivo não exista, ele irá executar a criação do arquivo
                arquivo = open('RelatorioA.txt', 'r')
                leitura = arquivo.readlines()
                arquivo.close()
            except:
                arquivo = open('Reservas.txt', 'r')
                leitura = arquivo.readlines()
                arquivo.close()
                for dados in leitura:
                    id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
                    if statusReserva1 == 'A':
                        arquivo = open('RelatorioA.txt', 'a')
                        arquivo.writelines(f'{dados}')
                        arquivo.close()
            arquivo = open('Reservas.txt', 'r')
            leitura = arquivo.readlines()
            arquivo.close()
            for dados in leitura:
                id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
                if statusReserva1 == 'A':
                    dados = id1 + ',' + statusReserva1 + ',' + nomeTitular1 + ',' + cpf1 + ',' + qntPessoas1 + ',' + diarias1 + ',' + tipoQuarto1 + ',' + valorReserva1
                    arquivo = open('RelatorioA2.txt', 'a')
                    arquivo.writelines(f'{dados}')
            arquivo.close()
            remove('RelatorioA.txt')  # Deleta o arquivo antigo
            rename('RelatorioA2.txt', 'RelatorioA.txt')  # Renomeia o código do novo arquivo para poder reutilizar no código
        
            print()
            print('Relatório gerado com sucesso!')
            t.sleep(1.5)
            print()
        
        except:
            print()
            print('Nada consta em nosso banco de dados!')
            t.sleep(2)
            print()

    elif opcao == opcoes[3]:  # F
        try:
            try:  # Caso o arquivo não exista, ele irá executar a criação do arquivo
                arquivo = open('RelatorioF.txt', 'r')
                leitura = arquivo.readlines()
                arquivo.close()
            except:
                arquivo = open('Reservas.txt', 'r')
                leitura = arquivo.readlines()
                arquivo.close()
                for dados in leitura:
                    id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
                    if statusReserva1 == 'F':
                        arquivo = open('RelatorioF.txt', 'a')
                        arquivo.writelines(f'{dados}')
                        arquivo.close()
            arquivo = open('Reservas.txt', 'r')
            leitura = arquivo.readlines()
            arquivo.close()
            for dados in leitura:
                id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
                if statusReserva1 == 'F':
                    dados = id1 + ',' + statusReserva1 + ',' + nomeTitular1 + ',' + cpf1 + ',' + qntPessoas1 + ',' + diarias1 + ',' + tipoQuarto1 + ',' + valorReserva1
                    arquivo = open('RelatorioF2.txt', 'a')
                    arquivo.writelines(f'{dados}')
            arquivo.close()
            remove('RelatorioF.txt')  # Deleta o arquivo antigo
            rename('RelatorioF2.txt', 'RelatorioF.txt')  # Renomeia o código do novo arquivo para poder reutilizar no código
        
            print()
            print('Relatório gerado com sucesso!')
            t.sleep(1.5)
            print()

        except:
            print()
            print('Nada consta em nosso banco de dados!')
            t.sleep(2)
            print()

    elif opcao == opcoes[4]:  # Somar os valores de F
        try:
            try:  # Caso o arquivo não exista, ele irá executar a criação do arquivo
                arquivo = open('RelatorioPagamento.txt', 'r')
                leitura = arquivo.readlines()
                arquivo.close()
            except:
                arquivo = open('Reservas.txt', 'r')
                leitura = arquivo.readlines()
                arquivo.close()
                for dados in leitura:
                    id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
                    if statusReserva1 == 'F':
                        arquivo = open('RelatorioPagamento.txt', 'a')
                        arquivo.writelines(valorReserva1)
                        arquivo.close()
            
            arquivo = open('Reservas.txt', 'r')
            leitura = arquivo.readlines()
            arquivo.close()
            for dados in leitura:
                id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
                if statusReserva1 == 'F':
                    arquivo = open('RelatorioPagamento2.txt', 'a')
                    arquivo.writelines(valorReserva1)
                    arquivo.close()
            arquivo = open('RelatorioPagamento2.txt', 'r')
            leitura = arquivo.readlines()
            arquivo.close()
            valorCheio = 0
            for dinheiro in leitura:
                valorCheio = int(dinheiro) + valorCheio

            arquivo = open('RelatorioPagamento.txt', 'w')
            arquivo.writelines(f'Valor total recebido: {valorCheio}')
            arquivo.close()
            remove('RelatorioPagamento2.txt')  # Deleta o arquivo antigo
        
            print()
            print('Relatório gerado com sucesso!')
            t.sleep(1.5)
            print()

        except:
            print()
            print('Nada consta em nosso banco de dados!')
            t.sleep(2)
            print()
    
    elif opcao == opcoes[5]:  # Todas as reservas de tal CPF
        try:
            cpfReservado = input('Digite o CPF do titular (sem pontuação) > ')
            while (not cpfReservado.isdigit()) or (len(cpfReservado) != 11):
                print()
                print('Dado inválido!')
                cpfReservado = input('Digite o CPF do titular (sem pontuação) > ')   
            else:
                cpfAlterado = cpfReservado
                cpfReservado = cpfReservado[0:3] + '.' + cpfReservado[3:6] + '.' + cpfReservado[6:9] + '-' + cpfReservado[9] + cpfReservado[10]
            
            txtNome = cpfAlterado + '.txt'
            txtNome2 = cpfAlterado + '2.txt'  
            
            print()
            try:
                arquivo = open(txtNome, 'r')
                leitura = arquivo.readlines()
                arquivo.close()
            except:
                arquivo = open('Reservas.txt', 'r')
                leitura = arquivo.readlines()
                arquivo.close()
                for dados in leitura:
                    id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
                    if cpf1 == cpfReservado:
                        arquivo = open(txtNome, 'a')
                        arquivo.writelines(f'{dados}')
                        arquivo.close()
            arquivo = open('Reservas.txt', 'r')
            leitura = arquivo.readlines()
            arquivo.close()
            for dados in leitura:
                id1, statusReserva1, nomeTitular1, cpf1, qntPessoas1, diarias1, tipoQuarto1, valorReserva1 = dados.split(',')
                if cpf1 == cpfReservado:
                    dados = id1 + ',' + statusReserva1 + ',' + nomeTitular1 + ',' + cpf1 + ',' + qntPessoas1 + ',' + diarias1 + ',' + tipoQuarto1 + ',' + valorReserva1
                    arquivo = open(txtNome2, 'a')
                    arquivo.writelines(f'{dados}')
            arquivo.close()
            remove(txtNome)  # Deleta o arquivo antigo
            rename(txtNome2, txtNome)  # Renomeia o código do novo arquivo para poder reutilizar no código
        
            print()
            print('Relatório gerado com sucesso!')
            t.sleep(1.5)
            print()

        except:
            print()
            print('Nada consta em nosso banco de dados!')
            t.sleep(2)
            print()


def saidaDoPrograma():
    print('Saindo...')
    t.sleep(1.7)  # Descanso de 1.7 segundo
    exit()


while True:
    print()  # Saída limpa de código
    print('MENU PRINCIPAL')
    opcoes = ('1', '2', '3', '4', '5', '6')

    print('1 - Cadastrar uma reserva.\n'
    '2 - Entrada do cliente (Check in).\n'
    '3 - Saída do cliente (Check out).\n'
    '4 - Alterar reserva.\n'
    '5 - Relatórios.\n'
    '6 - Sair.\n')

    opcao = input('Digite a opção que deseja > ')

    print()  # Saída limpa de código

    while opcao not in opcoes:
        print('A opção digitada não existe, tente novamente!')
        opcao = input('Digite uma opção válida > ')
        print()
    else:
        ...

    if opcao == opcoes[0]:  # Cadastrar uma reserva
        cadastroReserva()

    elif opcao == opcoes[1]:  # Entrada do cliente (Check in)
        cadastroCheckIn()

    elif opcao == opcoes[2]:  # Saída do cliente (Check out)
        saidaCheckOut()

    elif opcao == opcoes[3]:  # Alterar reserva
        alteracaoReserva()

    elif opcao == opcoes[4]:  # Relatórios
        mostrarRelatorios()

    elif opcao == opcoes[5]:  # Sair
        saidaDoPrograma()
