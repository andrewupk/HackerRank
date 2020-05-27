from itertools import combinations_with_replacement

if __name__ == '__main__':
    [S, k] = input().split()
    k = int(k)
    S = list(S)
    S.sort()
    listperm = list(combinations_with_replacement(S, k))
    for val in listperm:
        print(''.join(val))