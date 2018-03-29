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

def ver_char(letra):
    for variavel in letras:
        if(variavel == letra.lower()):
            return True
        else:
            pass

def ver_linha(byte):
    global linha
    if(byte == '\n'):
        linha += 1

#função de leitura do arquivo e que monta os atomos
def leitor(arquivo):
    #inicialização das variáveis para começo da análise na máquina de estados
    global linha, byte
    atomo = Atomo
    atomo.linha = linha
    atomo.lexema = ''
    
    while (True):
        #verificação de delimitadores e byte que inicia o arquivo 
        if(ver_delimit(byte) or byte == 'password'):
            byte = arquivo.read(1)
            ver_linha(byte)
            atomo.linha = linha
        else:
            #inicio da máquina de estados
            #****condição de identificador****
            if(ver_char(byte)):
                atomo.lexema = atomo.lexema + byte
                while(not ver_delimit(byte)):
                    if(byte == ''):
                        break

                    byte = arquivo.read(1)
                    ver_linha(byte)

                    if(ver_char(byte) or ver_numero(byte)):
                        atomo.lexema = atomo.lexema + byte

                    else:
                        break
                #verificação de palavra reservada
                if(atomo.lexema.lower() in p_reservadas):
                    atomo.tipo = 'P_RESERVADA'
                    atomo.lexema = atomo.lexema.upper()
                    return atomo

                elif((ver_delimit(byte) or byte == '') is True):
                    atomo.tipo = 'IDENTIFICADOR'
                    return atomo
            
                else:
                    atomo.tipo = 'IDENTIFICADOR'
                    return atomo

            #****condição de numero inteiro****
            if(ver_numero(byte)):
                atomo.lexema = atomo.lexema + byte
                while(not ver_delimit(byte)):
                    if(byte == ''):
                        break

                    byte = arquivo.read(1)
                    ver_linha(byte)

                    if(ver_numero(byte)):
                        atomo.lexema = atomo.lexema + byte
                    
                    #****condição de exponêncial
                    elif(byte.lower() == 'e'):
                        atomo.lexema = atomo.lexema + byte
                        byte = arquivo.read(1)
                        #pontência positiva ou negativa da exponêncial
                        if((byte == '+' or byte =='-')is True):
                            atomo.lexema = atomo.lexema + byte
                            while(not ver_delimit(byte)):
                                if(byte == ''):
                                    break

                                byte = arquivo.read(1)
                                ver_linha(byte)

                                if(ver_numero(byte)):
                                    atomo.lexema = atomo.lexema + byte
                            
                                elif((ver_char(byte) or byte =='.')is True):
                                    atomo.lexema = atomo.lexema + byte
                                    atomo.erro = True
                                    return atomo
                            
                                else:
                                    break

                            if((ver_delimit(byte) or byte == '') is True):
                                atomo.tipo = 'OP_EXPONENCIAL'
                                return atomo
                            
                              
                            atomo.tipo = 'OP_EXPONENCIAL'
                            return atomo

                        else:
                            atomo.lexema = atomo.lexema + byte
                            atomo.erro = True
                            return atomo
                        #fim da condição exponencial (numero inteiro)

                    #****condição numero real****
                    elif(byte == ponto):
                        atomo.lexema = atomo.lexema + byte
                        while(not ver_delimit(byte)):
                            if(byte == ''):
                                break

                            byte = arquivo.read(1)
                            ver_linha(byte)

                            if(ver_numero(byte)):
                                atomo.lexema = atomo.lexema + byte
                            
                            #****condição de exponencial(para numero real)****
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
                            
                                        elif((ver_char(byte) or byte =='.')is True):
                                            atomo.lexema = atomo.lexema + byte
                                            atomo.erro = True
                                            return atomo
                            
                                        else:
                                            break

                                    if((ver_delimit(byte) or byte == '') is True):
                                        atomo.tipo = 'OP_EXPONENCIAL'
                                        return atomo
                            
                              
                                    atomo.tipo = 'OP_EXPONENCIAL'
                                    return atomo

                                else:
                                    atomo.lexema = atomo.lexema + byte
                                    atomo.erro = True
                                    return atomo
                            #fim da condição enxponencial(para numero real)

                            elif((ver_char(byte) or byte == ponto)is True):
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

                elif(ver_char(byte)):
                    atomo.lexema = atomo.lexema + byte
                    atomo.erro = True
                    return atomo

                else:
                    atomo.tipo = 'NUMERO_INTEIRO'
                    return atomo

            #****condição operadores lógicos****
            if(byte in OP_LOGICO):
                atomo.lexema = byte
                atomo.tipo = 'OP_LOGICO'
                byte = arquivo.read(1)
                ver_linha(byte)
                return atomo

            #****condição para operadores relacionais****
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
                if(byte == '/'):
                    atomo.lexema = byte
                    byte = arquivo.read(1)
                    ver_linha(byte)
                    if(byte == '*'):
                        #****condição de comentário****
                        atomo.lexema = atomo.lexema[0:-1]
                        while(((ord(byte) < 128) and (byte !=''))is True):
                            
                            byte = arquivo.read(1)
                            ver_linha(byte)
                            atomo.lexema = atomo.lexema + byte

                            if(byte == ''):
                                break
                            if(byte == '*'):
                                byte = arquivo.read(1)
                                atomo.lexema = atomo.lexema[0:-1]
                                if(byte == '/'):
                                    atomo.tipo = 'COMENTÁRIO'
                                    byte = arquivo.read(1)
                                    ver_linha(byte)
                                    return atomo
                                
                                else:
                                    print('entrou no else do comentário')
                                    break
                                    
                        atomo.lexema = 'comentário'
                        atomo.erro = True
                        return atomo
                            
                    else:
                        atomo.tipo = 'SEM_ATRIBUTOS'
                        return atomo

                atomo.lexema = byte
                atomo.tipo = 'SEM_ATRIBUTOS'
                byte = arquivo.read(1)
                ver_linha(byte)
                return atomo
            
            #****estado de composição de frase****
            if(byte == '\"'):
                byte = arquivo.read(1)
                while(((ord(byte) < 128) and (byte != '\n') and (byte != '\r'))):
                    if(byte == ''):
                        break

                    if(byte == '\\'):
                        byte = arquivo.read(1)
                        if(byte == '\"'):
                            pass
                        else:
                            atomo.lexema = '\\ incorreto'
                            atomo.erro = True

                    atomo.lexema = atomo.lexema + byte
                    byte = arquivo.read(1)
                    ver_linha(byte)
                    

                    if(byte == '\"'):
                        atomo.tipo = 'FRASE'
                        byte = arquivo.read(1)
                        ver_linha(byte)
                        return atomo

                atomo.lexema = 'Frase'
                atomo.erro = True
                return atomo

            #verificador de byte de fim de arquivo
            if(byte==""):
                atomo.fim_de_arquivo = True
                return atomo
            
            #verificador de alfabeto permitido
            else:
                atomo.erro = True
                atomo.lexema = byte
                return atomo
        
        
    