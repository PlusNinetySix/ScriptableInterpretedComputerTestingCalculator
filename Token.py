import enum


class Tokens(object):
    def __init__(self):
        self._data = []

    def __iter__(self):
        return iter(self._data)

    def append(self, token):
        self._data.append(token)

    @property
    def lookahead(self):
        return self._data[0]

    def consume(self):
        self._data.pop(0)


class Token(object):
    def __init__(self, kind, value):
        self._kind = kind
        self._value = value

    def __str__(self):
        return "{0} {1}".format(self.kind, self.value)

    @property
    def kind(self):
        return self._kind

    @property
    def value(self):
        return self._value


# different kinds of tokens
class TokenEnum(enum.Enum):

    def __str__(self):
        return self.name

    VARIABLE = enum.auto()
    OP = enum.auto()
    OPEN_PAREN = enum.auto()
    CLOSE_PAREN = enum.auto()
    COLON = enum.auto()
    SEMICOLON = enum.auto()
    PERIOD = enum.auto()
    COMMA = enum.auto()
    EOF = enum.auto()