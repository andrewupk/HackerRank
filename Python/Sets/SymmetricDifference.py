if __name__ == '__main__':
    M = int(input())
    mlist = set(map(int, input().split()))
    N = int(input())
    nlist = set(map(int, input().split()))
    print('M: {0}, N: {1}'.format(M, N))
    print(mlist)
    print(nlist)
    for val in sorted(mlist.difference(nlist).union(nlist.difference(mlist))):
        print(val)