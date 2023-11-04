# armazenar a sequencia de insulina
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

lsInsulin = preproInsulin[0:24]
bInsulin = preproInsulin[25:54]
cInsulin = preproInsulin[55:89]
aInsulin = preproInsulin[90:110]

# print(cInsulin)

# concatenacao de variavei
insulin = bInsulin + aInsulin

print(insulin)

print("The sequence of human preproinsulin:")
print(preproInsulin)

print("The sequence of human insulin, chain a: " + aInsulin)


""""
REFERENCIAS DE CALCULOS DE AMINOACIDOS
"""
# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19} 


# Count the number of each amino acids  
# FUNCAO LAMBDA
# funcao de linha unica
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})  


# Multiply the count by the weights
# funcao LAMBDA  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  


print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))

# peso atutal da insulina
molecularWeightInsulinActual = 5807.63

# erro de percetagem %
print("Error percentage: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))


# dicionario
pKR = {'y':10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}

# contagem de aminoacidos
# funcao LAMBDA
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})

# variavel de controle
pH = 0

# estrutura de repeticao com WHILE
while (pH <= 14):
    # executar bloco de codigo
    netCharge = (
    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values())))

    # incrementar a variavel de controle
    pH += 1

    # mostrar os valores
    # .2f eh as casas decimais
    print('{0:.2f}'.format(pH), netCharge)
