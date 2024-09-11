from math import sqrt

def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True



if __name__ == '__main__':
    n = int(input())

    if is_prime(n):
        print("Это число простое")
    else:
        print("Это не простое число")