if __name__ == '__main__':
    N = int(input())
    countries = set()
    for i in range(N):
        countries.add(input())
    print(len(countries))