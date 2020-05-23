def print_rangoli(size):
    # your code goes here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rows = []
    for i in range(size-1, -1, -1):
        letters = ''
        for j in range(size-1, i-1, -1):
            letters += alphabet[j]
        rows.append(print_row(letters).center(4*size-3, '-'))

    for i in range(len(rows)):
        print(rows[i])
    for i in range(len(rows)-1, 0, -1):
        print(rows[i-1])

def print_row(letters):
    result = ''
    llet = list(letters)
    rllet = llet.copy()
    rllet.reverse()
    let = llet + rllet[1:]
    for i in range(len(let)-1):
        result += let[i] + '-'
    result += let[0]
    return result

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)