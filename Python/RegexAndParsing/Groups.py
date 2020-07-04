import re

if __name__ == '__main__':
    regex = r"(?P<group>[a-z0-9]{1,})\1"
    S = input()
    matches = re.finditer(regex, S, re.MULTILINE)
    ismatch = False
    for matchNum, match in enumerate(matches, start=1):
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            print(match.group(groupNum))
            ismatch = True
            break
        break
    if not ismatch:
        print(-1)