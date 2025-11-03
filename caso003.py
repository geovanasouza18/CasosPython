import time
nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))

print(f'Cheguei ao beco escuro e identifiquei o suspeito. O nome dele(a) é {nome}')
time.sleep(2)
print(f'Observei o sujeito com atenção clínica: aparenta {idade} anos e mede aproximadamente {altura} m de altura. Cada detalhe do seu porte físico parecia esconder mais do que mostrava')
time.sleep(2)
if idade >= 18:
    print('Permitido investigar 🕵️‍♂️')
else:
    print('Proibido investigar 🚫')

time.sleep(1)
print('Caso encerrado....por enquanto.')