import sys
from utils.language import Language
from utils.lexical_analyzer import LexicalAnalyzer

param = sys.argv[1]


if __name__ == "__main__":
    # Principal loop atom information

    lang = Language()
    lex_analyzer = LexicalAnalyzer(lang)
    with open(param, "r") as arquivo:
        while True:
            atom = lex_analyzer.read(arquivo)
            if atom.eof:
                break

            if atom.error:
                print(
                    "Error, this word does not belong to the language or the pattern is incorrect [Line %d, Position: %s]"
                    % (atom.line, atom.lexeme)
                )
                break
            else:
                print(
                    "[Line %d, Atom: %s, Lexeme: %s]"
                    % (atom.line, atom.type, atom.lexeme)
                )
