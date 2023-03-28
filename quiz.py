# 1
def isMultiple(n, m):
    if n % m == 0:
        return True
    else:
        return False


print(isMultiple(81, 9))

# 2


def isEven(n):
    if n % 2 != 0:
        return False
    else:
        return True


print(isEven(82))

# 3


def minmax(data):
    myList = []
    myList.append(min(data))
    myList.append(max(data))
    tuple(myList)
    return tuple(myList)


print(minmax([1, 4, 2, 3, 5, 6, 7, 8, 9, 10]))

# 4


def positiveInteger(n):
    data = []
    for i in range(1, n):
        data.append(i)
    print(sum(data))


positiveInteger(5)


def sumOfOdd(n):
    numbers = []
    for i in range(1, n):
        if i % 2 != 0:
            numbers.append(i)
    squares = []
    for i in numbers:
        squares.append(i ** 2)
    print(sum(squares))


sumOfOdd(5)

# 36
words = ['hello', 'world', 'my', 'hello', 'name', 'is', 'Anna']


def countWords(words):
    count = {}
    for i in words:
        # count[i] = 1
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)


countWords(words)

def oneString(list):
    word = ''
    for i in list:
        word += i
    print(word)

oneString(['hello','world','my','hello','name','is','Anna'])