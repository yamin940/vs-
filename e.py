def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle sides")
    if a == b == c:
        return("equilateral")
    elif a == b or b == c or a == c:
        return("isosceles")
    else:
        return("scalene")
    
print(classify_triangle(3,4,5)) 

def course_result(coursework, final, attendance):
    if attendance < 75 or final < 30 or (coursework + final) < 60:
        return("fail")
    else:
        return("pass")
print (course_result(40 ,35 , 80))

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0: print("FizzBuzz") 
        elif i % 3 == 0: print("Fizz") 
        elif i % 5 == 0: print("Buzz")
        else: print(i)
print (fizzbuzz(5))

import math
def is_prime(n):
    if n < 2:
        print(False)
        return
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            print(False)
            return
    print(True)
print (is_prime(7))    

def primes_below(n):
    for i in range(2, n):
        if is_prime_check(i): 
            print(i)

def is_prime_check(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print (is_prime_check(7))

def first_repeated(values):
    found = False
    for i in range(len(values)):
        for j in range(i):
            if values[i] == values[j]:
                print(values[i])
                found = True
                break
        if found:
            break
    if not found:
        print(None)
print (first_repeated([1, 2, 3, 2, 4]))        

def count_pairs(n):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            count += 1
    return count

print(count_pairs(4))

def calculator(command):
    parts = command.split()
    match parts:
        case ['add', a, b]:
            print(int(a) + int(b))
        case ['sub', a, b]:
            print(int(a) - int(b))
        case _:
            raise ValueError("Unknown command")
print(calculator("add 5 10"))       
def parse_int(text, default=None):
    try:
        print(int(text))
    except ValueError:
        print(default)
print (parse_int("123"))      

def stats(*numbers):
    if not numbers:
        print(None)
        return
    smallest = numbers[0]
    largest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    print(smallest, largest)
print (stats(5,2,9,1,7))   

def append_to(item, target=None):
    if target is None:
        target = []
    target.append(item)
    print(target)
print(append_to (10) )    

def make_multiplier(k):
    return lambda x: x * k
print (make_multiplier(3)(5))

def apply_n(f, x, n):
    result = x
    for _ in range(n):
        result = f(result)
    print(result)
print(apply_n(lambda x: x + 2, 5, 3))