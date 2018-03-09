from type import *
#variaveis

p_reservadas = ['algoritmo','ate','cadeia','caracter','enquanto','entao',
'faca','fim','funcao','inicio','inteiro','para','passo','procedimento',
'real','ref','retorne','se','senao','variaveis']

delimitadores = [' ',',','#','\n']#,',','(',')']

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

def leitor(arquivo):
    global linha
    byte = arquivo.read(1)
    atomo2 = Atomo
    atomo2 = Inicial
    atomo2.lexema = ''
    atomo2.linha = linha
    
    while (byte != ""):
        #boolean = ver_delimit(byte)
        if(byte == '\n'): 
            linha = linha+1

        if(ver_delimit(byte)):
            if(atomo2.lexema != ''):
                return atomo2

        else:
            atomo2.lexema = atomo2.lexema + byte
        #end of condition
        byte = arquivo.read(1)

    arquivo.close()
    