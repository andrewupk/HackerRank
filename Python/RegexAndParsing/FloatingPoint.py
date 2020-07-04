import re

if __name__ == '__main__':
    regex = re.compile("^[+-]?\d*(\.{1}\d{1,})$")

    T = int(input())
    for i in range(T):
        s = input()
        if regex.match(s):
            print(True)
        else:
            print(False)