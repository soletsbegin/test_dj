text = """

# Разбить текс на элементы списка
def spl(word):

    # Ваш код

    return 0

assert spl('hello') == ['h', 'e', 'l', 'l', 'o']
assert spl('Hello World') == ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
"""

try:
    exec(text)
except AssertionError as err:
    tr = err.__traceback__.tb_next.tb_lineno
    print(err.__traceback__.tb_frame.f_locals['text'].split('\n')[tr-1])

