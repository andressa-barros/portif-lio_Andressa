from aplicacao.servico import create_aluno, create_treino, create_instrutor, create_pagamento, update_aluno, update_treino, update_instrutor, update_pagamento, read_aluno, read_treinos, read_instrutor, read_pagamento, delete_aluno, delete_instrutor, delete_treino, delete_pagamento

tabela = ["Aluno", "Treino", "Instrutor", "Pagamento"]
operacao = ["Criar", "Ler", "Atualizar", "Delete"]
while True:
    print(f"TABELAS\n1-{tabela[0]}\n2-{tabela[1]}\n3-{tabela[2]}\n4-{tabela[3]}")
    n = int(input("Digite o número da tabela que deseja: "))
    if n < 1 or n > 4:
        print("Número de tabela inválido")
        n = int(input("Digite o número da tabela que desejada:"))
    else:
        if n == 1:
            print(f"1-{operacao[0]}\n2-{operacao[1]}\n3-{operacao[2]}\n4-{operacao[3]}")
            op = int(input("Escolha o modo de operação que deseja:"))
            if op < 1 or op > 4:
                print("Operação inválida")
                op = int(input("Escolha o modo de operação que deseja:"))

            if op == 1:
                print(f"1-{operacao[0]}")
                nome_aluno = input("Digite o nome do aluno: ")
                idade = int(input("Digite a sua idade "))
                cpf = int(input("Digite o CPF: "))
                create_aluno(nome_aluno, idade, cpf)

            elif op == 2:
                print(f"2-{operacao[1]}")
                read_aluno()
            elif op == 3:
                read_aluno()
                print(f"3-{operacao[2]}")
                cpf = int(input("Digite o cpf: "))
                nome_aluno = input("Digite o nome do aluno: ")
                idade = input("Digite a sua idade: ")
                id_aluno = int(input("Digite o ID do aluno: "))

                update_aluno(id_aluno, nome_aluno, idade, cpf)
            elif op == 4:
                print(f"4-{operacao[3]}")
                id_aluno = int(input("Digite o id do aluno: "))
                delete_aluno(id_aluno)
        elif n == 2:
            print(f"1-{operacao[0]}\n2-{operacao[1]}\n3-{operacao[2]}\n4-{operacao[3]}")
            op = int(input("Escolha o modo de operação que deseja:"))
            if op < 1 or op > 4:
                print("Operação inválida")
                op = int(input("Escolha o modo de operação que deseja:"))

            if op == 1:
                print(f"1-{operacao[0]}")
                situacao_saude = input("Descricão saúde do aluno:")
                objetivo_aluno = input("Objetivo do aluno:")

                create_treino(situacao_saude, objetivo_aluno)

            elif op == 2:
                print(f"2-{operacao[1]}")
                read_treinos()

            elif op == 3:
                read_treinos()
                print(f"3-{operacao[2]}")
                id_treino = int(input("Digite o id do treino: "))
                situacao_saude = input("Descrição saúde do aluno: ")
                objetivo_aluno = input("Objetivo do aluno:")

                update_treino(situacao_saude, objetivo_aluno, id_treino)
            elif op == 4:
                print(f"4-{operacao[3]}")
                id_treino = input("Digite o id do treino: ")
                delete_treino(id_treino)
        elif n == 3:
            print(f"1-{operacao[0]}\n2-{operacao[1]}\n3-{operacao[2]}\n4-{operacao[3]}")
            op = int(input("Escolha o modo de operação que deseja:"))
            if op < 1 or op > 4:
                print("Operação inválida")
                op = int(input("Escolha o modo de operação que deseja:"))
            else:
                if op == 1:
                    print(f"1-{operacao[0]}")
                    nome_instrutor = input("Digite o nome instrutor: ")
                    cpf = input("Digite o CPF: ")
                    cep = input("Digite o CEP: ")

                    novo_instrutor= create_instrutor(nome_instrutor, cpf, cep)
                    print(novo_instrutor)
                elif op == 2:
                    print(f"2-{operacao[1]}")
                    read_instrutor()
                elif op == 3:
                    read_instrutor()
                    print(f"3-{operacao[2]}")
                    id_instrutor = input("Digite o id do instrutor: ")
                    nome_instrutor = input("Digite o nome do instrutor: ")
                    cpf = input("Digite o CPF: ")
                    cep = input("Digite o CEP: ")
                    update_instrutor(id_instrutor, nome_instrutor, cpf, cep)
                elif op == 4:
                    print(f"4-{operacao[3]}")
                    id_instrutor = input("Digite o ID do instrutor: ")
                    delete_instrutor(id_instrutor)
        elif n == 4:
            print(f"1-{operacao[0]}\n2-{operacao[1]}\n3-{operacao[2]}\n4-{operacao[3]}")
            op = int(input("Escolha o modo de operação que deseja:"))
            if op < 1 or op > 4:
                print("Operação inválida")
                op = int(input("Escolha o modo de operação que deseja:"))
            else:
                if op == 1:
                    print(f"1-{operacao[0]}")
                    tipo_pagamento = input("Tipo de pagamento: ")
                    nome_aluno = input("Digite o nome do aluno ")

                    create_pagamento(nome_aluno, tipo_pagamento)
                elif op == 2:
                    print(f"2-{operacao[1]}")
                    read_pagamento()
                elif op == 3:
                    read_pagamento()
                    print(f"3-{operacao[2]}")
                    id_pagamento = input("Digite o id do pagamento: ")
                    tipo_pagamento = input("Tipo de pagamento: ")
                    nome_aluno = input("Digite o nome do aluno ")
                    update_pagamento(id_pagamento, tipo_pagamento, nome_aluno)

                elif op == 4:
                    print(f"4-{operacao[3]}")
                    id_pagamento = input("Digite o ID do pagamento: ")
                    delete_pagamento(id_pagamento)

