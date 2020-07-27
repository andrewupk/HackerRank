import numpy

numpy.set_printoptions(sign=' ')
arr = map(float, input().split())
np_arr = numpy.array(list(arr), float)
print(numpy.floor(np_arr))
print(numpy.ceil(np_arr))
print(numpy.rint(np_arr))