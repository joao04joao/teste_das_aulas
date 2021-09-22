'''Entrada de dados
numero1 = float(input('Digite o número 1: '))
numero2 = float(input('Digite o número 2: '))
numero3 = float(input('Digite o número 3: '))

#Processamento de dados
media = (numero1 + numero2 + numero3) / 3

#Saída de dados
print('A média de {0} + {1} + {2} dividido por 3 é {3}:'.format(numero1, numero2, numero3, media))

#Verificação númerica
numero = float(input('Digite um número'))
if numero >0:
    print('Número positivo!')
elif numero <0:
    print('Número negativo!')
else:
    print('Seu número é igual a zero.')
'''

'''Programa que verifica a permissão para voto eleitoral.
print('Ok, através desse processo saberemos se você esta apto para votar.')
nascimento = int(input('Em que ano você nasceu?:'))
ano = int(input('Informe o ano atual:'))

idade = ano - nascimento
print('Você tem {0} anos'.format(idade))
if (idade ==16) and (idade == 17):
    print('Apto! Mas voto não é obrigatorio.')
elif idade >18:
    print('Apto! Você é obrigado a votar.')
elif idade <16 and idade >0:
    print('Você ainda não esta apto para votar')
else:
    print('Informações incorretas, tente novamente!')
 '''
'''QUESTÃO 1

numero1 = float(input('Digite o número 1: '))
numero2 = float(input('Digite o número 2: '))
numero3 = float(input('Digite o número 3: '))

if numero1 > numero2 and numero1 > numero3:
    print('O maior número é:', numero1)
elif numero3 > numero2 and numero3 > numero1:
    print('O maior número é:', numero3)
else:
    print('O maior número é:',numero2)

#QUESTÃO 02

tempserv = int(input('Há quanto tempo você trabalha na empresa?:'))
salario = float(input('Informe o seu salário:'))
if tempserv >= 5:
   bonus = salario * 0.2
else:
    bonus = salario * 0.1
print('Seu bonus pelo tempo de {} anos é de {} R$'.format(tempserv,bonus))


#QUESTÃO 03

emprestimo = float(input('Informe o valor desejado:'))
parcela = int(input('Informe a quantidade de parcelas, até 24:'))
salario = float(input('informe o valor atual do seu salário:'))

valorDaParcela = emprestimo / parcelas
taxa = salario * 0.3

if valorDaParcela <= taxa:
    print('Emprestimo aprovado!')
else:
    print('Emprestimo negado!')

QUESTÃO 4
num = int(input('Digite um número:'))
if (num%2) == 0:
    print('O número é par! ')
else:
    print('O número é ímpar!')

#QUESTÃO 5

l1 = input('Qual o valor do lado A do triângulo:')
l2 = input('Qual o valor do lado B do triângulo:')
l3 = input('Qual o valor do lado C do triângulo:')
if l1 == l2 and l2 == l3 :
    print('O triângulo é equlatero')
else:
    if l1 == l2 or l1 == l3 :
        print('O triângulo é isoscele')
    else:
        print('O triângulo é escaleno')
#QUESTÃO 6
n1 = int(input('Informe um número:'))
n2 = int(input('Informe um número:'))
n3 = int(input('Informe um número:'))
if n1>n2>n3:
    print(n3,n2,n1)
elif n1>n3>n2:
    print(n2,n3,n1)
elif n2>n1>n3:
    print(n3,n1,n2)
elif n2>n3>n1:
    print(n1,n3,n2)
elif n3>n2>n1:
    print(n1,n2,n3)
elif n3>n1>n2:
    print(n2,n1,n3)

#QUSTÃO 07

prod1 = float(input('Informe o preço do produto A:'))
prod2 = float(input('Informe o preço do produto B:'))
prod3 = float(input('Informe o preço do produto c:'))

if prod1<prod2<prod3:
    print('Este valor: R${} é o menor preço entre os demais.'.format(prod1))
elif prod2<prod1<prod3:
     print('Este valor: R${} é o menor preço entre os demais.'.format(prod2))
else:
    print('Este valor: R${} é o menor preço entre os demais.'.format(prod2))'''

'''QUESTÃO 08

dia = int(input('Informe um número que represente o dia da semana [de 1 a 7]:'))

if dia == 1: print('Hoje é Domingo!')
elif dia == 2: print('Hoje é Segunda-Feira!')
elif dia == 3: print('Hoje é Terça-Feira!')
elif dia == 4: print('Hoje é Quarta-Feira!')
elif dia == 5: print('Hoje é Quinta-Feira!')
elif dia == 6: print('Hoje é Sexta-Feira!')
elif dia == 7: print('Hoje é Sábado!')
else:
    print('Erro! informe um caractere válido.')'''

'''#ESTRUTURA DE DECISÃO
contador = 10
while contador >= 1:
    print('O contador é:', contador)
    contador = contador - 1'''

'''''#Média e nome dos alunos.
contador = 1
while contador <=5:
 nome = input('Informe seu nome:')
 nota1 = float(input('Informe sua nota:'))
 nota2 = float(input('Informe sua nota:'))
 nota3 = float(input('Informe sua nota:'))
 media = (nota1 + nota2 + nota3) /3
 print('{}, sua média é:{}'.format(nome,media))
 contador = contador +1'''

'''#CPF RG E CIDADE
contador = 1
nome = input('Qual o seu nome?:')
while nome != 'EXIT':
 inf = int(input('Digite seu CPF: '))
 inf2 = int(input('Digite seu RG:'))
 inf3 = input('Informe sua cidade:')
 print('{0}, seu CPF é:{1}; seu RG{2} e sua cidade é:{3}'.format(nome,inf,inf2,inf3))
 nome = input('Qual o seu nome?:')'''

'''#SEPARANDO OS GÊNEROS

sexo = input('Qual o seu sexo?')
feminino = 0
masculino = 0

while sexo != 'x':
    if sexo == 'feminino':
        feminino = feminino + 1
    elif sexo == 'masculino':
        masculino = masculino + 1
    sexo = input('Qual o seu sexo?')
    else : print('Informe dados corretos.')
          
print('O número de pessoas do gênero feminino é:',feminino)
print('O número de pessoas do gênero masculino é:',masculino)'''

'''x = int(input('Digite o limite:'))
quantidade_de_pares = 0

for n in range(x):
    if n%2 == 0:
        quantidade_de_pares = quantidade_de_pares + 1
print('A quantidade de números par