def cifra_metades_repetitiva(string):

    frase = ''.join(string.split())


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

#----------------------------------------------------------------------