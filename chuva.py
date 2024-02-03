N = (int(input('Digite a quantidade (ímpar) entre 3 e 500 de linhas da parede: ')))
if N % 2 != 0 and N >= 3 and N <= 500:

    M = (int(input('Digite a quantidade entre 3 e 500 de colunas da parede: ')))

    P = []

    for i in range(N):
        pontos = []
        for j in range(M):
            pontos.append(".")
        P.append(pontos)

    posicao = int(input('Digite a posição do vazamento (M <= posicao < 1): '))

    if posicao > j:
        print('Não é possível continuar\nAs condições da posição não foram atendidas')

    else:

        P[0][posicao] = "o"
        for i in range(1, N, 2):
            for j in range(1, M - 1, 1):
                paredeprateleira = str(input(f'Digite (#) para prateleira ou (.) para parede em P[{i}][{j}]: '))
                P[i][j] = paredeprateleira

        print('\n')

        for i in range(N):
            linha = ''
            for j in range(M):
                linha += str(P[i][j]) + " "
            print(linha)

        print('\n')

        for i in range(N):
            for j in range(M):

                if P[i][j] == '.':

                    if P[i - 1][j] == 'o':
                        P[i][j] = 'o'
                        if i < (N - 1):
                            aux = j
                            while j >= 0:
                                j -= 1
                                if P[i + 1][j + 1] == '#':
                                    P[i][j] = 'o'
                                else:
                                    j = -1
                            j = aux

                    if i < (N - 1):
                        if P[i][j - 1] == 'o' and P[i + 1][j - 1] == '#':
                            P[i][j] = 'o'

                    if j < (M - 1):
                        if P[i][j + 1] == 'o' and P[i + 1][j + 1] == '#':
                            P[i][j] = 'o'
                            aux = j
                            while j >= 0:
                                j -= 1
                                if P[i + 1][j + 1] == '#':
                                    P[i][j] = 'o'
                                else:
                                    j = -1
                            j = aux

        for i in range(N):
            linha = ''
            for j in range(M):
                linha += str(P[i][j]) + " "
            print(linha)

else:
    print('Não é possível continuar. \nAs condições das linhas não foram atendidas')
