#criando estrutura de condição IF ELSE
idade=15
#se a idade for maior que o valor 18 entao imprime maior de idade
if idade >= 18:
    print('voce é maior de idade')   
#se a idade for menor que o valor 18 entao imprime menor de idade
else:
    print('voce é menor de idade')

#estrutura com ELIF
idade=60

if idade <= 12:
    print('voce é criança')
elif idade < 18:
    print('voce é adolecente')
elif idade < 60:
    print('voce é adulto')
else:
    print('voce é idoso')