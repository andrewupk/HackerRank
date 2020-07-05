regex = r"<(?P<isend>/?)(?P<tag>\w+)\s?(?P<isempty>/?)(?P<attributes>[\w -=]*)>(?P<value>[\w -]*)"

import re

if __name__ == '__main__':
    N = int(input())
    html = []
    for i in range(N):
        html.append(input())
    html = "".join(html)

    matches = re.finditer(regex, html, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        if match.group(1) == "/":
            print("End   : {}".format(match.group(2)))
        else:
            if match.group(3) == "/":
                print("Empty : {}".format(match.group(2)))
            else:
                print("Start : {}".format(match.group(2)))
                if match.group(4):
                    attrs = re.split(r"\s", match.group(4))
                    for attr in attrs:
                        splitted = re.split("=", attr)
                        if len(splitted) > 1:
                            print("-> {} > {}".format(splitted[0], re.findall(r"[\'\"]([\w\/\-\.]+)[\'\"]", splitted[1])[0]))
                        else:
                            print("-> {} > {}".format(splitted[0], 'None'))