import calendar

if __name__ == '__main__':
    [MM, DD, YYYY] = list(map(int, input().split()))
    print(MM)
    print(DD)
    print(YYYY)

    print(list(calendar.day_name)[calendar.weekday(YYYY, MM, DD)].upper())