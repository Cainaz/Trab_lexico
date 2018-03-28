linha = 1
byte = 'password'

p_reservadas = ['algoritmo','ate','cadeia','caracter','enquanto','entao',
'faca','fim','funcao','inicio','inteiro','para','passo','procedimento',
'real','ref','retorne','se','senao','variaveis']

delimitadores = [' ','\n','\t','\r']

sem_atr = ['.','(',')',';',',','-','+','*','/','%']

OP_RELACIONAL1 = ['<','=','>']

OP_INTER = ['<','>']

OP_RELACIONAL2 = ['=','>']

OP_LOGICO=['&','$','!']

letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

numeros = ['0','1','2','3','4','5','6','7','8','9']

ponto='.'

#declaração da classe atomo

class Atomo:
    lexema = ''
    linha = 0
    tipo = ''
    erro = False
    fim_de_arquivo= False
    
# class Numero(Atomo):
#     pass

# class Palavra_Reservada(Atomo):
#     pass

# class OP_RELACIONAL(Atomo):
#     pass

# class OP_LOGICO(Atomo):
#     pass

# class IDENTIFICADOR(Atomo):
#     pass

# class NUMERO_INTEIRO(Atomo):
#     pass

# class NUMERO_REAL(Atomo):
#     pass

# class FRASE(Atomo):
#     pass

# class COMENTARIO(Atomo):
#     pass

# class INICIAL(Atomo):
#     pass




