from ast import Str
from random import random


def jogar():
    print('*****************************************')
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*****************************************')

    arquivo = open ("texto_palavras.txt", "r")
    palavras= []

    for linha in arquivo:
        linha= linha.strip()
        palavras.append(linha )
    
    arquivo.close()

    numero= random.randrange (0,len(palavras ))
    palavra_secreta=palavras[numero]

    letras_acertadas=["_" for letra in palavra_secreta ]


    enforcou = False
    acertou = False
    erros=0

    print(letras_acertadas)
    while (not acertou and not enforcou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                 letras_acertadas [index] = letra
            index += 1
        else:
            erros +=1
            enforcou = erros == 6
            acertou= "_" not in letras_acertadas
            print (letras_acertadas)

    if(acertou ):
        print("você ganhou!")
    else:
        print("você perdeu!")
    print("Fim do jogo")

if(__name__ == '__main__'):
    jogar()
