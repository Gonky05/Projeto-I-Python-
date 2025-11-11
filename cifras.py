def cifra_carangejo_recursiva(s):
    if len(s) == 0: # Se a string não tiver caracteres, então retorna igual a mesma string.
        return s
    else:
        return cifra_carangejo_recursiva(s[1:]) + s[0] # Tendo caracteres, aqui inverte o sentido da frase, chamando a função novamente.


""" Funciona como desejado, porque o argumento da função após a primeira vez que é chamada são o segundo caracter até 
ao fim da string e depois é o primeiro caracter,  logo os caracteres iniciais ficam para o fim, e os finais ficam no início. """

#---------------------------------------------------------------

def cifra_carangejo_repetitiva(string):
    reversed = ""
    for c in string:
        reversed = c + reversed   # Inverte o sentido da frase utilizando um loop para, caracter a caracter inverter a frase.
    return reversed

#---------------------------------------------------------------

def cifra_metades_repetitiva(string):

    frase = ''.join(string.split())  # Tira os espaços existentes para conseguir codificar a frase de seguida.


    metade1 = frase[::2]  
    metade2 = frase[1::2]


    metade = ' '.join([metade1, metade2])

    return metade

#----------------------------------------------------------------------

def cifra_metades_recursiva(string, i, y):
    
    if i == 0:
        string = ''.join(string.split())

    if i >= len(string):
        print(' ', end='')
        i = 1
        if y == 1:
            return ''
        y = 1
        
    print(string[i], end='')
    
    return cifra_metades_recursiva(string, i + 2, y)

#---------------------------------------------------------------

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

#--------------------------------------------------------------

def cifra_data_repetitiva(palavra):
    
    palavra_codificada = ""
    
    # Irá verificar letra a letra 
    for letra in palavra.upper(): # Força a letra a ser maíuscula para encontrar na tabela.
        
        # Verificar se a letra está na tabela e adicionar o número correspondente à palavra codificada
        if letra in tabela:
            palavra_codificada += tabela[letra]
        else:
            # Se a letra não estiver no dicionário, adicionar um marcador de erro ( ! ), por exemplo se tiver acento
            palavra_codificada += "!"
    return palavra_codificada

#-------------------------------------------------------------------------------------------------------------------------------------

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
    
#-------------------------------------------------------------------------------------------------------------------------------------