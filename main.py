#!/usr/bin/env python3
# https://github.com/MrBlaise/learnpython/blob/master/Numbers/pi.py
# Find PI to the Nth Digit
# Have the user enter a number 'n'
# and print out PI to the 'n'th digit
from color_filler import writing_number


def calcPi():  # Generator function
    """
    Prints out the digits of PI
    until it reaches the given limit
    """

    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3

    # decimal = limit
    counter = 0

    while True:
        if 4 * q + r - t < n * t:
            # yield digit

            if "b" == writing_number(n):
                break
            # insert period after first digit
            if counter == 0:
                if "b" == writing_number('.'):
                    break
            # end
            counter += 1
            nr = 10 * (r - n * t)
            n = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r = nr
        else:
            nr = (2 * q + r) * l
            nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
            q *= k
            t *= l
            l += 2
            k += 1
            n = nn
            r = nr


def main():  # Wrapper function

    # # Calls CalcPi with the given limit
    # pi_digits = calcPi()
    calcPi()
    # i = 0
    #
    # # Prints the output of calcPi generator function
    # # Inserts a newline after every 40th number
    # for d in pi_digits:
    #     print(d, end='')
    #     i += 1
    #     if i == 40:
    #         print("")
    #         i = 0


if __name__ == '__main__':
    main()
