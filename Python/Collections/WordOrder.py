from collections import OrderedDict

if __name__ == '__main__':
    N = int(input())
    words = OrderedDict()
    for i in range(N):
        word = input()
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    print(len(words))
    for word, count in words.items():
        print('{0}'.format(count), end=' ')