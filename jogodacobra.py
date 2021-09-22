# SNAKE GAME

def jogar():
    print('Bem vindo ao Snake Game!')

    nlinhas = int(input('Digiteo números de linhas: '))
    ncolunas = int(input('Digite o número de colunas: '))
    x0 = int(input('Digite a posição x inicial: '))
    y0 = int(input('Digite a posição y inicial: '))
    x = x0 + 1
    y = y0
    borda = 2

    tabuleiro(nlinhas, ncolunas, x0, y0, x, y)
    mover_direita = False
    mover_esquerda = False
    mover_cima = False
    mover_baixo = False

    while x < (ncolunas + borda) and y < (nlinhas + borda):

        mover = int(input('Digite os números para mover a cobra: 1 para cima, 2 para baixo, 3 para esquerda ou 4 para a direita'))

        if (mover == 1):
            mover_direita = False
            mover_esquerda = False
            mover_cima = True
            mover_baixo = False

        if (mover == 2):
            mover_direita = False
            mover_esquerda = False
            mover_cima = False
            mover_baixo = True

        if (mover == 3):
            mover_direita = False
            mover_esquerda = True
            mover_cima = False
            mover_baixo = False

        if (mover == 4):
            mover_direita = True
            mover_esquerda = False
            mover_cima = False
            mover_baixo = False

        if mover_direita:
            x = x + 1

            tabuleiro(nlinhas, ncolunas, x0, y0, x, y)

        if mover_esquerda:
            x = x - 1
            if x0 == y or x0 == x:
                print('Fim de jogo!')
            else:
                tabuleiro(nlinhas, ncolunas, x0, y0, x, y)

            if mover_baixo:
                y = y + 1

                tabuleiro(nlinhas, ncolunas, x0, y0, x, y)

            if mover_cima:
                y = y - 1

                tabuleiro(nlinhas, ncolunas, x0, y0, x, y)

            if (x == ncolunas + borda - 1) or (y == nlinhas + borda - 1) or x == 1 or y == 1:
                print('Fim de jogo!')

def tabuleiro (nlinhas, ncolunas, x0, y0, x, y):
    borda = 2

    contador_y = 1
    contador_x = 1
    contador = 1

#Borda

    while contador_x < (ncolunas + borda):
        contador_x = contador_x + 1
        print('#', end='')

        if contador_x == (ncolunas + borda):
            print('#')

#tabuleiro

    contador_x = 1

    while contador_y <= (nlinhas + borda):
        contador_y = contador_y + 1
        contador_x = 1

        while contador_x <= (ncolunas + borda):
            contador_x = contador_x + 1

            if contador_x == 2:
                print('#', end='')
                contador_x = contador_x + 1

            if x0 == contador_x and x0 == contador_y:
                while x > contador_x:
                    print('x', end='')
                    contador_x = contador_x + 1

            if ( x == contador_x and (y) == contador_y):
                print('C', end='')
                contador_x = contador_x + 1

            print('.', end='')

            if contador_x == ncolunas + borda:
                print('#')
                contador_x = contador_x + 1

#Borda

    contador_x = 1

    while contador_x < (ncolunas + borda):
        contador_x = contador_x + 1
        print('#,', end='')

        if contador_x == (ncolunas + borda):
            print('#')

jogar()




