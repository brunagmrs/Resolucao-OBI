N = int(input('Digite um número de 1 a 500: '))
numant = 1

if N>=1 and N<=500:

    if N > 99:
        numcirculo1 = N % 100
        numcirculo2 = N - numcirculo1
    else:
        numcirculo1 = N % 10
        numcirculo2 = N - numcirculo1

    num = []
    print(f'Insira uma sequência de termos ({N} >= termo > 1)')
    for i in range (N):
        v =int(input(f'Digite o número {i} da sequência (entre 1 à {N}): '))

        if v > N or v < 0:
            print('Erro, o número digitado ultrapassa o intervalo descrito anteriormente')
            break
        else:
            num.append(v)

    if v > N or v < 0:
        print('Não foi possível calcular a quantidade de círculos.')
    else:
        ant = 0
        quantidadecirculos = 0

        for i in range(len(num)):

            if num[i] != ant and (numcirculo1 == num[i] or numcirculo2 == num[i]):
                quantidadecirculos += 1
                ant = int(num[i])

        print(f'A quantidade de círculos é: {quantidadecirculos}')
else:
    print('o número está fora do intervalo esperado')
