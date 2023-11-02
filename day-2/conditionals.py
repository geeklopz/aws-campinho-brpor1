# condicionais

# funcao INPUT, recebe valores digitados pelo usuario
userReply = input("Do you need to ship a package? (Enter yes or no) ")

print('USUARIO DIGITOU: ', userReply)


# estrutura condicional
if userReply == "yes":
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")   