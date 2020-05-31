class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):

        diffs = []

        for i in range(len(self.__elements)):
            for j in range(i+1, len(self.__elements)):
                diffs.append(abs(self.__elements[i] - self.__elements[j]))
        
        self.maximumDifference = sorted(diffs, reverse=True)[0]

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
