import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    #print("{}: {}".format(elem.tag, level))
    if level + 1 > maxdepth:
        maxdepth = level + 1 
    if (len(elem)):
        for child in elem:
            depth(child, level + 1) 

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
