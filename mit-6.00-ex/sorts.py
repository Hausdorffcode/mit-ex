

def selectionSort(a):
    for i in range(0, len(a)):
        min = i
        for j in range(i+1, len(a)):
            if a[j] < a[min]:
                min = j
        temp = a[i]
        a[i] = a[min]
        a[min] = temp

def insertSort(a):
    for i in range(1, len(a)):
        temp = a[i]
        j = i - 1
        while j >= 0 and a[j] > temp:
            a[j+1] = a[j]
            j = j - 1
        a[j+1] = temp

def merge(a, left, mid, right):
    aux = a[:]
    i = left
    j = mid + 1
    for k in range(left, right+1):
        if(i <= mid and (j > right or aux[i] <= aux[j])):
           a[k] = aux[i]
           i = i + 1
        else:
           a[k] = aux[j]
           j = j + 1

##x = [1,3,5,2,4,6]
##merge(x, 0, 2, 5)
##print x

def mergeSort(a, left ,right):
    if (right <= left):
        return
    else:
        mid = (left + right) / 2
        mergeSort(a, left, mid)
        mergeSort(a, mid+1, right)
        merge(a, left, mid, right)
            
def topDownMergeSort(a):
    mergeSort(a, 0, len(a)-1)

def bottomUpMergeSort(a):
    n = len(a)
    size = 1
    while(size < n):
        for left in range(0, n-size, 2*size):
            merge(a, left, left+size-1, min(n-1, left+2*size-1))
        size = 2*size

def testSort(f):
    a = [-1,0,1,2,3,4,5,6,7,8,9]
    f(a)
    if a == [-1,0,1,2,3,4,5,6,7,8,9]:
        print "First test success!"
    else:
        print a
        print "First test failed"

    b = [9,8,7,6,5,4,3,2,1,0,-1]
    f(b)
    if b == [-1,0,1,2,3,4,5,6,7,8,9]:
        print "Second test success!"
    else:
        print b
        print "Second test failed"

    c = [-22, 5, 3, 78, 23, 9, 100, 4]
    f(c)
    if c == [-22, 3, 4, 5, 9, 23, 78, 100]:
        print "Third test success!"
    else:
        print c
        print "Third test failed"

    print "====================================================="

testSort(selectionSort)
testSort(insertSort)
testSort(topDownMergeSort)
testSort(bottomUpMergeSort)
