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

aspa ='\"'

#declaração da classe atomo
class Atomo:
    lexema = ''
    linha = 0
    tipo = ''
    erro = False
    fim_de_arquivo= False
    

