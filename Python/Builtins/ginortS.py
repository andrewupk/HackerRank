# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
print(*sorted(s, key=lambda ch: (ch.isdigit() and int(ch) % 2 == 0, ch.isdigit() and int(ch) % 2 == 1, ch.isupper(), ch.islower(), ch)), sep='')
