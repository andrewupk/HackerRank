import numpy

[N, M, P] = map(int, input().split())
arr_n = []
arr_m = []
for i in range(N):
    row = []
    cur_input = map(int, input().split())
    for val in cur_input:
        row.append(val)
    arr_n.append(row)

for i in range(M):
    row = []
    cur_input = map(int, input().split())
    for val in cur_input:
        row.append(val)
    arr_m.append(row)

print(numpy.concatenate((numpy.array(arr_n), numpy.array(arr_m)), axis = 0))
