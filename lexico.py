import sys
from leitor import *
from type import *

param = sys.argv[1]

#Loop principal e amostragem de atomos e erros
with  open(param,'r') as arquivo:
    while True:
        atomo = Atomo
        atomo = leitor(arquivo)
        if(atomo.fim_de_arquivo):
            break

        if(atomo.erro):
            print('Erro, essa palavra não pertence a linguagem ou padrão incorreto [Linha %d, Erro em: %s]'%(atomo.linha,atomo.lexema))
            break

        print('[Linha %d, Átomo: %s, Lexema: %s]'%(atomo.linha, atomo.tipo, atomo.lexema))

