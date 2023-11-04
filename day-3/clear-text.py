"""
LIMPAR DADOS DE ARQUIVO COM PYTHON
"""

# importar
import re #regex
import os #sistema operacional

# ler o arquivo
with open('preproinsulin-seq.txt') as file:
    insulinFile = file.read()

# exibir os dados do arquivo
print("----- DADO ORIGINAL -----")
print(insulinFile)


# funcao para limpar os dados
# def
def clean_text(string):
    # removeList = ["ORIGIN", "61", "1",]
    # for item in removeList:
    #     string = string.replace(item, "")

    # remover os numeros
    string = re.sub(r"\d+", "", string)

    # remover ORIGIN
    string = string.replace("ORIGIN", "")
    # remover o 61
    # string = string.replace("61", "")
    # remover o 1
    # string = string.replace("1", "")
    # remover o //
    string = string.replace("//", "")
    # remover os espacos em branco
    string = re.sub(r"\s", "", string)
    # string = string.replace(" ", "")
    # remover quebra de linha
    string = string.replace("\n", "")

    return string

# dado limpo
cleanInsulin = clean_text(insulinFile)

# exibir os dados do arquivo
print("----- DADO LIMPO -----")
print(cleanInsulin)

# contagem de caracteres
# funcao len() retornar a quantidade de caracteres da string
print("----- CONTAGEM DE CARACTERES -----")
print("Quantidade de caracteres: {}".format(len(cleanInsulin)))



"""
CLASSIFICANDO OS DADOS
"""

# LS
print(f"EXEMPLO LS: {cleanInsulin[0:24]}")

# atribuir valores nas variaveis
lsInsulin = cleanInsulin[0:24]
bInsulin = cleanInsulin[25:54]
cInsulin = cleanInsulin[55:89]
aInsulin = cleanInsulin[90:110]


# contagem
print(f"Contagem LS: { len(lsInsulin) }")

# criar os arquivos
names = ["lsInsulin", "bInsulin", "cInsulin", "aInsulin"]

# estrutura de repeticao
# for

for insulin in names:
    fw = open(str(insulin).upper() + "-seq-clean.txt", "w")
    fw.write(globals()[insulin])
    fw.close()