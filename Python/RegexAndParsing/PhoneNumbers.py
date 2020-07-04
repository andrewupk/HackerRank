regex_pattern = r"^[7-9]\d{9}$"	# Do not delete 'r'.

import re
N = int(input())
for i in range(N):
    if re.match(regex_pattern, input()):
        print('YES')
    else:
        print('NO')