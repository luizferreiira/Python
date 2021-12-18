import forca
import main

print("********************************")
print("*******Escolha um jogo!*********")
print("********************************")

print("(1) Forca (2) Adivinhação")
escolher = int(input("Qual jogo? "))

if escolher == 1:
    print("Jogando forca")
    forca.jogar()
elif escolher == 2:
    print("Jogando Adivinhação")
    main.jogar()
