
import itertools

from string import ascii_letters
from string import digits
from string import punctuation

from datetime import datetime
import time

from win32com import client


def brute_xlsx():
    possible_symbols = digits + ascii_letters + punctuation
    count = 0
    for length in range(32):
        for password in itertools.product(possible_symbols, repeat=length):
            password = ''.join(password)
            print(password)
            open_doc = client.Dispatch('Excel.Application')
            count += 1

            try:
                open_doc.Workbooks.Open(
                    r'C:\Users\God\Desktop\test_password.xlsx',
                    False,
                    True,
                    None,
                    password
                )
                print(password)
                return password
            except:
                print(count)




def main():
    start = time.time()
    print(f'Started - {datetime.utcfromtimestamp(time.time()).strftime("%H:%M:%S")}')
    brute_xlsx()
    print(f'Finished - {datetime.utcfromtimestamp(time.time()).strftime("%H:%M:%S")}')


if __name__ == '__main__':
    main()