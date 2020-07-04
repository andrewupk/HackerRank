regex = r"<([a-zA-Z])([0-9a-zA-z\-\,\.\,\_]+)@[a-zA-Z]+\.{1}[a-z]{1,3}>"

import re

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        s = input()
        r = re.search(regex, s)
        if r:
            print(s)