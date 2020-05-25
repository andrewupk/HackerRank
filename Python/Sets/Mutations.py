if __name__ == '__main__':
    nA = int(input())
    A = set(map(int, input().split()))
    N = int(input())
    for i in range(N):
        command = input().split()
        otherSet = set(map(int, input().split()))
        if command[0] == 'intersection_update':
            A.intersection_update(otherSet)
            continue
        if command[0] == 'update':
            A.update(otherSet)
            continue
        if command[0] == 'symmetric_difference_update':
            A.symmetric_difference_update(otherSet)
            continue
        if command[0] == 'difference_update':
            A.difference_update(otherSet)
            continue

        sum = 0
        for val in A:
            sum += val
        print(sum)