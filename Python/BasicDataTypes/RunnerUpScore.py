if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    larr = list(arr)
    larr.sort(reverse=True)
    for i in range(1, len(larr)):
        if larr[i] < larr[0]:
            print(larr[i]);
            break;