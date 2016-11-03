###
### template of code for Problem 4 of Problem Set 2, Fall 2008
###

#bestSoFar = 0     # variable that keeps track of largest number
                  # of McNuggets that cannot be bought in exact quantity
#packages = (6,9,20)   # variable that contains package sizes

#for n in range(1, 150):   # only search for solutions up to size 150
    ## complete code here to find largest size that cannot be bought
    ## when done, your answer should be bound to bestSoFar

def amount_packages(packagesNumber, packages):
    if packagesNumber == 1:
        return packages[0]
    if packagesNumber == 2:
        return packages[1]
    if packagesNumber == 3:
        return packages[2]
    else:
        return -1000000
    
def cc(n, packagesNumber, packages):
    if n == 0:
        return 1
    elif n < 0 or packagesNumber == 0:
        return 0
    else:
        return cc(n, packagesNumber - 1, packages) + cc(n - amount_packages(packagesNumber, packages), packagesNumber, packages)

def find_the_exact_number(packages):
    bestSoFar = 1
    for n in range(1, 150):
        test = True
        x = bestSoFar
        for i in range(1, 6):
            if cc(x, 3, packages) == 0:
                test = False
                break
            else:
                x = x + 1
        if test:
            print '''Given package size %i, %i, and %i, the largest number of
Mcnuggets that can not be bought in exact quantity is: %i''' %(packages[0], packages[1], packages[2], bestSoFar - 1)
            return
        else:
            bestSoFar += 1

find_the_exact_number((6, 9, 20))
