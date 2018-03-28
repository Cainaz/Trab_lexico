import sys
from tabPR import *
from type import *

param = sys.argv[1]

with  open(param,'r') as arquivo:
    while True:
        #try:
        atomo = Atomo
        atomo = leitor(arquivo)
        if(atomo.fim_de_arquivo):
            print('fim de arquivo')
            break

        if(atomo.erro):
            print('Erro de variável, essa palavra não pertence a linguagem [linha %d, lexema:%s]'%(atomo.linha,atomo.lexema))
            break

        print('[linha %d, Atomo: %s, lexema: %s]'%(atomo.linha, atomo.tipo, atomo.lexema))

        #except AttributeError:
            #break
    #print("Linha %d atomo %s"%(nlinha,atomo))

    #if(atomo != EOS & atomo != ERRO):
     #   break
