antecedentes = input('Tem antecedentes criminais? ').strip().lower()

if not antecedentes == 'sim':
    print('Nada mancha o histórico deste indivíduo. Um cidadão tão limpo quanto luvas recém-lavadas.')
else:
    print('Há sombras no passado deste sujeito. Investigue antes que escape pelas rachaduras.')
