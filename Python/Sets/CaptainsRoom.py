if __name__ == '__main__':
    K = int(input())
    rooms = list(map(int, input().split()))
    setR = set(rooms)
    rooms.sort()
    for i in range(0, len(rooms), K):
        if i == len(rooms)-1 or rooms[i] != rooms[i+1]:
            print(rooms[i])
            break
