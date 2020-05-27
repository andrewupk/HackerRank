from itertools import product

if __name__ == '__main__':
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    for val in list(product(A, B)):
        print('{0} '.format(val), end='')