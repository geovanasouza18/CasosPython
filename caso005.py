tempo_Observado = int(input('Por quanto tempo observou o relógio? '))
volta_Completa = 7
print('Quantas voltas COMPLETAS ele deu? ')
resultado = tempo_Observado // volta_Completa
print(resultado)
print('Quantos minutos sobraram depois das voltas completas? ')
minutos_sobrando = tempo_Observado % volta_Completa
print(minutos_sobrando)
