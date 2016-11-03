
def amount_packages(packages):
    if packages == 1:
        return 6
    if packages == 2:
        return 9
    if packages == 3:
        return 20
    else:
        return -1000000
    
def cc(n, packages):
    if n == 0:
        return 1
    elif n < 0 or packages == 0:
        return 0
    else:
        return cc(n, packages-1) + cc(n-amount_packages(packages), packages)

def find_the_exact_number():
    n = 1
    while True:
        test = True
        x = n
        for i in range(1, 6):
            if cc(x, 3) == 0:
                test = False
                break
            else:
                x = x + 1
        if test:
            return n - 1
        else:
            n = n + 1

print "Largest number of McNuggest that can not be bought in exact quantity: " + str(find_the_exact_number())
