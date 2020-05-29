from collections import defaultdict

if __name__ == '__main__':
    [n, m] = list(map(int, input().split()))
    A = defaultdict(list)
    for i in range(n):
        A[input()].append(i+1)

    #print(A)
    B = defaultdict(list)
    words = []
    for i in range(m):
        val = input()
        words.append(val)
        if A[val]:
            B[val] = A[val]
        else:
            B[val].append(-1)
    #print(B)
    """
    for key, val in B.items():
        #print('{0}: {1}'.format(key, val))
        for ind in val:
            print('{0}'.format(ind), end=' ')
        print()
    """
    for word in words:
        for ind in B[word]:
            print('{0}'.format(ind), end=' ')
        print()