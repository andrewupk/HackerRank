import cmath

if __name__ == '__main__':
    value = complex(input())
    print(abs(value))
    print(cmath.phase(value))