
import itertools
import re

from string import ascii_letters
from string import digits
from string import punctuation


def brute_xlsx():
    possible_symbols = digits + ascii_letters + punctuation
    for length in range(0,32):
        for password in itertools.product(possible_symbols, repeat=length):
            password = ''.join(password)
            print(password)



def main():
    brute_xlsx()


if __name__ == '__main__':
    main()