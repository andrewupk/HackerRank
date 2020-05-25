if __name__ == '__main__':
    n = int(input())
    nset = set(map(int, input().split()))
    b = int(input())
    bset = set(map(int, input().split()))
    print(len(nset.symmetric_difference(bset)))