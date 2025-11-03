import time
testemunha = float(input('Qual a altura do criminoso? '))
altura = 1.80
time.sleep(2)
if testemunha > altura:
    print('O suspeito confere com a descrição. Investigação continua…')
else:
    print('Não bate com a descrição da testemunha. Ele é liberado.')