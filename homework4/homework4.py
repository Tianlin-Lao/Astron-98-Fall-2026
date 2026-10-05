# 3.1
five_favorite_foods = ['apple', 'banana', 'carrot', 'donuts', 'egg']
print(five_favorite_foods[1])
print(five_favorite_foods[-1])
five_favorite_foods.append('fries')
five_favorite_foods.insert(0, 'orange')
"""
I encountered this error: 
TypeError: 'str' object cannot be interpreted as an integer
I originally wrote: five_favorite_foods.insert('orange', 0)
I fixed it by changing the order of function input
"""
del five_favorite_foods[2]
print(len(five_favorite_foods))
for i in five_favorite_foods:
    print(i.upper())
first_and_last = five_favorite_foods[0::len(five_favorite_foods)-1]
if 'potato' in five_favorite_foods:
    print("A potato!")
else:
    print('No potato!')

# 3.2 
numbers = list(range(21))
def get_first_15(numbers):
    return numbers[:15]
step1 = get_first_15(numbers)
def get_every_5th(lst):
    return lst[0::5]
step2 = get_every_5th(step1)
def reverse_and_stride(lst):
    return lst[::-1][0::3]
step3 = reverse_and_stride(step2)

# 3.3
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(numbers[2])
print(numbers[2][1])
numbers.append([10, 11, 12])
def sum_nested(n):
    ans = 0
    for i in n:
        for j in i:
            ans += j
    return ans

# 3.4
def five_five():
    five_five = []
    for i in range(5):
        five_five.append([])
        for j in range(5):
            five_five[i].append(5*i+j+1)
    return five_five
five_square = five_five()
"""
I encountered this error: 
TypeError: 'builtin_function_or_method' object is not subscriptable
I originally wrote: five_five[i].append[5*i+j]
I fixed it by adding a pair of ()
"""
def replace_3(five_square):
    for i in range(5):
        for j in range(5):
            if five_square[i][j] % 3 == 0:
                five_square[i][j] = '?'
    return five_square
question_square = replace_3(five_square)

def sum_square(question_square):
    ans = 0
    for i in question_square:
        for j in i:
            if j != '?':
                ans += j
    return ans
square_sum = sum_square(question_square)

# 4.1
ages = {'Katie': 30, 'Mariam': 42, 'Safia': 25, 'Mira': 48}
print(ages['Katie'])
"""
I encountered this error: 
KeyError: 0
I originally wrote: print(ages[0])
I fixed it by change 0 to an actual key
"""
ages['Mira'] = 100
ages['Milana'] = 52
del ages['Mariam']
for i in ages:
    print(i, ages[i])

# 5.2
print(five_five())