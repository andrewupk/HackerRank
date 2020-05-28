from itertools import combinations

if __name__ == '__main__':
    N = int(input())
    lst = input().split()
    K = int(input())

    combs = list(combinations(list(range(1, N+1)), K))
    #print(combs)
    res = 0
    for val in combs:
        for v in val:
            if lst[v-1] == 'a':
                res += 1
                break

    print(res / len(combs))