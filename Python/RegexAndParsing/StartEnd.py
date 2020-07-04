import re

if __name__ == '__main__':
    S = input()
    k = input()
    regex = re.compile(k)
    r = re.search(regex, S)
    ismatch = False
    while r:
        print("({0}, {1})".format(r.start(), r.end()-1))
        r = regex.search(S, r.start()+1)
        ismatch = True
    if not ismatch:
        print("(-1, -1)")