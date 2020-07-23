import numpy

arr = input().strip().split(' ')
my_arr = numpy.array(arr, int)
my_arr.shape = (3,3)
print(my_arr)