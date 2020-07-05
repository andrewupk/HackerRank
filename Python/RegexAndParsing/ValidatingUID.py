import re

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        uid = input()
        if re.match(r"[a-zA-Z0-9]{10}", uid):
            if len(re.findall(r"\d", uid)) >= 3:
                if len(re.findall(r"[A-Z]", uid)) >= 2:
                    if len(re.findall(r"([a-zA-Z0-9]).*\1", uid)) > 0:
                        print('Invalid')
                    else:
                        print('Valid')
                else:
                    print('Invalid')
            else:
                print('Invalid')
        else:
            print('Invalid')