from itertools import groupby

if __name__ == '__main__':
    S = input()
    for k, g in groupby(S):
        print('({1}, {0}) '.format(k, len(list(g))), end='')
