import sys
from tabPR import *
from type import *

param = sys.argv[1]

with  open(param,'r') as arquivo:
    while True:
        atomo = Atomo
        try:
            atomo = leitor(arquivo)
            print('[linha %d, Atomo: %s, lexema: %s]'%(atomo.linha, atomo.__name__, atomo.lexema))
            
        except AttributeError:
            break
    
    #print("Linha %d atomo %s"%(nlinha,atomo))

    #if(atomo != EOS & atomo != ERRO):
     #   break
