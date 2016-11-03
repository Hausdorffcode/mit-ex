from string import *

# this is a code file that you can use as a template for submitting your
# solutions


# these are some example strings for use in testing your code

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

def subStringMatchExact(target, key):
    startPoint = []
    for index in range(0, len(target)):
        if target.find(key, index, -1) == index:
            startPoint.append(index)
    return tuple(startPoint)

##print subStringMatchExact(target1, key10)
print subStringMatchExact(target1, key12)
##print subStringMatchExact(target2, key12)
##print subStringMatchExact(target2, key13)


