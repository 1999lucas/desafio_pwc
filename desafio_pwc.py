# DESAFIO DE CÓDIGO
# Pedimos gentilmente que você resolva o seguinte desafio de código como parte de nosso
# processo de seleção.
# Endereço
# Um provedor de endereços retorna endereços apenas com ruas concatenadas, nomes e números.
# Nosso próprio sistema, por outro lado, tem campos para nome da rua e o número da rua.
#
# Entrada: string de endereço
# Saída: string da rua e string do número da rua
#
# 1. Escreva um programa simples que processe a entrada e retorne na saída para o casos simples abaixo, por exempl-
#
# a. “Miritiba 339” -> {“Miritiba”, “339”}
# b. “Babaçu 500” -> { “Babaçu”, “500”}
# c. “Cambuí 804B” -> {“Cambuí”, “123B”}
#
# 2. Considere os casos mais complicados:
#
# a. “Rio Branco 23” -> {“Rio Branco”, “23”}
# b. “Quirino dos Santos 23 b” -> {“Quirino dos Santos”, ”23 b”}
#
# 3. BÔNUS: Considere endereços de outros países (casos complexos)
#
# a. “4, Rue de la République” -> {"Rue de la République", "4"}
# b. “100 Broadway Av” -> {"Broadway Av", "100"}
# c. “Calle Sagasta, 26” -> {“Calle Sagasta”, “26”}
# d. “Calle 44 No 1991” -> {“Calle 44”, “No 1991”}
#
# Sua tarefa:
# Escreva uma aplicação executável, na linguagem de programação de sua escolha, incluindo casos de teste e envie o código-fonte de volta para leticia.sbueno@pwc.com
# *BÔNUS: Subir o código em um repositório do GitHub.

import os

opcao = None

while opcao != 2:
    print('\n********************* SEPARADOR DE ENDEREÇOS *********************')
    print('''\n[1] INSERIR ENDEREÇO
[2] SAIR''')
    opcao = int(input('Digite uma opção: '))
    match opcao:
        case 1:
            endereco = str(input('\nDigite o endereço para separá-lo no formato [NOME DA RUA], [NUMERO]: '))

            def sep_end_numero(endereco):
                if ',' in endereco:
                    fim = [x.strip() for x in endereco.split(',')]
                    parte = fim[0].lower().split()[0]
                    if parte.isdigit() or parte == 'no':
                        return fim[::-1]
                    else:
                        return fim

                fim = ['','']
                primeiro_numero = None
                numero_manipulado = False
                manipulando_numero = False
                numero_potencial = ''


                for x in endereco.split():
                    if primeiro_numero is None:
                        if x.lower() == 'no' or x.isdigit():
                            primeiro_numero = True
                            fim[1] = x
                            numero_manipulado = x.isdigit()
                        else:
                            primeiro_numero = False
                            fim[0] = x
                        continue

                    if numero_manipulado:
                        fim[0] += ('' if fim[0] == '' else ' ') + x
                    elif x.lower() == 'no' or primeiro_numero:
                        if numero_potencial != '':
                            fim[0] += ('' if fim[0] == '' else ' ') + numero_potencial
                            numero_potencial = ''
                        manipulando_numero = True
                        fim[1] += ('' if fim[1] == '' else ' ') + x
                        numero_manipulado = x.isdigit()
                    elif x.isdigit():
                        if manipulando_numero == True:
                            fim[1] += ' ' + x
                            numero_potencial = ''
                            numero_manipulado = True
                        elif numero_potencial != '':
                            fim[0] += ('' if fim[0] == '' else ' ') + numero_potencial
                            numero_potencial = x
                        else:
                            numero_potencial = x
                    elif numero_potencial != '':
                        numero_potencial += ' ' + x
                    else:
                        fim[0] += ('' if fim[0] == '' else ' ') + x

                if numero_potencial != '':
                    fim[1] = numero_potencial
                return fim

            print(f'{sep_end_numero(endereco)}')

        case 2:
            print('*************************** ENCERRANDO ***************************')
            os.system('')