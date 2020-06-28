if __name__ == '__main__':
    N = int(input())
    list = input().split()
    if all(int(val) > 0 for val in list):
        if any(j == j[::-1] for j in list):
            print(True)
        else:
            print(False)
    else:
        print(False)