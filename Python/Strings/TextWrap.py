import textwrap

def wrap(string, max_width):
    result = ''
    for line in (textwrap.wrap(string, width = max_width)):
        result = result + line + '\n'
    return result

if __name__ == '__main__':

    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)