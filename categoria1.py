def cifra_carangejo_recursiva(s):
    if len(s) == 0:
        return s
    else:
        return cifra_carangejo_recursiva(s[1:]) + s[0]

#---------------------------------------------------------------

def cifra_carangejo_repetitiva(string):
    reversed = ""
    for c in string:
        reversed = c + reversed
    return reversed

#---------------------------------------------------------------