import time
full_name = str(input('Digite seu nome completo: '))
first_name = str(input('Digite seu primeiro nome: '))
middle_name = str(input('Digite seu nome do meio (caso tenha): '))
last_name = str(input('Digite seu último nome: '))
nickname = str(input('Digite seu nickname: '))
occupation = str(input('Digite sua profissão: '))
origin = str(input('Digite sua nacionalidade: '))
marital_status = str(input('Digite seu estado civil: '))
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))

meses = idade * 12
time.sleep(2)
print('-' * 30)
print(f'Seu nome completo: {full_name}\n'
      f'Seu primeiro nome: {first_name}\n'
      f'Seu nome do meio: {middle_name}\n'
      f'Seu último nome: {last_name}\n'
      f'Seu nickname: {nickname}\n'
      f'Sua ocupação: {occupation}\n'
      f'Sua origem: {origin}\n'
      f'Seu estado civil: {marital_status}\n'
      f'Sua idade: {idade}\n'
      f'Sua idade em meses: {meses}\n'
      f'Sua altura: {altura}\n')
