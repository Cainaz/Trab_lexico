from type import *
#variaveis

p_reservadas = ['algoritmo','ate','cadeia','caracter','enquanto','entao',
'faca','fim','funcao','inicio','inteiro','para','passo','procedimento',
'real','ref','retorne','se','senao','variaveis']

delimitadores = [' ',',','#','\n','\'\'']#,',','(',')']

def ver_palavra(word):
    for variavel in P_reservadas:
        if(variavel == word.lower()):
            return True
        else:
            pass

def ver_delimit(delim):
    for variavel in delimitadores:
        if(variavel == delim):
            return True
        else:
            pass

#maquina de estado e leitor de char by char

def leitor(arquivo):
    global linha
    #byte = arquivo.read(1)
    atomo = Atomo
    atomo = INICIAL
    atomo.lexema = ''
    atomo.linha = linha
    
    while (True):#byte != ""):
        #boolean = ver_delimit(byte)
        byte = arquivo.read(1)
        if(byte == '\n'): 
            linha = linha+1

        #maquina de estados**
        
        
        if(ver_delimit(byte) or byte == ''):
            if(atomo.lexema != ''):
                return atomo

        else:
            atomo.lexema = atomo.lexema + byte

        if(byte==""):
            break
        

    