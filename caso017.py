titulo1 = "\033[36m A Biblioteca de Conhecimento Sherlock \033[0m"
linha = "\033[35m=\033[0m" * 40

print(linha)
print(f'{titulo1:^50}')
print(linha)

acervo = list()
opcao = ''
while True:
    print('''
    [1] ADICIONAR LIVRO AO ACERVO
    [2] VER BIBLIOTECA 
    [3] LIVROS CONCLUÍDOS
    [4] CATEGORIA
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
                status = input('Digite o status do livro [ler, em andamento, lido]: ').strip().lower()

                if status == "":
                    print("Erro: o status não pode ser vazio 🚫📖")
                else:
                    registro = (titulo, categoria, status)
                    acervo.append(registro)
                    print("Livro registrado com sucesso ✅📚", registro)

    elif opcao == 2:
        for titulo, categoria, status in acervo:
            print(f'Título: {titulo}')
            print(f'Categoria: {categoria}')
            print(f'Status: {status}')
            print(linha)

    elif opcao == 3:
        total_lido = 0
        for titulo, categoria, status in acervo:
            if status == 'lido':
                total_lido += 1
            else:
                print('Você não concluiu nenhuma leitura ainda.')
        print(f'Livro(s) lido(s): {total_lido}')

    elif opcao == 4:

    # elif opcao == 5:
    #     break

print(f'Saindo do programa...')
print(linha)
