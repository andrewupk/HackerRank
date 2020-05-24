def average(array):
    # your code goes here
    print(array)
    setarr = set(array)
    print(setarr)
    sum = 0
    for val in setarr:
        sum += val
    return sum/len(setarr)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)