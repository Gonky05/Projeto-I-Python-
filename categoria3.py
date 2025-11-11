# Tabela traduzida
tabela = {
    "A": "11", "B": "12", "C": "13", "D": "14", "E": "15",
    "F": "16", "G": "17", "H": "18", "I": "19", "J": "10",
    "K": "91", "L": "92", "M": "93", "N": "94", "O": "95",
    "P": "96", "Q": "97", "R": "98", "S": "99", "T": "90",
    "U": "81", "V": "82", "W": "83", "X": "84", "Y": "85",
    "Z": "86", "0": "87", "1": "88", "2": "89", "3": "80",
    "4": "41", "5": "42", "6": "43", "7": "44", "8": "45",
    "9": "46"
}

def cifra_data_repetitiva(palavra):
    
    palavra_codificada = ""
    
    # Irá verificar letra a letra 
    for letra in palavra.upper():
        # Verificar se a letra está na tabela e adicionar o número correspondente à palavra codificada
        if letra in tabela:
            palavra_codificada += tabela[letra]
        else:
            # Se a letra não estiver no dicionário, adicionar um marcador de erro, por exemplo se tiver acento
            palavra_codificada += "!"
    return palavra_codificada

#---------------------------------------------------------------------------------------------------------------------------------

def cifra_data_recursiva(palavra):
    # Nesta condição analisamos se a palavra existe. Se a palavra for nula, ou seja não houver caracteres, retorna string vazia
    if len(palavra) == 0:
        return ""
    # Se a palavra tiver apenas uma letra, retorne a codificação dessa letra apenas
    elif len(palavra) == 1:
        return tabela.get(palavra.upper(), "!")
    # Caso contrário, codifique a primeira letra e chame a função recursivamente para o restante da palavra
    else:
        primeira_letra = palavra[0]
        resto_da_palavra = palavra[1:]
        # Codifique a primeira letra e adicione à codificação do restante da palavra
        codigo_letra = tabela.get(primeira_letra.upper(), "!")
        return codigo_letra + cifra_data_recursiva(resto_da_palavra)
    
#---------------------------------------------------------------------------------------------------------------------------------