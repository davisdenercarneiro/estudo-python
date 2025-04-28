#
n1 = int (input('insira o primeiro numero entre 0 e 10: '))
n2 = int(input('insira o segundo numero maior que 10: '))
n3=int(input('insira o terceiro numero positivo: '))
#operador AND
if n1 >= 0 and n1 <= 10:
    print ('seu primeiro numero é positivo e menor que 11')
elif n1 < 0:
    print ('seu primeiro numero é negativo')
else:
    print('seu primeiro numero maior que 10')
#operador OR
if n2>10 or n1>0:
    print('seu segundo numero é maior que 10')
else:
    print('insira o segundo numero maior que 10')
#operador NOT
condic = n3 < 0
if not condic:
    print('seu terceiro numero é maior que zero')
else:
    print ('digitar o terceiro numero maior que zero')