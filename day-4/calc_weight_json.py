""""
CALCULAR O PESO DA INSULINA JSON
EX: LER DADOS DE UMA API, 
LER DADOS DE UM ARQUIVO JSON
"""

# importar o leitor de arquivo JSON personalizado
from jsonFileHandler import readJsonFile

data = readJsonFile('insulin.json')

print('JSON: {}'.format(data))

# verifica se os dados forams lidos
if data != "" :
    # acessar os dados na posicoes no arquivo JSON
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']

    # concatenacao das insulinas
    insulin = bInsulin + aInsulin

    # peso
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']

    # mostra os valores lidos
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))

    # Calculating the molecular weight of insulin  
    # Getting a list of the amino acid (AA) weights  
    # FUNCOES LAMBDA
    aaWeights = data['weights']
    # Count the number of each amino acids  
    aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})  
    # Multiply the count by the weights  
    molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
    ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())  
    print("The rough molecular weight of insulin: " +
    str(molecularWeightInsulin))
    print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))

else:
    print("Error. Exiting program")

