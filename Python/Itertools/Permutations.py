from itertools import permutations

if __name__ == '__main__':
    [S, k] = input().split()
    k = int(k)
    listperm = list(permutations(S, k))
    listperm.sort()
    for val in listperm:
        print(''.join(val))