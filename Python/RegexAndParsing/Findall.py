import re

if __name__ == '__main__':
    regex = r"(?P<vowels>[AEIOUaeiou]{2,})[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]{1}"
    S = input()
    matches = re.finditer(regex, S)
    ismatch = False
    for matchNum, match in enumerate(matches, start=1):
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            print(match.group(groupNum))
            ismatch = True

    if not ismatch:
        print(-1)