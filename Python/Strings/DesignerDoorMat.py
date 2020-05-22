if __name__ == '__main__':
    input = input().split()
    N = int(input[0])
    M = int(input[1])

    for i in range(1, N-1, 2):
        print(('.|.'*i).center(M, '-'))
    print('WELCOME'.center(M, '-'))
    for i in range(N-2, 0, -2):
        print(('.|.'*i).center(M, '-'))