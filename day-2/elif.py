# programa de papelaria

userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? \n (Enter stamps, envelope, or copy) ")

# print(f"USUARIO DIGITOU { str.upper(userReply) }")
# print(f"USUARIO DIGITOU { str.lower(userReply) }")

if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")