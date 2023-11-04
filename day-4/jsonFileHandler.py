""""
LER ARQUIVO JSON
MODULO PERSONALIZADO
"""

# importar o modulo JSON
import json

# funcao com TRATAMENTO DE EXCESSAO try/except
def readJsonFile(fileName):
    data = ""
    # estrutura com tratamento de excessao
    # tente executar a leitura do arquivo
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    # caso nao consiga
    # mostre a mensagem de erro de leitura
    except IOError:
        print("Could not read file")
    
    # retorna o conteudo do arquivo
    return data

# ler o arquivo
# file = readJsonFile('insulin.json')
# print('JSON: {}'.format(file))