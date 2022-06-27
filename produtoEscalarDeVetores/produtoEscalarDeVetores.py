rep = 'sim'
while rep == 'sim':
    N = int(input('Quantos numeros voce deseja em seus vetores? '))
    a: [float] = [0 for x in range(N)]
    b: [float] = [0 for x in range(N)]

    print()
    print('Digite os números para o primeiro vetor:')
    for i in range(0, N):
        a[i] = float(input(f"{i + 1}º número: "))

    print()
    print('Digite os números para o segundo vetor:')
    for i in range(0, N):
        b[i] = float(input(f'{i + 1}º número: '))

    pev = 0
    for i in range(0, N):
        mult = a[i] * b[i]
        pev = pev + mult
    print()
    print('O produto escalar dos vetores é: ', pev)
    print()
    rep = input("Digite 'Sim', se deseja realizar um novo calculo de produto escalar dos vetores: ")
    print('--------------------------------------------------------------------------------------')
