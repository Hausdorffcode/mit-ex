
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

print cc(50, 3)
print cc(51, 3)
print cc(52, 3)
print cc(53, 3)
print cc(54, 3)
print cc(55, 3)

print cc(16, 3)
