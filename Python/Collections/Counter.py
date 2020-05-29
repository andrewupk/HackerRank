from collections import Counter

if __name__ == '__main__':
    X = int(input())    #number of shoes
    sizes = list(map(int, input().split()))
    N = int(input())    #number of customers
    desire = []
    for i in range(N):
        desire.append(tuple(map(int, input().split())))

    dict_sizes = Counter(sizes)
    print(dict_sizes)
    #for size, count in Counter(sizes).items():
    #    print('Count: {0}, size: {1}'.format(count, size))

    money = 0
    for size, price in desire:
        print('Size: {0}, price: {1}'.format(size, price))
        if dict_sizes[size] > 0:
            dict_sizes[size] -= 1
            money += price
            print(dict_sizes)

    print(money)