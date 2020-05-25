if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())
    for i in range(N):
        command = input().split()
        if command[0] == 'pop':
            s.pop()
            continue
        if command[0] == 'remove':
            s.remove(int(command[1]))
            continue
        if command[0] == 'discard':
            s.discard(int(command[1]))
            continue

    sum = 0
    for val in s:
        sum += val
    print(sum)