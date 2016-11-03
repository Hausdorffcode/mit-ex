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

def countSubStringMatch(target, key):
    count = 0
    for index in range(0, len(target)):
        if target.find(key, index, -1) == index:
            count += 1
    return count

##print countSubStringMatch(target1, key10)
##print countSubStringMatch(target1, key11)
##print countSubStringMatch(target2, key12)
##print countSubStringMatch(target2, key13)

def countSubStringMatchRecursive(target, key):
    if len(target) < len(key):
        return 0
    else:
        if target.find(key) != 0:
            count = 0
        else:
            count = 1
        return count + countSubStringMatchRecursive(target[1:], key)

##print countSubStringMatchRecursive(target1, key10)
##print countSubStringMatchRecursive(target1, key11)
##print countSubStringMatchRecursive(target1, key12)
##print countSubStringMatchRecursive(target1, key13)
