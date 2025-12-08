titulo = "\033[36m Diário de Treinamento Sherlock \033[0m"
linha = "\033[35m=\033[0m" * 40

print(linha)
print(f"{titulo:^50}")  # centralizado em 40 colunas
print(linha)

diario = []
opcao = 0
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
        topico = input('Digite o tema estudado: ').strip()

        if topico == "":
            print("Erro: o tópico não pode ser vazio 🚫")
        else:
            try:
                horas = int(input('Digite a quantidade de horas estudadas: '))
                if horas < 0:
                    print("Erro: horas não podem ser negativas ⏳🚫")
                else:
                    obs = input('Digite as observações da aula estudada: ')
                    registro = (topico, horas, obs)
                    diario.append(registro)
                    print("Registro salvo ✅", registro)
            except ValueError:
                print("Erro: horas inválidas ❌")
    if opcao == 2:
        for topico, horas, obs in diario:
            print(f"Tópico: {topico}")
            print(f"Horas estudadas: {horas}")
            print(f"Observações: {obs}")
            print("-" * 30)
    if opcao == 3:
        total = 0
        for topico, horas, obs in diario:
            total += horas
        print(f'Total das horas estudadas: {total}')
    if opcao == 4:
        diario2 = []
        for topico, horas, obs in diario:
            print(f'Tópicos estudados: {topico}')
        if topico not in diario2:


