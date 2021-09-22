#AULAS DE PYTHON

#FUNÇÃO

'''def título(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


#Programa Principal
título('Eu vou conseguir programar')'''

'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


#Programa Principal
soma(4, 5)
soma(5, 3)
soma(7, 8)'''

'''def contador(* núm):
    for valor in núm:
        print(f'{valor} ',end='')
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números.')
    print('FIM')


contador(6, 5, 7, 8)
contador(4, 7, 8)
contador(7, 5)'''

'''def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1


valores = [9, 9 , 5, 7, 2]
dobra(valores)
print(valores)'''

#EXERCÍCIO-Faça um programa que tenha um função chamada área, que receba as dimensões de um terreno retangular (largura e comprimento e mopstre a área do terreno

'''def calculo(b, h):
    r = b * h
    print(f'O valor de {b} X {h} é igual a {r}')


b = float(input('Digite o valor da base:'))
h = float(input('Digite o valor da altura'))'''

#Estudo de classes

'''class Carro:
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano

    def obterNome(self):
        return self.nome

    def obterAno(self):
        return self.ano

carro = Carro('camaro', 2010)
print(carro.obterNome())
print(carro.obterAno())'''

'''class ClassePai:
    var1 = 'classe pai'

class ClasseFilha(ClassePai):
    pass

objeto_pai = ClassePai()
objeto_filho = ClasseFilha()

print(objeto_pai.var1)
print(objeto_filho.var1)'''

#CÁLCULO DE PORCENTAGEM DO TECNICO

class Cliente:
    def __init__(self, nome, ano, idade, rg, cidade, email):
        self.nome = nome
        self.ano = ano
        self.idade = idade
        self.rg = rg
        self.cidade = cidade
        self.email = email

    def obterNome(self):
        return self.nome

    def obterAno(self):
        return self.ano

    def obterIdade(self):
        return self.idade

    def obterRG(self):
        return self.rg

    def obterCidade(self):
        return self.cidade

    def obterEmail(self):
        return self.email

cliente = Cliente('José', 2002, 16, 45784, 'Jeremoabo', 'jjose@hentmail.com')
print(cliente.obterNome())
print(cliente.obterAno())
print(cliente.obterIdade())
print(cliente.obterRG())
print(cliente.obterCidade())
print(cliente.obterEmail())



