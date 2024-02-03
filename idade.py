M = int(input('Digite a idade de Dona Mônica (40 a 110 anos): '))

if M < 40 or M > 110:
    print('A idade de Dona Mônica está fora do intervalo esperado')
else:
    f1 = int(input('Digite a idade de um dos três filhos de Dona Mônica: '))
    f2 = int(input('Digite a idade de outro filho de Dona Mônica: '))
    if f1 < 0 or f2 < 0 or f1 == f2:
        print('A idade dos filhos é inválida')
    else:
        som = f1 + f2
        if som >= M:
            print('Não foi possível realizar o cálculo'
                  '\nA somatória da idade dos filhos de Mônica supera ou é igual à idade dela')
        else:
            f3 = M - som
            maisvelho = f1
            if f2 > maisvelho:
                maisvelho = f2
            if f3 > maisvelho:
                maisvelho = f3
            print(f'A idade do filho mais velho de Dona Mônica é {maisvelho}')