from math import *
import math

def odd(n):
    return n % 2 == 1

def generate_odd():
    n = 3
    while True:
        yield n
        n = n + 2
    
def generate_primes(n):

    prime_list = [2,]
    for candidate_prime in generate_odd():
        if candidate_prime > n:
            break
        is_prime = True
        for test in prime_list:
            if test > math.sqrt(candidate_prime):
                break
            else:
                if candidate_prime % test == 0:
                    is_prime = False
        if is_prime == True:
            prime_list.append(candidate_prime)

    return prime_list

def display_sum_of_log_prime_n_and_ratio(n):
    sum_of_log_prime = 0
    list_of_prime = generate_primes(n)
    for item in list_of_prime:
        sum_of_log_prime += log(item)
    ratio = n / sum_of_log_prime
    print sum_of_log_prime, n, ratio

display_sum_of_log_prime_n_and_ratio(100)
display_sum_of_log_prime_n_and_ratio(1000)
display_sum_of_log_prime_n_and_ratio(10000)
display_sum_of_log_prime_n_and_ratio(100000)
display_sum_of_log_prime_n_and_ratio(1000000)
