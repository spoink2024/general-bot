from math_functions import math_random_square, math_list_primes

def call_function(input_string):
    input_string = input_string.lower()
    if input_string == "random square":
        math_random_square()
    elif input_string == "list primes":
        math_list_primes(int(input("Num 1:")), int(input("Num 2:")))
