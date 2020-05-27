from itertools import combinations

if __name__ == '__main__':
    [S, k] = input().split()
    k = int(k)
    string = list(S)
    string.sort()
    for i in range(1, k+1):
        listperm = list(combinations(string, i))
        for val in listperm:
            print(''.join(val))