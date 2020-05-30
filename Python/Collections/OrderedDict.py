from collections import OrderedDict

if __name__ == '__main__':
    N = int(input())
    items = OrderedDict()
    for i in range(N):
        item = list(input().split())
        name = ''
        price = 0
        if len(item) == 2:
            #items[item[0]] = item[1]
            name = item[0]
            price = int(item[1])
        if len(item) == 3:
            name = '{0} {1}'.format(item[0], item[1])
            price = int(item[2])
            #items['{0} {1}'.format(item[0], item[1])] = item[2]

        if name in items:
            items[name] += price
        else:
            items[name] = price

    for name, price in items.items():
        print('{0} {1}'.format(name, price))