
from socket import SOMAXCONN


print(">>>>>>>>>>>>>>>>>>>>>>")
print("Seja bem vindo ao jogo da calculadora")
print("Informe a operação desejada:" "\n1 para adição" "\n2 para subtração" "\n3 para divisão")

operacao = int(input("qual operação você deseja usar ?"))


if operacao == 1:
    numero_1 = int(input( "informe o primeiro numero ?"))
    numero_2 = int(input("informe o segundo numero ?"))
    resultado = (numero_1 + numero_2)
    print("o resultado da operação é:", (resultado))

elif operacao == 2:
        numero_1=int(input( "informe o primeiro numero ?"))
        numero_2=int(input("informe o segundo numero ?"))
        resultado = (numero_1 - numero_2)
        print("o resultado da operação é:", (resultado))

elif operacao == 3:
        numero_1=int(input( "informe o primeiro numero ?"))
        numero_2=int(input("informe o segundo numero ?"))
        resultado = (numero_1 / numero_2)
        print("o resultado da operação é:"/ {resultado})

elif operacao == 4:
        numero_1=int(input( "informe o primeiro numero ?"))
        numero_2=int(input("informe o segundo numero ?"))
        resultado = (numero_1 * numero_2)
        print("o resultado da operação é:" * (resultado))
print("fim de jogo ")


