import numpy

[N, M] = map(int, input().split())
print(str(numpy.eye(N, M)).replace('1', ' 1').replace('0', ' 0'))
