'''
R-1.1 Write a short Python function, is_multiple(n, m), that takes two integer values and
returns True if n is a multiple of m, that is, n = mi for some integer i, and False otherwise
'''
def is_multiple(n, m):
    try:
        return n % m == 0
    except ZeroDivisionError:
        return True if n == 0 else False

'''
R-1.2 Write a short Python function, is_even(k), that takes an integer value and
returns True if k is even, and False otherwise.
However, your function, your function cannot use the multiplication, modulo, or division operators.
'''
def is_even(k):
    return bin(k).endswith('0')

'''
R-1.3 Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and
returns the smallest and largest numbers, in the form of a tuple of length two.
Do not use the built-in functions min or max in implementing your solution.
'''
def minmax(data):
    result = sorted(data)
    return result[0], result[-1]

'''
R-1.4 Write a short Python function that takes a positive integer n and
returns the sum of the squares of all the positive integers smaller than n.
'''
def sumofsquares(n):
    result = 0
    i = 1
    while i < n:
        result += i * i
        i += 1
    return result

'''
R-1.5 Give a single command that computes the sum from Exercise R-1.4,
relying on Python's comprehension syntax and the built-in sum function.
'''
def sumofsquares2(n):
    return sum(k * k for k in range(n))

'''
R-1.6 Write a short Python function that takes a positive integer n and
returns the sum of the squares of all the odd positive integers smaller than n.
'''
def sumofoddsquares(n):
    result = 0
    i = 1
    while i < n:
        if i % 2 == 1:
            result += i * i
        i += 1
    return result

'''
R-1.7 Give a single command that computes the sum from Exercise R-1.6,
relying on Python's comprehension syntax and the built-in sum function.
'''
def sumofoddsquares2(n):
    return sum(k * k for k in range(n) if k % 2 == 1)

'''
R-1.8 Python allows negative integers to be used as indices into a sequence, such as a string.
If string s has length n, and expression s[k] is used for index -n <= k < 0,
what is the equivalent index j >= 0 such that s[j] references the same element?

Answer: j = n + k
'''

'''
R-1.9 What parameters should be sent to the range constructor,
to produce a range with values 50, 60, 70, 80?

Answer: range(50, 90, 10)
'''

'''
R-1.10 What parameters should be sent to the range constructor,
to produce a range with values 8, 6, 4, 2, 0, -2, -4, -6, -8?

Answer: range(8, -10, -2)
'''

'''
R-1.11 Demonstrate how to use Python's list comprehension syntax
to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256]

Answer: list(pow(2, k) for k in range(9))
'''

'''
R-1.12 Python's random module includes a function choice(data) that returns a random element
from a non-empty sequence. The random module includes a more basic function randrange, with
parameterization similar to the built-in range function, that return a random choice from
the given range. Using only the randrange function, implement your own version of the choice function.
'''
import random
def mychoice(data):
    return data[random.randrange(0, len(data))]·