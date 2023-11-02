# estruturas de repeticao
# jogo da advinhacao

# importar modulos no inicio
import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# gerar e guardar o numero aleatorio
number = random.randint(1,10)

print("NUMERO ALEATORIO: ", number)

# variavel de controle
isGuessRight = False

# estrutura de repeticao com WHILE (ENQUANTO)
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    # estrutura condicional
    # verificar se o usuario digitou o numero correto
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
