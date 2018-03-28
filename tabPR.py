from type import *

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

def ver_numero(num):
    for variavel in numeros:
        if(variavel == num):
            return True
        else:
            pass

def is_char(letra):
    for variavel in letras:
        if(variavel == letra.lower()):
            return True
        else:
            pass

def ver_linha(byte):
    global linha
    if(byte == '\n'):
        linha += 1

#maquina de estado e leitor de char by char
# def maquina_estados(byte, atomo):


#     else:
#         atomo.tipo = 'NUMERO_INTEIRO'
#         return atomo

def leitor(arquivo):
    global linha, byte
    atomo = Atomo
    atomo.linha = linha
    atomo.lexema = ''
    
    while (True):
        if(ver_delimit(byte) or byte == 'password'):
            byte = arquivo.read(1)
            ver_linha(byte)
            atomo.linha = linha
        else:
            #condição de identificador
            if(is_char(byte)):
                atomo.lexema = atomo.lexema + byte
                while(not ver_delimit(byte)):
                    if(byte == ''):
                        break

                    byte = arquivo.read(1)
                    ver_linha(byte)

                    if(is_char(byte) or ver_numero(byte)):
                        atomo.lexema = atomo.lexema + byte

                    else:
                        break
                if(atomo.lexema.lower() in p_reservadas):
                    atomo.tipo = 'P_RESERVADA'
                    atomo.lexema = atomo.lexema.upper()
                    return atomo

                elif((ver_delimit(byte) or byte == '') is True):
                    atomo.tipo = 'IDENTIFICADOR'
                    return atomo
            
                else:
                #atomo.estado = 'erro'
                    atomo.tipo = 'IDENTIFICADOR'
                    return atomo

            #condição de numero
            if(ver_numero(byte)):
                atomo.lexema = atomo.lexema + byte
                while(not ver_delimit(byte)):
                    if(byte == ''):
                        break

                    byte = arquivo.read(1)
                    ver_linha(byte)

                    if(ver_numero(byte)):
                        atomo.lexema = atomo.lexema + byte
                    
                    elif(byte.lower() == 'e'):
                        atomo.lexema = atomo.lexema + byte
                        byte = arquivo.read(1)

                        if((byte == '+' or byte =='-')is True):
                            atomo.lexema = atomo.lexema + byte
                            while(not ver_delimit(byte)):
                                if(byte == ''):
                                    break

                                byte = arquivo.read(1)
                                ver_linha(byte)

                                if(ver_numero(byte)):
                                    atomo.lexema = atomo.lexema + byte
                            
                                elif((is_char(byte) or byte =='.')is True):
                                    atomo.lexema = atomo.lexema + byte
                                    atomo.erro = True
                                    return atomo
                            
                                else:
                                    break

                            if((ver_delimit(byte) or byte == '') is True):
                                atomo.tipo = 'OP_EXPONENCIAL'
                                return atomo
                            
                              
                                atomo.tipo = 'IDENTIFICADOR'
                                return atomo

                        else:
                            atomo.lexema = atomo.lexema + byte
                            atomo.erro = True
                            return atomo

                    #condição NUMERO REAL
                    elif(byte == ponto):
                        atomo.lexema = atomo.lexema + byte
                        while(not ver_delimit(byte)):
                            if(byte == ''):
                                break

                            byte = arquivo.read(1)
                            ver_linha(byte)

                            if(ver_numero(byte)):
                                atomo.lexema = atomo.lexema + byte
                            
                            elif((is_char(byte) or byte == ponto)is True):
                                atomo.lexema = atomo.lexema + byte
                                atomo.erro = True
                                return atomo
                            
                            else:
                                break

                        if((ver_delimit(byte) or byte == '') is True):
                            atomo.tipo = 'NUMERO_REAL'
                            return atomo

                        
                
                    else:
                        break
                
                if((ver_delimit(byte) or byte == '') is True):
                    atomo.tipo = 'NUMERO_INTEIRO'
                    return atomo

                elif(is_char(byte)):
                    atomo.lexema = atomo.lexema + byte
                    atomo.erro = True
                    return atomo

                else:
                    atomo.tipo = 'NUMERO_INTEIRO'
                    return atomo

            if(byte in OP_LOGICO):
                atomo.lexema = byte
                atomo.tipo = 'OP_LOGICO'
                byte = arquivo.read(1)
                ver_linha(byte)
                return atomo

            if(byte in OP_RELACIONAL1):
                atomo.lexema = byte
                if(byte in OP_INTER):
                    byte = arquivo.read(1)
                    ver_linha(byte)
                    if(byte in OP_RELACIONAL2):
                        atomo.lexema = atomo.lexema + byte
                        atomo.tipo = 'OP_RELACIONAL'
                        byte = arquivo.read(1)
                        ver_linha(byte)
                        return atomo

                    elif(byte == '-'):
                        atomo.lexema = atomo.lexema + byte
                        atomo.tipo = 'SEM_ATRIBUTOS'
                        byte = arquivo.read(1)
                        ver_linha(byte)
                        return atomo
                    else:
                        pass
                
                atomo.tipo = 'OP_RELACIONAL'
                return atomo

            if(byte in sem_atr):
                atomo.lexema = byte
                atomo.tipo = 'SEM_ATRIBUTOS'
                byte = arquivo.read(1)
                ver_linha(byte)
                return atomo
            
        
        # if(ver_delimit(byte) or byte == ''):
        #     if(atomo.lexema != ''):
        #         return atomo
        # else:
        #     atomo.lexema = atomo.lexema + byte
        #     atomo = maquina_estados(byte,atomo)

            if(byte==""):
                atomo.fim_de_arquivo = True
                return atomo
            
            else:
                atomo.erro = True
                atomo.lexema = byte
                return atomo
        
        
    