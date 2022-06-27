from collections import Counter

text = input('Digite o texto que deseja contar os buracos:')
counter = Counter(text)


numtotalbur = counter['a']+counter['A']+counter['b']+counter['B']*2+counter['d']+counter['D']+counter['e']+counter['g']+counter['o']+counter['O']+counter['p']+counter['q']+counter['Q']+counter['R']

print('O número total de buracos no texto, considerando as letras maiusculas e minusculas e suas diferenças, é : ', numtotalbur)