"""
CIFRA DE CESAR
CRIPTOGRAFIA ANTIGA
"""

# funcao para duplicar o alfabeto
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# funcao para solicitar a mensagem a ser encriptada
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

# numero de chave para encriptar
# numero de 1 a 25
def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount


"""
FUNCAO PARA ENCRIPTAR A MENSAGEM
"""
def encryptMessage(message, cipherKey, alphabet):
    # iniciando as variaveis
    encryptedMessage = ""
    uppercaseMessage = ""

    # convertendo a mensagem para letras maiusculas
    uppercaseMessage = message.upper()

    # loop para percorrer cada caractere
    for currentCharacter in uppercaseMessage:
        # percorre as letras do alfabeto
        # buscar posicao
        position = alphabet.find(currentCharacter)

        # gera uma nova posicao a partir da chave de cifra
        newPosition = position + int(cipherKey)

        # condicional
        # se a letra contem no alfabeto
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition] # B == 1, CHAVE == 5 => 5 + 1 = 6 => G
        else:
            encryptedMessage = encryptedMessage + currentCharacter

    return encryptedMessage


"""
FUNCAO PARA DECRIPTAR A MENSAGEM
"""
def decryptMessage(message, cipherKey, alphabet):
    # retornar a posicao original
    # -1 inverte a posicao (do final para o inicio)
    decryptKey = -1 * int(cipherKey)
    # retorna a mensagem decriptada
    return encryptMessage(message, decryptKey, alphabet)



""""
PROGRAMA PRINCIPAL
"""
def runCaesarCipherProgram():
    # definicao do alfabeto
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')

    # funcao com alfabeto duplicado
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')

    # recuperar a mensagem do usuario
    myMessage = getMessage()
    print(myMessage)

    # recuperar a chave de cifra
    myCipherKey = getCipherKey()
    print(myCipherKey)

    # encriptar a mensagem
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')

    # decriptar a mensagem
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')

# executar a funcao principal
runCaesarCipherProgram()

