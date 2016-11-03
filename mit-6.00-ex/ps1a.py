import math

def odd(n):
    return n % 2 == 1

def generate_odd():
    n = 3
    while True:
        yield n
        n = n + 2
    
    
count = 1

prime_list = [2,]

for candidate_prime in generate_odd():
    is_prime = True
    for test in prime_list:
        if test > math.sqrt(candidate_prime):
            break
        else:
            if candidate_prime % test == 0:
                is_prime = False
    if is_prime == True:
        prime_list.append(candidate_prime)
        count  = count + 1
    if count >= 1000:
        break


for item in prime_list:
    print item,
