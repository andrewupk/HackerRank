import math

if __name__ == '__main__':
    AB = int(input())
    BC = int(input())

    theta = math.degrees(math.atan(AB / BC))
    print('{0}°'.format(round(theta)))