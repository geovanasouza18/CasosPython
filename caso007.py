import time
alibi = int(input('Que horas chegou no cinema? '))
camera = 19
time.sleep(2)
if alibi == camera:
    print('O suspeito confirma seu álibi. Por ora, nada a declarar.')
else:
    print('Mentira descoberta! O alibi não se sustenta sob o olhar da câmera.')
