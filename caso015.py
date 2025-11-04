import time
nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))

meses = idade * 12
time.sleep(2)
print(f'O nome do suspeito(a) é {nome}, tem {idade} anos e sua altura é de {altura} metros')
print(f'Sua idade em meses é {meses}')