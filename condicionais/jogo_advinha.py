# Jogo de Advinhação usando condicionais e importando a biblioteca random

from random import randint

#Apresentaçao do jogo

print('Bem vindo ao jogo de advinhação! Versão 1.0')
print()
nome = input('Digite seu nome:')
print()
print('Olá,{}! Vamos jogar?'.format(nome))
print()
print('Estou pesando em um número entre 1 e 10. Tente advinhar qual é!')
print()

#Gera o numero secreto e inicia o jogo com loop de 3 tentativas

numero_secreto = randint(1, 10)
print('Você tem 3 tentativas para acertar o numero secreto.')
tentativas = 3
while tentativas > 0:
    palpite = int(input('Digite seu palpite:'))
    print()
    if palpite == numero_secreto:
        print('Parabens,{}! Voce advinhou o número secreto!'.format(nome))
        break
        print()
    else:
        tentativas -= 1
        if tentativas > 0:
            print('Errado! Tente novamente. Voce tem {} tentativas restantes.'.format(tentativas))
            print()
        else:
            print('Que pena,{}! Voce esgotou suas tentativas. O numero secreto era {}.'.format(nome, numero_secreto))
            print()
            #fim do jogo!!!
            #Estou em fase de desenvolvimento, por isso o jogo termina aqui.

print('Obrigado por participar do jogo, {}!'.format(nome))
        
