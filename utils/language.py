class Language:
    linha = 1
    byte = "password"

    def __init__(self) -> None:
        self.reverved_words = [
            "algoritmo",
            "ate",
            "cadeia",
            "caracter",
            "enquanto",
            "entao",
            "faca",
            "fim",
            "funcao",
            "inicio",
            "inteiro",
            "para",
            "passo",
            "procedimento",
            "real",
            "ref",
            "retorne",
            "se",
            "senao",
            "variaveis",
        ]
        self.delimiters = [" ", "\n", "\t", "\r"]
        self.semantic_attr = [".", "(", ")", ";", ",", "-", "+", "*", "/", "%"]
        self.relacional_op1 = ["<", "=", ">"]
        self.inter_op = ["<", ">"]
        self.relacional_op2 = ["=", ">"]
        self.logic_operators = ["&", "$", "!"]
        self.words = [
            "_",
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]
        self.numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.dot = "."
        self.quot_mark = '"'
