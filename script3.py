import sys
from functools import partial

ls = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def binary(n: int, base=10):
    try:
        return bin(int(n, base))[2:]
    except ValueError as ex:
        print(ex.args)
        sys.exit(0)


def to_base64ch(index: int):
    return ls[index]


def from_base64ch(ar: str):
    return ls.index(ar)


binary = partial(binary, base=16)


def bin_rjust(x):
    return binary(x).rjust(8, '0')


def bytes(s: str):
    ar = s.split()
    ar = '\\x'.join(ar)
    return s


def to_base64(ar: bytearray):
    pass


def from_base64(ar: str):
    pass


# =====================================================================


prompt = 'введите список чисел через пробел\nв 16 системе исчисления:\n'
ar = input(prompt).split()
ar = list(map(bin_rjust, ar))
ar = ''.join(ar)
ar += '0' * (6 - len(ar) % 6)
ar = [ar[i:i+6] for i in range(0, len(ar), 6)]
chars = [to_base64ch(int(el, base=2)) for el in ar]
chars += '=' * (3 - len(ar)*6 // 8 % 3)
print(''.join(chars))
