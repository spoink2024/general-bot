import random
def math_list_primes(start, end):
    tmp = 1
    if start > end:
        tmp = -1
    for i in range(start, end+1, tmp):
        prime = True
        for j in range(2, i):
            if(i%j==0):
                prime = False
        if (prime or i==2 or i==3) and not i==1:
            print(i)

def math_random_square():
    print(random.randint(1, 100) ** 2)

def math_count_to_69():
    for i in range(1, 70):
        print(i)
