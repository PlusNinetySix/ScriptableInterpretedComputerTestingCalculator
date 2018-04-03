import string
from sictc.Token import Token, TokenEnum, Tokens


def scanner():
    line = input("Please input a string to be tokenized.\n")
    tokens = Tokens()
    failed = False
    skip = 0

    for i in range(len(line)):
        if skip > 0:
            skip -= 1
            continue

        character = line[i]
        token = None

        if character in string.whitespace:
            continue

        if character in ["("]:
            token = Token(TokenEnum.OPEN_PAREN, "(")
        elif character in [")"]:
            token = Token(TokenEnum.CLOSE_PAREN, ")")
        elif character in [":"]:
            token = Token(TokenEnum.COLON, ":")
        elif character in [";"]:
            token = Token(TokenEnum.SEMICOLON, ";")
        elif character in ["."]:
            token = Token(TokenEnum.PERIOD, ".")
        elif character in [","]:
            token = Token(TokenEnum.COMMA, ",")
        elif character in string.ascii_letters:
            word = [character, ]

            # alpha + (beta + gamma)
            for j in range(1, len(line[i:])):
                lookahead = line[i + j]
                skip += 1

                if lookahead in string.whitespace:
                    continue

                if lookahead not in string.ascii_letters:
                    skip -= 1
                    break

                word.append(lookahead)

            token = Token(TokenEnum.VARIABLE, "".join(word))
        elif character in ["+", "-", "*", "/", "%"]:
            token = [character, ]

        if token is not None:
            tokens.append(token)
        else:
            print("Invalid character "
                  "{0} at index {1}".format(repr(character), i))
            failed = True
            break

    if not failed:
        tokens.append(Token(TokenEnum.EOF, "$"))
        return tokens
    else:
        return []

    import string

    fstream = None
    offset = 0

    def scan():
        global fstream
        global offset

        while True:
            fstream.seek(offset)
            character = fstream.read(1)
            offset += 1

            if character not in string.whitespace or character in "":
                break
            else:
                print('Skipping whitespace')

        return character

    def filescanner(filename):
        global fstream
        global offset

        comment = False

        with open(filename) as fstream:
            while True:
                character = scan()

                if character in ['#']:
                    comment = not comment
                    continue

                if not character:
                    break

                if not comment:
                    word = [character]
                    if character in string.ascii_letters:
                        while True:
                            lookahead = scan()
                            if lookahead not in string.ascii_letters:
                                offset -= 1
                                character = "".join(word)
                                break

                            word.append(lookahead)

                        if character in string.digits:
                            while True:
                                offset -= 1
                                character = "".join(word)
                                break
                        word.append(lookahead)

                print(character)

    if comment:
        print('Error! comment not closed correctly.')


if __name__ == "__main__":
    filescanner(filename)