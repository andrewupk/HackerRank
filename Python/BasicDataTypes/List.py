if __name__ == '__main__':
    N = int(input())
    result = []

    for i in range(N):
        command, *values = input().split()
        #print(command)
        data = list(map(int, values))
        #print(data)
        if command == 'insert':
            result.insert(data[0], data[1])
        if command == 'print':
            print(result)
        if command == 'remove':
            result.remove(data[0])
        if command == 'append':
            result.append(data[0])
        if command == 'sort':
            result.sort()
        if command == 'pop':
            result.pop()
        if command == 'reverse':
            result.reverse()