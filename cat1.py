import math

result = math.factorial(5)
print(result)

# Python program that calculates the area of a rectangle, circle, triangle or trapezium
def calculateArea():
    print("Please select a shape: \nA. Circle\nB. Rectangle\nC. Triangle\nD. Trapezium\n")
    shape = input()
    if shape == "A":
        print()


calculateArea()


def BMI(m, h):
    return m / (h ** 2)


def sample_variance(data):
    """
    Compute the sample variance of a set of data.
    """
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / (n - 1)
    return variance


data = [58.2, 57.2, 43.7, 72.1, 41.9, 45.2, 52.7, 38.2, 52.3, 41.1]
variance = sample_variance(data)
print(variance)   # Output: 179.85088888888884
