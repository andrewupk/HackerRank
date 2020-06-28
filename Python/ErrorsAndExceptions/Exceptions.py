if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        [a, b] = input().split()
        try:
            print(int(int(a)/int(b)))
        except ZeroDivisionError as e:
            print('Error Code: integer division or modulo by zero')
        except ValueError as e:
            print('Error Code: {0}'.format(e))
