titulo = "\033[36m Diário de Treinamento Sherlock \033[0m"
linha = "\033[35m=\033[0m" * 40

print(linha)
print(f"{titulo:^50}")  # centralizado em 40 colunas
print(linha)

diario = []
topico = ()
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
        topico =