from itertools import product

if __name__ == '__main__':
    [K, M] = map(int, input().split())
    lists = []
    for i in range(K):

        lists.append(list(map(int, input().split()))[1:])

    moduluses = []
    prods = product(*lists)
    for val in prods:
        sum = 0
        for v in val:
            sum += v*v
        moduluses.append(sum % M)

    print(max(moduluses))



