import time
idade = int(input('Digite sua idade: '))
nivel = int(input('Digite seu nível de acesso? '))
time.sleep(1)
if idade > 21 and nivel > 5:
    print('Após avaliar os registros, confirmo: o agente atende a todos os critérios. O acesso ao laboratório secreto é concedido.')
else:
    print('O acesso é negado. Apenas aqueles que cumprem todos os requisitos podem adentrar o santuário de segredos.')