titulo = "\033[36m A Biblioteca de Conhecimento Sherlock \033[0m"
linha = "\033[35m=\033[0m" * 40

print(linha)
print(f'{titulo:^50}')
print(linha)

acervo = list()
opcao = ''
while True:
    print('''
    [1] REGISTRAR ESTUDO
    [2] VER DIÁRIO
    [3] TOTAL DE HORAS
    [4] TÓPICOS ESTUDADOS
    [5] SAIR
    ''')

    opcao = int(input('Digite uma dessas opções: '))

    if opcao == 1:
        titulo = input('Digite o título do livro: ').strip().lower()

        if titulo == "":
            print("Erro: o título não pode ser vazio 🚫📚")
        else:
            categoria = input('Digite a categoria do livro: ').strip().lower()

            if categoria == "":
                print("Erro: a categoria não pode ser vazia 🚫🏷️")
            else:
                status = input('Digite o status do livro: ').strip().lower()

                if status == "":
                    print("Erro: o status não pode ser vazio 🚫📖")
                else:
                    registro = (titulo, categoria, status)
                    acervo.append(registro)
                    print("Livro registrado com sucesso ✅📚", registro)

    elif opcao == 2:

    elif opcao == 3:

    elif opcao == 4:

    elif opcao == 5:
        break

print(f'Saindo do programa...')
print(linha)
