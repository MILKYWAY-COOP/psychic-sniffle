# Variables
# they are containers for storing data

my_name = "Steve"
print(my_name)

# data types
# strings as anything enclosed in quotes

# numbers
# integers
# floats

# booleans
#True or False
isTuesday = True
isPregnant = False

# lists
my_colors = ["red", "blue", "green"]  # lists are ordered and changeable
# lists can contain different data types
myData = ["Steve", 45, True, "blue", [1, 2, 3, 4, 5]]

# tuples
# tuples are ordered and unchangeable
my_days = ("Monday", "Tuesday", "Wednesday")

# numeric operations
print(2+2)
print(9 % 2)  # 1
print(9/2)  # 0

# conditional statements
isPregnant = False
if (isPregnant == True):
    print("Dorothy is pregnant")
else:
    print("Dorothy is not pregnant")

# loops
# for loop
my_players = ["Steve", "Dorothy", "John", "Jane"]
for i in my_players:
    print(i)

my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in my_numbers:
    if (i % 2 == 0):
        print(i)

for i in my_numbers:
    if (i % 2 == 1):
        print(i)

x = 0
while (x <= 10):
    print(x)
    x += 1


def helloWorld():
    print("Hello World")

helloWorld()

def addTwoNumbers(num1, num2):
    print(num1 + num2)

addTwoNumbers(5, 6)

y = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
print(y)


def is_multiple(n, m):
    if (n % m == 0):
        return True
    else:
        return False

print(is_multiple(10,3))

def getSumOfAllSmallerNumbers(n):
    sum = 0
    for i in range(n):
        square = i * i
        sum += square
    return sum

print(getSumOfAllSmallerNumbers(3))