from collections import deque

if __name__ == '__main__':
    N = int(input())
    d = deque()
    for i in range(N):
        command = input().split()
        if command[0] == 'append':
            d.append(int(command[1]))
        if command[0] == 'appendleft':
            d.appendleft(int(command[1]))
        if command[0] == 'pop':
            d.pop()
        if command[0] == 'popleft':
            d.popleft()

    for val in d:
        print('{0}'.format(val), end=' ')