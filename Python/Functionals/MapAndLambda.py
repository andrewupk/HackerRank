cube = lambda x: x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    if (n == 0):
        return []
    if (n == 1):
        return [0]
    if (n == 2):
        return [0, 1]
    if (n > 2):
        prev = fibonacci(n-1)
        prev.append(prev[-1] + prev[-2])
        return prev

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))