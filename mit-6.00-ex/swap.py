
def swap0(s1, s2):
    assert type(s1) == list and type(s2) == list
    tmp = s1[:]
    s1 = s2[:]
    s2 = tmp
    return
s1 = [1]
s2 = [2]
swap0(s1, s2)
print s1, s2


def swap1(s1, s2):
    assert type(s1) == list and type(s2) == list
    return s2, s1
s1 = [1]
s2 = [2]
s1, s2 = swap1(s1, s2)
print s1, s2
