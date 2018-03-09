import sys
from tabPR import *
from type import *
param = sys.argv[1]
with  open(param,'r') as arquivo:
    while True:
        atomo = Atomo
        try:
            atomo = leitor(arquivo)
            print('lexema: %s, linha %d'%(atomo.lexema, atomo.linha))
        except AttributeError:
            break
    
    #print("Linha %d atomo %s"%(nlinha,atomo))

    #if(atomo != EOS & atomo != ERRO):
     #   break
