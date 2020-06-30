import re

def fun(s):
    # return True if s is a valid email, else return False
    pattern = re.compile("([a-z0-9-_]+)@([a-z0-9]+)\.(\w{1,3})")
    return pattern.match(s)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)