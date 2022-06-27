print('▀▄▀▄▀▄▀▄▀▄ Descubra o Assassino ▄▀▄▀▄▀▄▀▄▀')
print()
input('APERTE QUALQUER TECLA PARA INICIAR O JOGO')
print('═════════════════════════════════════════')
print('O empresário Bill G. Ates foi assassinado e \no corpo dele foi deixado na frente da delegacia \nde polícia. O detetive Lin Ust Orvalds foi escolhido \npara investigar este caso. Após uma série de investigações,\nele organizou uma lista com prováveis assassinos,os locais \ndo crime e quais armas poderiam ter sido utilizadas.')
print()
input('APERTE QUALQUER TECLA PARA CONTINUAR')
print('═════════════════════════════════════════')
print('SUSPEITOS:','1.Charles B. Abbage','2.Donald Duck Knuth','3.Ada L. Ovelace','4.Alan T. Uring','5.Ivar J. Acobson', '6.Ras Mus Ler Dorf', sep='\n')
print()
print('LOCAL:','1.Redmond','2.Palo Alto','3.San Francisco','4.Tokio','5.Restaurante no Fim do Universo', '6.São Paulo','7.Cupertino','8.Helsinki','9.Maida Vale', '10.Toronto', sep='\n')
print()
print('ARMA DO CRIME:','1.Peixeira','2.DynaTAC 8000X (o primeiro aparelho celular do mundo)','3.Trezoitão','4.Trebuchet','5.Maça', '6.Gládio', sep='\n')
print()
print('Uma testemunha foi encontrada, mas ela só consegue \nresponder se você fornecer uma teoria. Digite \no número referente a cada dica (Suspeitos, Local, Arma)' )
x = 0
tent = 0
while x == 0 :
    s = int(input('Suspeito: '))
    l = int(input('local: '))
    a = int(input('Arma do crime: '))
    tent = tent + 1

    if s == 2 and l == 4 and a == 5:
        print()
        print ('Parabéns! Você desvendou o caso!')
        print()
        print('A testemunha conseguiu identificar que, Donald Duck Knuth \nmatou Bill G.Ates em Tokyo, com uma maça.')
        print()
        print('Você finalizou o jogo em ',tent, ' tentativa(s)')
        x = 1
    elif s == 2 and l == 4 and a != 5:
        print('Você está indo bem, mas ainda não olhou a fundo! Bole outra teoria')
    elif s == 2 and l != 4 and a != 5:
        print('Assim fica um pouco difícil para a testemunha! Tente novamente!')
    elif s == 2 and l != 4 and a == 5:
        print('Você está bem, só está meio perdido! Tente novamente!')
    elif s != 2 and l != 4 and a != 5:
        print('Tem certeza que você está apto a bolar alguma teoria? É melhor prestar mais atenção e tentar outra vez!')
    elif s != 2 and l == 4 and a == 5:
        print('Você está indo bem, mas a teoria ainda está sem personalidade! Tenta de novo.')
    elif s != 2 and l == 4 and a != 5:
        print('Em geografiz você pode até ser bom, mas em investigação... Eu tentaria novamente!')
    elif s != 2 and l != 4 and a == 5:
        print('Observou bem o ferimento mas não observou o resto. Tente outra vez.')





