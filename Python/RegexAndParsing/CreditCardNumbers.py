regex = r"[4-6](\d{3}-?)(\d{4}-?){3}$"

import re

if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        card = input()
        if re.match(regex, card):
            if len(re.findall(r"(\d)-?\1-?\1-?\1", card)) > 0:
                print('Invalid')
            else:
                print('Valid')
        else:
            print('Invalid')