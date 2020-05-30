from collections import deque

if __name__ == '__main__':
    T = int(input())
    results = []
    for i in range(T):
        n = int(input())
        cubes = deque(map(int, input().split()))
        new_cubes = []
        if cubes[0] > cubes[-1]:
            new_cubes.append(cubes.popleft())
        else:
            new_cubes.append(cubes.pop())
        while len(cubes):
            if cubes[0] > cubes[-1]:
                if new_cubes[-1] >= cubes[0]:
                    new_cubes.append(cubes.popleft())
                else:
                    results.append('No')
                    break
            else:
                if new_cubes[-1] >= cubes[-1]:
                    new_cubes.append(cubes.pop())
                else:
                    results.append('No')
                    break
        if len(new_cubes) == n:
            results.append('Yes')

    for res in results:
        print(res)