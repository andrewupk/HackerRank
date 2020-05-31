def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        cur_s = string[i:i+k]
        res = ''
        for char in cur_s:
            if char not in res:
                res += char
        print(res)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


