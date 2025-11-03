import time
anos_Servico = int(input('Quantos anos de serviço? '))
time.sleep(1)
if anos_Servico >= 18:
    print('Parabéns, veterano, você pode mexer no cofre. Agora tente não perder as chaves.')
else:
    print('Desculpe, jovem padawan, o cofre não aceita amadores. Volte quando tiver mais anos de serviço.')