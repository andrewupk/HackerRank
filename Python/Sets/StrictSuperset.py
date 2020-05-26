if __name__ == '__main__':
    A = set(map(int, input().split()))
    n = int(input())
    result = True
    for i in range(n):
        N = set(map(int, input().split()))
        if not A.issuperset(N):
            result = False
            break

    print(result)