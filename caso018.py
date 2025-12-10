dados = list()
opcao = ''
while True:
    print('''
    1 - Cadastrar usuário
    2 - Listar usuários
    3 - Buscar usuário
    4 - Remover usuário
    5 - Sair
    ''')
    opcao = int(input('Digite uma dessas opções: '))

    if opcao == 1:
        nome = input("Digite o nome do usuário: ").strip()

        if nome == "":
            print("Erro: o nome não pode ser vazio 🚫👤")

        else:
            idade = input("Digite a idade do usuário: ").strip()

            if idade == "":
                print("Erro: a idade não pode ser vazia 🚫🎂")

            elif int(idade) <= 0:
                print("Erro: a idade deve ser maior que zero 🚫📉")

            else:
                idade = int(idade)
                email = input("Digite o email do usuário: ").strip().lower()

                if email == "":
                    print("Erro: o email não pode ser vazio 🚫📧")

                else:
                    email_existe = False

                    for usuario in dados:
                        if usuario[2] == email:
                            email_existe = True

                    if email_existe:
                        print("Erro: este email já está cadastrado 👀🚫")

                    else:
                        dados.append((nome, idade, email))
                        print("Usuário cadastrado com sucesso ✅🎉")

    if opcao == 2:

    # if opcao == 3:
    # if opcao == 4:
    # if opcao == 5: