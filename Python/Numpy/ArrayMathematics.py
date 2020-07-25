import numpy

[N, M] = map(int, input().split())
arr_A = []
arr_B = []
for i in range(N):
    row = map(int, input().split())
    curr_arr = []
    for val in row:
        curr_arr.append(val)
    arr_A.append(curr_arr)

for i in range(N):
    row = map(int, input().split())
    curr_arr = []
    for val in row:
        curr_arr.append(val)
    arr_B.append(curr_arr)

nparr_A = numpy.array(arr_A, int)
nparr_B = numpy.array(arr_B, int)

print(nparr_A + nparr_B)
print(nparr_A - nparr_B)
print(nparr_A * nparr_B)
print(nparr_A // nparr_B)
print(nparr_A % nparr_B)
print(nparr_A ** nparr_B)
