#1
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


#2
def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):          #range要求内容是int，同时注意range范围
        if n % i == 0:
            return False
    return True


#3
def fizzbuzz(n):
    for i in range(1, n + 1):                  #写range注意范围
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)


#4
def factorial1(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial2(n):
    if n == 1:
        return n
    else:
        return n * factorial2(n - 1)         #递归


#5
def fibonacci(n):
    a, b = 1, 1
    if n == 1 or n == 2:
        return 1
    for i in range(n - 2):
        a, b = b, a + b
    return b


#6
def reverse_string(s):
    chars = list(s)            #字符串不可变
    i, j = 0, len(s) - 1
    while i < j:
        chars[i], chars[j] = chars[j], chars[i]
        i += 1
        j -= 1
    return "".join(chars)


#7
def dedupe(nums):
    result = []
    for j in nums:
        if j not in result:
            result.append(j)
    return result


#8
def average(nums):
    if not nums:
        return None
    total = 0
    for i in nums:
        total += i
    return total / len(nums)


#9
def is_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


#10
def multiplication_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{i} × {j} = {i * j}", end="\t")
        print()
