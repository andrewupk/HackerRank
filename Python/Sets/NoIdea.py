if __name__ == '__main__':
    [n, m] = list(map(int, input().split()))
    array = list(map(int, input().split()))
    setA = set(map(int, input().split()))
    setB = set(map(int, input().split()))

    happiness = 0
    for i in range(n):
        if array[i] in setA:
            happiness += 1
        if array[i] in setB:
            happiness -= 1

    print(happiness)