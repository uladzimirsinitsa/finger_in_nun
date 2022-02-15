
import itertools

from collections import deque
from string import ascii_letters
from string import digits
from string import punctuation


LENGHT = 4


def create_write_save_file() -> list:
    possible_symbols = digits + ascii_letters + punctuation
    count = 0
    passwords = []
    for length in range(LENGHT + 1):
        for password in itertools.product(possible_symbols, repeat=length):
            password = ''.join(password)
            passwords.append(password)
            if len(passwords) > 1000:
                with open('passwords.txt', 'a') as file:
                    while passwords:
                        file.write(passwords.pop())


def main() -> None:
    passwords = create_write_save_file()



if __name__=='__main__':
    main()
