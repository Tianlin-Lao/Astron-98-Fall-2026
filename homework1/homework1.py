# File: homework1.py

# --- Variables and Data Types ---
a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # b is a float number, a number with decimals

c = 3j
print(c)
print(type(c)) # c is a complex number, a number with a real and imaginary part as defined in math

d = "hello"
print(d)
print(type(d)) # d is a string, a sequence of characters

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, a collection of any parameter in a specific order

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, pairs of keys and values

g = (1, 2)
print(g)
print(type(g)) # g is a tuple, a collection of any parameter in a specific order that cannot be changed unlike a list

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, a collection of any parameter in a specific order

i = True
print(i)
print(type(i)) # i is a boolean, a value that is True or False

j = None
print(j)
print(type(j)) # j is a NoneType, a value that represents missing or undefined value

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list, a collection of any parameter in a specific order

l = str(14)
print(l)
print(type(l)) # l is a string, a sequence of characters

m = 1e4
print(m)
print(type(m)) # m is a float number, a number with decimals

# There are nine distinct data types here
# These data types are: int, float, complex, str, list, dict, tuple, bool, NoneType
# Variable e, h, k are all lists; variable d and l are both strings; variable b and m are both floats
# Variable l is a string because it was the function output of str(), which outputs a string representation of the input
# One data type that is not represented here is a set, which is a collection of unique elements
n = {1, 2, 3}
print(n)
print(type(n)) # n is a set, a collection of unique elements

# --- Booleans ---
10 > 9 #True
10 == 9 #False
10 <= 9 #False
bool("abc") #True
bool(123) #True
bool(["apple", "cherry", "banana"]) #True
bool(True) #True
bool(False) #False
bool(0) #False
bool("") #False
bool(" ") #True
bool(()) #False
bool([]) #False
bool({}) #False
bool(True and False) #False
bool(True and True) #True
bool(False and False) #False
bool(True or False) #True
bool(True or True) #True
bool(False or False) #False
bool(not(False)) #True
bool(not(True)) #False

# Expressions returning True or False are boolean expressions.
# bool(" "). Python do not count white space?
# 1==1 True Because 1 is equal to 1 mathematically
# 1!=1 False != means not equal to

# --- Operators ---
10 + 5 # 15, + preforms addition
10 - 5 # 5, - preforms subtraction
2 * 4 # 8, * preforms multiplication
6 / 3 # 2.0, / preforms division
5 % 2 # 1, % preforms modulus
3 ** 2 # 9, ** preforms exponential 
15 // 2 # 7, // preforms floor division

5 == 2 # False, == compares whether two values are equal
10 != 10 # False, != compares whether two values are not equal
2 < 5 # True, < compares whether the left value is less than the right value
12 > 5 # True, > compares whether the left value is greater than the right value
5 <= 6 # True, <= compares whether the left value is less than or equal to the right value
1 >= 10 # False, >= compares whether the left value is greater than or equal to the right value

x = 5
x += 5 # 10, += updates the value on the left by adding value on the right to it
x -= 4 # 6, -= updates the value on the left by subtracting value on the right from it
x *= 3 # 18, *= updates the value on the left by multiplying value on the right to it

# operator and returns True if both statements are true (True and True = True, True and False = False)
# operator or returns True if one of the statements is true (True or False = True, False or False = False)
# operator not reverses the result. (not(True) = False, not(False) = True)

# The difference between / and // is that / returns a float value while // returns an integer value.
# The difference between % and // is that % returns the remainder of a division while // returns the integer value of a division.
# We use % to find the remainder of a division, like 3%2=1
# Assignment operators work by updating the value of a variable based on its current value.

# --- Strings ---
my_string = "hello"

print(my_string) # Prints: hello
print(my_string[0]) # Prints: h, indexing starts at 0
print(my_string[1]) # Prints: e
print(my_string[2]) # Prints: l
print(my_string[3]) # Prints: l
print(my_string[4]) # Prints: o
print(my_string[-1]) # Prints: o, negative indexing starts at -1
print(my_string[1:3]) # Prints: el, slicing returns a substring from index 1 to 2
print(my_string[0:5:2]) # Prints: hlo, slicing returns a substring from index 0 to 4 for every 2nd character
print(len(my_string)) # Prints: 5, len() returns the length of the string
print(my_string + "goodbye") # Prints: hellogoodbye, + concatenates two strings
print(my_string * 7) # Prints: hellohellohellohellohellohellohello, * repeats the string 7 times

# Term slicing is a way to extract a portion of a string by specifying a start index, an end index, and a step value. 
name = "Oski"
print("Hello, my name is " + name) # Prints: Hello, my name is Oski

print(f"Hello, my name is {name}") # Prints: Hello, my name is Oski

# These statements are the same because f-strings allow for variable interpolation

# --- Terminal Commands ---
# cd
# Changes directories. Use it to move from one folder to another
# Example: cd Desktop

# ls
# Lists the contents of the current directory. Use it to see what files and folders are in the current directory
# Example: ls

# ls -a
# Lists all contents of the current directory, including hidden files and folders. Use it to see all files and folders in the current directory
# Example: ls -a

# mkdir
# Creates a new directory. Use it to create a new folder in the current directory
# Example: mkdir new_folder

# cat
# Displays the contents of a file. Use it to view the contents of a file in the terminal
# Example: cat 111.txt

# pwd
# Prints the current working directory. Use it to see the full path of the current directory
# Example: pwd

# cd ..
# Moves up one directory level. Use it to go back to the parent directory
# Example: cd ..

# cd . 
# Stays in the current directory. Use it to stay in the current directory
# Example: cd .

# cd ~
# Moves to the home directory. Use it to go to the home directory
# Example: cd ~

# cp
# Copies a file or directory. Use it to make a copy of a file or directory
# Example: cp 111.txt 222.txt

# mv
# Moves a file or directory. Use it to move a file or directory to a new location
# Example: mv 111.txt new_folder/111.txt

# rm
# Removes a file or directory. Use it to delete a file or directory
# Example: rm 111.txt

# clear 
# Clears the terminal screen. Use it to clear the terminal screen
# Example: clear

# grep
# Searches for a specific pattern in a file. 
# Example: grep "hello" 111.txt



# echo
# Prints a message to the terminal. Use it to display a message in the terminal
# Example: echo "hello world"

# man
# Displays the manual for a command. Use it to see the manual for a command
# Example: man ls

# exit
# Exits the terminal. Use it to close the terminal
# Example: exit 


# The difference between ls and ls -a is that ls only lists the contents of the current directory while ls -a lists all contents of the current directory, including hidden files and folders.
# A hidden file is a file that is not normally visible in the file system. Done by setting the hidden attribute.
# 3 other flags for ls are -l, -h, and -R. -l lists the contents of the current directory in long format, -h lists the contents of the current directory in human-readable format, and -R lists the contents of the current directory recursively.



