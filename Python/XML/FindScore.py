import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    score = len(node.attrib)
    #print("Tag: {}, Attr: {}, Len: {}".format(node.tag, len(node.attrib), len(node)))
    if len(node):
        for child in node:
            score += get_attr_number(child)
            """
        else:
            score += len(node.attrib)
            """
    return score

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
