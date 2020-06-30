from fractions import Fraction
from functools import reduce

def product(fracs):
    print(fracs)
    #t = # complete this line with a reduce statement
    t = reduce(lambda num, den: num * den, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)