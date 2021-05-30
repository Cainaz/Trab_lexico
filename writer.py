import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "teste.ptl")

file = open(filename, "w")
file.write(' "\\".ola mundo\\""\n')
file.write("operador 9oi logico fim; 10e+.10 5E-1 10.2e-3.34, \n")
file.write("que Ret_%ORnE_ 123..45 \n")
file.write("variaveis123oi inIciO /*porque 41414141&esse nao pega*/ \n")
file.write('bla bla bla"23" 45%1.1329u40134 ')
file.close()
