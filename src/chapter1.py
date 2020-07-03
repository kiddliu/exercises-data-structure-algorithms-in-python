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
    return data[random.randrange(0, len(data))]

'''
C-1.13 Write a pseudo-code description of a function that reverses a list of n integers, so that
the numbers are listed in the opposite order than they were before, and compare this method to an
equivalent Python function for doing the same thing.

Answer:

current index is 0
mid is the ceiling of n / 2

while current index is smaller than mid
    exchange list[current index] and list[n - 1 - current index]
    current index increases by 1
'''

'''
C-1.14 Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose product is odd.
'''
def is_product_odd_pair_in(data):
    return len([k for k in data if k % 2 == 1]) > 1

'''
C-1.15 Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other(that is, they are distinct).
'''
def is_sequence_elements_distinct(data):
    i = 0
    while i < len(data):
        i += 1
        if data[0] in data[i:]:
            return False
    return True

'''
C-1.16 In our implementation of the scale function (page 25), the body of the loop executes the command
data[j] *= factor. We have discussed that numeric types are immutable, and that use of the *= operator
in this context causes the creation of a new instance (not the mutation of an existing instance).
How is it still possible, then, that our implementation of scale changes the actual parameter sent by
the caller?

Answer: It's only possible if the sequence, that is data in this case, is mutable.
'''

'''
C-1.17 Had we implemented the scale function (page 25) as follows, does it work properly?

def scale(data, factor):
    for val in data:
        val *= factor

Explain why or why not.

Answer: No, it doesn't. Because val is only an alias to the current loop value,
        and changing it won't affact the actual element.
'''

'''
C-1.18 Demonstrate how to use Python's list comprehension syntax
to product the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]

Answer: list(k * (k + 1) for k in range(10))
'''

'''
C-1.19 Demonstrate how to use Python's list comprehension syntax to produce the list
['a', 'b', 'c', ..., 'z'], but without having to type all 26 such characters literally.

Answer: list(chr(k + ord('a')) for k in range(26))
'''

'''
C-1.20 Python's random module includes a function shuffle(data) that accepts a list of elements
and randomly reorders the elements so that each possible order occurs with equal probability.
The random module includes a more basic function randint(a, b) that returns a uniformly random
integer from a to b (including both endpoints). Using only the randint function, implement your
own version fo the shuffle function.
'''
def my_shuffle(data):
    import random
    index = 0
    while index < len(data):
        target = data[random.randint(index, len(data) - 1)]
        data.remove(target)
        data.insert(0, target)
        index += 1
    return data

'''
C-1.21 Write a Python program that repeatedly reads lines from standard input until an EOFError
is raised, and then outputs those lines in reverse order (a user can indicate end of input by
typing Ctrl-D).
'''
def main():
    lines = []
    try:
        while True:
            lines.insert(0, input())
    except EOFError:
        pass
    for line in lines:
            print(line)

if __name__ == "__main__":
    main()

'''
C-1.22 Write a short Python program that takes two arrays a and b of length n storing int values,
and returns the dot product of a and b. That is, it returns an array c of length n such that
c[i] = a[i] * b[i], for i = 0, ..., n - 1.
'''
def array_dot_product(a, b):
    return [a[i] * b[i] for i in range(len(a))]

'''
C-1.23 Give an example of a Python code fragment that attempts to write an element to a list based
on an index that may be out of bounds. If that index is out of bounds, the program should catch the
exception that results, and print the following error message:
"Don't try buffer overflow attacks in Python!"
'''
def try_write_out_of_bound():
    some_list = []
    try:
        some_list[1] = 3
    except IndexError:
        print("Don't try buffer overflow attacks in Python!")

'''
C-1.24 Write a short Python function that counts the number of vowels in a give character string.
'''
def count_vowels(s):
    return len([c for c in list(s) if c in ['a', 'e', 'i', 'o', 'u']])

'''
C-1.25 Write a short Python function that takes a string s, representing a sentence, and
returns a acopy of the string with all punctuation removed. For example, if given the string
"Let's try, Mike.", this function would return "Let's try Mike"
'''
def remove_punc(s):
    return ''.join([c for c in list(s) if 'A' <= c <= 'z' or c == ' '])

'''
C-1.26 Write a short program that takes as input three integers, a, b, and c, from the console and
determines if they can be used in a correct arithmetic formula (in the given order), like
"a + b = c", "a = b - c", or "a * b = c".
'''
def main2():
    a = int(input())
    b = int(input())
    c = int(input())

    import operator
    arithmetics = [
        operator.add,
        operator.sub,
        operator.mul,
        operator.floordiv
    ]

    try:
        return c in [op(a, b) for op in arithmetics]
    except ZeroDivisionError:
        return False

'''
C-1.27 In section 1.8, we provided three different implementations of a generator that
computes factors of a given integer. The third of those implementations, from page 41,
was the most efficient, but we notes that it did not yield the factors in increasing order.
Modify the generator so that it reports factors in increasing order, while maintaining
its general performance advantages.
'''
def factors(n):
    k = 1
    bigger_half = []
    while k * k <= n:
        if n % k == 0:
            yield k
            bigger_half.insert(0, n // k)
        k += 1
    for k in bigger_half:
        yield k

'''
C-1.28 The p-norm of a vector v = (v1, v2, ..., vn) in n-dimensional space is defined as
                ||v|| = p√(v1 ** p + v2 ** p + ... + vn ** p)
For the special case of p = 2, this results in the traditional Euclidean norm, which represents
the length of the vector. For example, the Euclidean norm of a two-dimensional vector with
coordinates (4, 3) has Euclidean norm of √(4 ** 2 + 3 ** 2) = √(16 + 9) = √25 = 5.
Give an implementation of a function named norm such that norm(v, p) returns the p-norm value of v
and norm(v) returns the Euclidean norm of v. You may assume that v is a list of numbers.
'''
def norm(v, p = 2):
    import math
    return math.pow(sum(math.pow(k, p) for k in v), 1 / p)