visto_na_cena_crime = input('Foi visto na cena do crime? ').lower()
lista_suspeito = input('Está na lista suspeito? ').lower()
if visto_na_cena_crime == 'sim' or lista_suspeito == 'sim':
    print('O suspeito despertou nossa atenção. A investigação prossegue com cautela.')
else:
    print('Nada a declarar. O suspeito não apresenta indícios suficientes para a investigação.')