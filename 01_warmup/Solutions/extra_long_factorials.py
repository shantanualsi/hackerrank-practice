from __future__ import print_function

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


if __name__ == '__main__':
    num = int(raw_input())

    print(factorial(num))
