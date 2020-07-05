import re

if __name__ == '__main__':
    N = int(input())
    code = []
    for i in range(N):
        code.append(input())
    code = "\n".join(code)
    r = re.search(r"\s&{2}\s", code)
    while r:
        code = re.sub(r"\s&{2}\s", " and ", code)
        r = re.search(r"\s&{2}\s", code)
    r = re.search(r"\s\|{2}\s", code)
    while r:
        code = re.sub(r"\s\|{2}\s", " or ", code)
        r = re.search(r"\s\|{2}\s", code)
    print(code)