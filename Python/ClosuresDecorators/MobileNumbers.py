def wrapper(f):
    def fun(l):
        # complete the function
        res = []
        for number in l:
            res.append("+91 {} {}".format((int(number) % 10000000000) // 100000, int(number) % 100000))
        f(res)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)