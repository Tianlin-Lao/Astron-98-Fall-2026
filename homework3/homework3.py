# 3.1
def say_goodbye(name):
    print('Goodbye,', name)

# 3.2
def area_circle(r):
    print(3.14*r**2)

# 4.1
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    return a/b

# 5.1
def what_should_I_wear(readings):
    return (min(readings), max(readings))

# 5.2
def is_weekend(day):
    if day == 6 or day == 7:
        return True
    else:
        return False

# 5.3 
def fuel_efficiency(miles, gallons):
    return miles/gallons

# 5.4
def secret(i):
    import math
    return (i%10)*10**math.floor(math.log10(i)) + i//10

# 6.1
def power(x, y):
    ans = 1
    for i in range(y):
        ans *= x
    return ans

# 6.2.1 
def min_for(l):
    ans = l[0]
    for i in l:
        if i < ans:
            ans = i
    return ans
def max_for(l):
    ans = l[0]
    for i in l:
        if i > ans:
            ans = i
    return ans

# 6.2.2
def min_while(l):
    i = 0
    ans = l[i]
    while i < len(l):
        if l[i] < ans:
            ans = l[i]
        i += 1
    return ans
def max_while(l):
    i = 0
    ans = l[i]
    while i < len(l):
        if l[i] > ans:
            ans = l[i]
        i += 1
    return ans
    
# 6.3
def sum_digit(i):
    ans = 0
    while i>0:
        ans += i%10
        i = i // 10
    return ans

# 7.1
x = 6789
result = secret(x) # 6789 became 9678
print(f'The result of secret (5.4) with x = {x} is result = {result}')

