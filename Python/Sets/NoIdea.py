#TODO
if __name__ == '__main__':
    [n, m] = list(map(int, input().split()))
    array = set(map(int, input().split()))
    setA = set(map(int, input().split()))
    setB = set(map(int, input().split()))

    print(len(array.intersection(setA)) - len(array.intersection(setB)))
