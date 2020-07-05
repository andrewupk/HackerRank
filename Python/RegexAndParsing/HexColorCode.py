regex = r"(?P<color>#[0-9A-Fa-f]{3,6})[;,)]"

import re

if __name__ == '__main__':
    N = int(input())
    styles = []
    for i in range(N):
        styles.append(input())
    styles = "\n".join(styles)
    matches = re.findall(regex, styles)
    for m in matches:
        print(m)