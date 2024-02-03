print('Digite o número de termos da sequência ')
N = int(input('(O número deve ser maior ou igual a 1 e menor ou igual a 500000):\n'))
if N < 1 or N > 500000:
    print('Erro, N não atende as condições para continuar')
else:
    print('Digite um resultado esperado para a soma dos números:')
    K = int(input('O número deve ser maior ou igual a 0 e menor ou igual a 1000000:\n'))
    if K < 0 or K > 1000000:
        print('Erro, K não atende as condições para continuar')
    else:
        v = []
        cont = int(0)
        print('\nAdicione valores entre 0 e 100\n')
        for i in range(N):
            valor = (int(input(f'Digite um valor para adiciona-lo em {i}: ')))
            if valor > 100 or valor < 0:
                print('Erro, o número digitado ultrapassa os limites indicados.')
                break
            else:
                v.append(valor)

        if 100 >= valor >= 0:
            atual = int

            for i in range(N):
                atual = v[i]
                if atual == K:
                    cont += 1

                if i < N:
                    for j in range(i+1, N):
                        if v[j] + atual == K:
                            cont += 1
                        atual = atual + v[j]

            print(f'A soma é: {cont}')