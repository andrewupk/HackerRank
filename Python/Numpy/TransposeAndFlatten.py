import numpy

[N, M] = map(int, input().split())

arr = []
for i in range(N):
    cur_arr = map(int, input().split())
    row = []
    for val in cur_arr:
        row.append(val)
    arr.append(row)

print(numpy.transpose(numpy.array(arr)))
print(numpy.array(arr).flatten())
