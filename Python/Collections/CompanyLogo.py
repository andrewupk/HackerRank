from collections import Counter

if __name__ == '__main__':
    name = input()
    letters = Counter(name)
    letters_sorted = sorted(letters.most_common(), key=lambda item: (-item[1], item[0]))
    for i in range(0, 3):
        print('{0} {1}'.format(letters_sorted[i][0], letters_sorted[i][1]))
