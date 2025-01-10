import re

# Определение токенов
TOKENS = [
    ('WHILE', r'while'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('COLON', r':'),
    ('NUMBER', r'\d+'),
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),
    ('OP', r'[+\-*/]'),
    ('EQ', r'=='),
    ('ASSIGN', r'='),
    ('NEWLINE', r'\n'),
    ('WHITESPACE', r'[ \t]+'),
]

# Компиляция регулярных выражений
TOKEN_REGEX = [(name, re.compile(regex)) for name, regex in TOKENS]

def lexer(input_string):
    pos = 0
    tokens = []
    while pos < len(input_string):
        match = None
        for token_type, regex in TOKEN_REGEX:
            match = regex.match(input_string, pos)
            if match:
                lexeme = match.group(0)
                if token_type != 'WHITESPACE':  # Игнорируем пробелы
                    tokens.append((token_type, lexeme))
                pos = match.end(0)
                break
        if not match:
            raise SyntaxError(f"Неожиданный символ: {input_string[pos]}")
    return tokens

# Пример использования
input_code = """while (x == abc):
    x = 123 - 10 
"""

tokens = lexer(input_code)

for token in tokens:
    print(token, sep="")  # Убираем лишнюю запятую

class Parser:
    def __init__(self, tokens):  # Исправляем метод на __init__
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        self.while_loop()

    def match(self, expected_type, expected_value=None):
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == expected_type:
            if expected_value is None or self.tokens[self.pos][1] == expected_value:
                self.pos += 1
            else:
                raise SyntaxError(f"Ожидалось {expected_value}, но найдено {self.tokens[self.pos][1]}")
        else:
            raise SyntaxError(f"Ожидался {expected_type}, но найдено {self.tokens[self.pos]}")

    def while_loop(self):
        self.match('WHILE', 'while')
        self.match('LPAREN', "(")
        self.condition()
        self.match('RPAREN', ")")
        self.match('COLON', ":")
        self.match('NEWLINE', "\n")
        self.statements()

    def condition(self):
        self.expression()
        self.match('EQ', "==")
        self.expression()

    def expression(self):
        # Если токены ещё есть и выражение содержит число или идентификатор
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] in ('IDENTIFIER', 'NUMBER'):
            self.pos += 1
            # Если после выражения идёт оператор, то продолжаем
            if self.pos < len(self.tokens) and self.tokens[self.pos][0] == 'OP':
                self.pos += 1
                self.expression()
        else:
            raise SyntaxError(f"Ожидался идентификатор или число, но найдено {self.tokens[self.pos]}")

    def statements(self):
        # Пока не дошли до конца цикла, смотрим на выражения
        while self.pos < len(self.tokens):
            if self.tokens[self.pos][0] == 'NEWLINE':
                self.pos += 1
            elif self.tokens[self.pos][0] in ('IDENTIFIER', 'NUMBER'):
                self.expression()
            else:
                break

# Пример использования
# tokens = [
#     ('WHILE', 'while'), ('LPAREN', '('), ('IDENTIFIER', 'x'), ('EQ', '=='), ('NUMBER', '10'),
#     ('RPAREN', ')'), ('COLON', ':'), ('NEWLINE', '\n'), ('IDENTIFIER', 'x'), ('ASSIGN', '='),
#     ('IDENTIFIER', 'x'), ('OP', '+'), ('NUMBER', '1'), ('NEWLINE', '\n')
# ]

parser = Parser(tokens)
try:
    parser.parse()
    print("Синтаксический анализ завершён успешно.")
except SyntaxError as e:
    print(f"Ошибка синтаксического анализа: {e}")
