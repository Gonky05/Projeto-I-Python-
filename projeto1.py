# Importámos as funções criadas no ficheiro cifras.py onde se encontram as definições de cada função importada

from cifras import cifra_carangejo_repetitiva                
from cifras import cifra_carangejo_recursiva

from cifras import cifra_metades_repetitiva
from cifras import cifra_metades_recursiva    
 
from cifras import cifra_data_repetitiva
from cifras import cifra_data_recursiva


while True:      
# Neste loop, verificamos que ele se repete enquanto o utilizador escolher continuar depois de escolher qual cifra deseja
    
    frase= str(input("Digite uma frase: "))
    print()

    print("|--------------------------MENU--------------------------|")
    print("|                                                        |")
    print("| 1- caranguejo (ler a frase em sentido inverso)         |")
    print("|                                                        |")   
    print("| 2- metades (dividir as letras de índice par das ímpar) |")
    print("|                                                        |")
    print("| 3- data (codificar a frase)                            |")
    print("|                                                        |")
    print("|--------------------ESCOLHA UMA CIFRA-------------------|")

    
    # O utilizador escolhe qual a cifra que deseja para que a sua frase seja codificada.
    escolha = str(input("\nEscolha uma opção (1/2/3): "))       
    
    
    continuar = ''

    match escolha:
        
        # De acordo com a cifra que o utilizador escolhe, uma das opções é escolhida e mostrada. Se não for 1, 2, ou 3, então é mosrtado Opção inválida
        
        case '1':
            resultado = cifra_carangejo_repetitiva(frase) or cifra_carangejo_recursiva(frase)
            print("\nResultado:", resultado)
        
        case '2':
            resultado = cifra_metades_repetitiva(frase) or cifra_metades_recursiva(frase)   
            print("\nResultado:", resultado)
        
        case '3':
            resultado = cifra_data_repetitiva(frase) or cifra_data_recursiva(frase)
            print("\nResultado:", resultado)
        
        case _:
            print("\nOpção inválida...")

    continuar = input("\nDeseja continuar? (s/n): ")
    print()
    
    if continuar.lower() != 's':
        break