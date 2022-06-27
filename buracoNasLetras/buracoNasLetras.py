from collections import defaultdict

text = input('Digite o texto que deseja contar os buracos:')
counter = 0
chars = defaultdict(int)

for char in text:
    chars[char] += 1

ba = chars['a']*1
bA = chars['A']*1
bb = chars['b']*1
bB = chars['B']*2
bd = chars['d']*1
bD = chars['D']*1
be = chars['e']*1
bg = chars['g']*1
bo = chars['o']*1
bO = chars['O']*1
bp = chars['p']*1
bP = chars['P']*1
bq = chars['q']*1
bQ = chars['Q']*1
bR = chars['R']*1

numtotalbur = ba+bA+bb+bB+bd+bD+be+bg+bo+bO+bp+bP+bq+bQ+bR

print('O número total de buracos no texto, considerando as letras maiusculas e minusculas e suas diferenças, é : ', numtotalbur)