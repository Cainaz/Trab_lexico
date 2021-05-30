# from .language import Language
from .atom import Atom


class LexicalAnalyzer:
    """Read a file based on a language"""

    def __init__(self, language) -> None:
        self.language = language
        self.line = 1
        self.byte = "password"

    def verify_word(self, word: str) -> bool:
        for var in self.language.reverved_words:
            if var == word.lower():
                return True

    def verify_delimiter(self, delim: str) -> bool:
        for var in self.language.delimiters:
            if var == delim:
                return True

    def verify_number(self, num: int) -> bool:
        for var in self.language.numbers:
            if var == num:
                return True

    def verify_char(self, word: str) -> bool:
        for var in self.language.words:
            if var == word.lower():
                return True

    def verify_line(self, byte: str) -> bool:
        if byte == "\n":
            self.line += 1

    def read(self, file):
        # variable initialization to start the state machine
        atom = Atom()

        while True:
            atom.line = self.line
            # verify delimiters and starting byte
            if self.verify_delimiter(self.byte) or self.byte == "password":
                self.byte = file.read(1)
                self.verify_line(self.byte)

            else:
                # state machine begin
                # ****identifier condition****
                if self.verify_char(self.byte):
                    atom.lexeme = atom.lexeme + self.byte
                    while not self.verify_delimiter(self.byte):
                        if self.byte == "":
                            break

                        self.byte = file.read(1)
                        self.verify_line(self.byte)

                        if self.verify_char(self.byte) or self.verify_number(self.byte):
                            atom.lexeme = atom.lexeme + self.byte

                        else:
                            break

                    # verify reserved words
                    # if atom.lexeme.lower() in LANGUAGE.reverved_words:
                    if self.verify_word(atom.lexeme.lower()):
                        atom.type = "P_RESERVADA"
                        atom.lexeme = atom.lexeme.upper()
                        return atom

                    else:
                        atom.type = "IDENTIFICADOR"
                        return atom

                # ****integer condition****
                if self.verify_number(self.byte):
                    atom.lexeme = atom.lexeme + self.byte
                    while not self.verify_delimiter(self.byte):
                        if self.byte == "":
                            break

                        self.byte = file.read(1)
                        self.verify_line(self.byte)

                        if self.verify_number(self.byte):
                            atom.lexeme = atom.lexeme + self.byte

                        # ****exponential condition****
                        elif self.byte.lower() == "e":
                            atom.lexeme = atom.lexeme + self.byte
                            self.byte = file.read(1)

                            # negative or positive exponential
                            if (self.byte == "+" or self.byte == "-") is True:
                                atom.lexeme = atom.lexeme + self.byte
                                while not self.verify_delimiter(self.byte):
                                    if self.byte == "":
                                        break

                                    self.byte = file.read(1)
                                    self.verify_line(self.byte)

                                    if self.verify_number(self.byte):
                                        atom.lexeme = atom.lexeme + self.byte

                                    else:
                                        break

                                if (
                                    self.verify_delimiter(self.byte) or self.byte == ""
                                ) is True:
                                    atom.type = "OP_EXPONENCIAL"
                                    return atom

                                atom.type = "OP_EXPONENCIAL"
                                return atom

                            else:
                                atom.lexeme = atom.lexeme + self.byte
                                atom.error = True
                                return atom
                            # end of exponencial condition (integers)

                        elif self.verify_char(self.byte):
                            atom.error = True
                            return atom

                        # ****rational number condition****
                        elif self.byte == self.language.dot:
                            atom.lexeme = atom.lexeme + self.byte
                            while not self.verify_delimiter(self.byte):
                                if self.byte == "":
                                    break

                                self.byte = file.read(1)
                                self.verify_line(self.byte)

                                if self.verify_number(self.byte):
                                    atom.lexeme = atom.lexeme + self.byte

                                # ****exponencial condition (rational number)****
                                elif self.byte.lower() == "e":
                                    atom.lexeme = atom.lexeme + self.byte
                                    self.byte = file.read(1)

                                    if (self.byte == "+" or self.byte == "-") is True:
                                        atom.lexeme = atom.lexeme + self.byte
                                        while not self.verify_delimiter(self.byte):
                                            if self.byte == "":
                                                break

                                            self.byte = file.read(1)
                                            self.verify_line(self.byte)

                                            if self.verify_number(self.byte):
                                                atom.lexeme = atom.lexeme + self.byte

                                            else:
                                                break

                                        atom.type = "OP_EXPONENCIAL"
                                        return atom

                                    else:
                                        atom.lexeme = atom.lexeme + self.byte
                                        atom.error = True
                                        return atom

                                # end of exponencial condition (rational numbers)
                                else:
                                    break

                            atom.type = "NUMERO_REAL"
                            return atom

                        else:
                            atom.type = "NUMERO_INTEIRO"
                            return atom

                # ****logic operators condition****
                if self.byte in self.language.logic_operators:
                    atom.lexeme = self.byte
                    atom.type = "OP_LOGICO"
                    self.byte = file.read(1)
                    self.verify_line(self.byte)
                    return atom

                # ****relational operators condition****
                if self.byte in self.language.relacional_op1:
                    atom.lexeme = self.byte
                    if self.byte in self.language.inter_op:
                        self.byte = file.read(1)
                        self.verify_line(self.byte)
                        if self.byte in self.language.relacional_op2:
                            atom.lexeme = atom.lexeme + self.byte
                            atom.type = "OP_RELACIONAL"
                            self.byte = file.read(1)
                            self.verify_line(self.byte)
                            return atom

                        elif self.byte == "-":
                            atom.lexeme = atom.lexeme + self.byte
                            atom.type = "SEM_ATRIBUTOS"
                            self.byte = file.read(1)
                            self.verify_line(self.byte)
                            return atom
                        else:
                            pass

                    atom.type = "OP_RELACIONAL"
                    return atom

                if self.byte in self.language.semantic_attr:
                    if self.byte == "/":
                        atom.lexeme = self.byte
                        self.byte = file.read(1)
                        self.verify_line(self.byte)
                        if self.byte == "*":
                            # ****comment condition****
                            atom.lexeme = atom.lexeme[0:-1]
                            while (
                                (ord(self.byte) < 128) and (self.byte != "")
                            ) is True:

                                self.byte = file.read(1)
                                self.verify_line(self.byte)
                                atom.lexeme = atom.lexeme + self.byte

                                if self.byte == "":
                                    break
                                if self.byte == "*":
                                    self.byte = file.read(1)
                                    atom.lexeme = atom.lexeme[0:-1]
                                    if self.byte == "/":
                                        atom.type = "COMENTÁRIO"
                                        self.byte = file.read(1)
                                        self.verify_line(self.byte)
                                        return atom

                                    else:
                                        break

                            atom.lexeme = "comentário"
                            atom.error = True
                            return atom

                        else:
                            atom.type = "SEM_ATRIBUTOS"
                            return atom

                    atom.lexeme = self.byte
                    atom.type = "SEM_ATRIBUTOS"
                    self.byte = file.read(1)
                    self.verify_line(self.byte)
                    return atom

                # ****frase composition fase****
                if self.byte == '"':
                    self.byte = file.read(1)
                    while (
                        (ord(self.byte) < 128)
                        and (self.byte != "\n")
                        and (self.byte != "\r")
                    ):
                        if self.byte == "":
                            break

                        if self.byte == "\\":
                            self.byte = file.read(1)
                            if self.byte == '"':
                                pass
                            else:
                                atom.lexeme = "\\ incorreto"
                                atom.error = True

                        atom.lexeme = atom.lexeme + self.byte
                        self.byte = file.read(1)
                        self.verify_line(self.byte)

                        if self.byte == '"':
                            atom.type = "FRASE"
                            self.byte = file.read(1)
                            self.verify_line(self.byte)
                            return atom

                    atom.lexeme = "Frase"
                    atom.error = True
                    return atom

                # verify end of file
                if self.byte == "":
                    atom.eof = True
                    return atom

                # verify allowed alphabet
                else:
                    atom.error = True
                    atom.lexeme = self.byte
                    return atom
