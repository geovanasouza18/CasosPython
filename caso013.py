import time
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
time.sleep(1)

print("\033[33mBem-vindo ao Menu de Investigação\033[0m")
print("\033[36m 1- Somar pistas\033[0m")
print("\033[35m 2 - Subtrair evidências\033[0m")
print("\033[32m 3 - Multiplicar suspeitas\033[0m")
print("\033[31m 4 - Dividir depoimentos\033[0m")
opcao = input("Escolha a operação (1/2/3/4): ")

time.sleep(1)

if opcao == "1":
    print("Você escolheu somar pistas 🔍➕")
    soma = num1 + num2
    time.sleep(1)
    print(f'O resultado da soma foi {soma}')

elif opcao == "2":
    print("Você escolheu subtrair evidências 🧾➖")
    sub = num1 - num2
    time.sleep(1)
    print(f'O resultado da subtração foi {sub}')

elif opcao == "3":
    print("Você multiplicou suspeitas 🕵️‍♀️✖️")
    mult = num1 * num2
    time.sleep(1)
    print(f'O resultado da multiplicação foi {mult}')

elif opcao == "4":
    print("Você decidiu dividir depoimentos 🗣️➗")
    if num2 == 0:
        time.sleep(1)
        print("Dividir por zero? Isso é tão impossível quanto o criminoso voltar à cena do crime! 🚫")
    else:
        div = num1 / num2
        time.sleep(1)
        print(f'O resultado da divisão foi {div}')

else:
    print("Opção inválida! Isso cheira a sabotagem... ☠️")

