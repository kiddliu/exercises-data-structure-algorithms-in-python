'''
R-2.1 Give three examples of life-critical software application.

My serious answer: Wechat, TikTok, Zhihu
'''

'''
R-2.2 Give an example of a software application in which adaptability can mean the difference
between a prolonged lifetime of sales and bankruptcy

My answer: Wechat miniprogram
'''

'''
R-2.3 Describe a component from a text-editor GUI and the methods that it encapsulates

My answer: Context menu. Methods: get_items(), show(), close()
'''

'''
R-2.4 Write a Python class, Flower, that has three instance variables of type str, int, and float,
that respectively represent the name of the flower, its number of petals, and its price. Your class
must include a constructor method that initializes each variable to an appropriate value, and
your class should include methods for setting the vlaue of each type, and retrieving the value of
each type.
'''
class Flower():
    def __init__(self, name, petals, price):
        self.__name = str(name)
        self.__petals = int(petals)
        self.__price = float(price)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = str(value)

    @name.deleter
    def name(self):
        del self.__name

    @property
    def petals(self):
        return self.__petals

    @petals.setter
    def petals(self, value):
        self.__petals = int(value)

    @petals.deleter
    def petals(self):
        del self.__petals

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = float(value)

    @price.deleter
    def price(self):
        del self.__price

'''
R-2.5 Use the techniques of Section 1.7 to revise the charge and make_payment methods of the
CreditCard class to ensure that the caller sends a number as a parameter.

R-2.6 If the parameter to the make_payment method of the CreditCard class were a negative number,
that would have the effect of raising the balance on the account. Revise the implementation
so that it raises a ValueError if a negative value is sent.
'''
def charge(self, price):
    """
    Charge given price to the card, assuming sufficient credit limit.    
    Return True if charge was processed; False if charge was denied.
    """
    if isinstance(price, (int, float)):
        raise TypeError('price should be a number')
    elif price < 0:
        raise ValueError('price should be positive')

    if price + self.balance > self.limit: # if charge would exceed limit,
        return False # cannot accept charge
    else:
        self.balance += price
        return True 

def make_payment(self, amount):
    """Process customer payment that reduces balance."""
    if isinstance(amount, (int, float)):
        raise TypeError('price should be a number')
    elif amount < 0:
        raise ValueError('price should be positive')

    self.balance -= amount

'''
R-2.7 The CreditCard class of Section 2.3 initializes the balance of a new account to zero.
Modify that class so that a new account can be given a nonzero balance using an optional fifth
parameter to the constructor. The four-parameter constructor syntax should continue to produce
an account with zero balance.

C-2.30 At the close of Section 2.4.1, we suggest a model in which the CreditCard class supports
a nonpublic method, _set_balance(b), that could be used by subclasses to affect a change to
the balance, without directly accessing the balance data member. Implement such a model,
revising both the CreditCard and PredatoryCreditCard classes accordingly.
'''
class CreditCard:
    
    def __init__(customer, bank, acnt, limit, balance = 0):
        '''Create a new credit card instance.

        The default balance is zero.

        customer    the name of the customer (e.g., John Bowman)
        bank        the name of the bank (e.g., California Savings)
        acnt        the account identifier (e.g., 5391 0375 9387 5309)
        limit       credit limit (measured in dollars)
        balance     the initial balance of the account
        '''
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance

    def _set_balance(self, b):
        self._balance = b

'''
R-2.8 Modify the declaration of the first for loop in the CreditCard tests, from Code Fragment 2.3,
so that it will eventually cause exactly one of the three credit cards to go over its credit limit.
Which credit card is it?

Answer, Card 3, if the loop continues to 59.
'''

'''
R-2.9 Implement the __sub__ method for the Vector class of Section 2.3.3, so that the expression
u - v returns a new vector instance representing the difference between two vectors.

R-2.10 Implement the __neg__ method for the Vector class of Section 2.3.3, so that the expression
-v returns a new vector instance whose coordinates are all the negated values of the respective
coordinates of v.

R-2.11 In Section 2.3.3, we note that our Vector class supports a syntax such as
v = u + [5, 3, 10, -2, 1], in which the sum of a vector and list returns a new vector. However,
the syntax v = [5, 3, 10, -2, 1] + u is illegal. Explain how the Vector class definition can be
revised so that this syntax generates a new vector.

Answer: The original implementation starts with __add__ only, and the fix is to add __radd__

R-2.12 Implement the __mul__ method for the Vector class of Section 2.3.3, so that the expreesion
v * 3 returns a new vector with coordinates that are 3 times the respective coordinates of v.

R-2.13 Exercise R-2.12 asks for an implementation of __mul__, for the Vector class of Section 2.3.3,
to provide support for the syntax v * 3. Implement the __rmul__ method, to provide additional
support for syntax 3 * v.

R-2.14 Implement the __mul__method for the Vector class of Section 2.3.3, so that the expression
u * v returns a scalar that represents the dot product of the vectors, that is, sum(ui * vi).

R-2.15 The Vector class of Section 2.3.3 provides a constructor that takes an integer d, and
produces a d-dimensional vector with all coordinates equal to 0. Another convenient form for
creating a new vector would be to send the constructor a parameter that is some iterable type
presenting a sequence of numbers, and to create a vector with dimension equal to the length of that
sequence and coordinates equal to the sequence values. For example, Vector([4, 7, 5]) would produce
a three-dimensional vector with coorindiates <4, 7, 5>. Modify the constructor so that either of
these forms is acceptable; that is, if a single integer is sent, it produces a vector of that
dimension with all zeros, but if a sequence of numbers is provided, it produces a vector with
coordinates based on that sequence.

C-2.25 Exercise R-2.12 uses the mul method to support multiplying a Vector by a number, while
Exercise R-2.14 uses the __mul__ method to support computing a dot product of two vectors.
Give a single implementation of Vector. __mul__ that uses run-time type checking to support both
syntaxes u * v and u * k, where u and v designate vector instances and k represents a number.
'''
from collections.abc import Iterable

class Vector:
    def __init__(self, data):
        if isinstance(data, Iterable):
            self._coord = list(data)
        elif isinstance(data, int):
            self._coord = [0] * int

    def __sub(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -self[j]
        return result

    __radd__ = __add__
    __rmul__ = __mul__

    def __mul__(self, multiplier):
        if not isinstance(multiplier, (int, float, Vector)):
            raise TypeError('multiplier must be a number, or a Vector')

        result = Vector(len(self))

        if isinstance(multiplier, (int, float)):
            for j in range(len(self)):
                result[j] = self[j] * multiplier
        else:
            for j in range(len(self)):
                result[j] = self[j] * multiplier[j]

        return result

'''
R-2.16 Our Range class, from Section 2.3.5, relies on the formula
                            max(0, (stop - start + step - 1) // step)
to compute the number of elements in the range. It is not immediately evident why this formula
provides the correct calculation, even if assuming a positive step size. Justify this formula,
in your own words.

My answer: The result is 0, if it's impossible to step from start to stop
           Else, if the step is 1, then it's stop - start.
           And since step - 1 + n // step would result 1 if n is non-zero,
           that is the modulo of the difference of stop and start, and the step is non-zero
           then the length increases by 1 to hold this modolo.
'''

'''
R-2.17 Draw a class inheritance diagram for the following set of classes:
    • Class Goat extends object and adds an instance variable tail and methods milk() and jump().
    • Class Pig extends object and adds an instance variable nose
      and methods eat(food) and wallow().
    • Class Horse extends object and adds instance variables height and color, 
      and methods run() and jump().
    • Class Racer extends Horse and adds a method race().
    • Class Equestrian extends Horse, adding an instance variable weight
      and methods trot() and is trained().

Answer: check R-2.17.pdf
'''

'''
R-2.18 Give a short fragment of Python code that uses the progression classes from Section 2.4.2 to
find the 8th value of a Fibonacci progression that start with 2 and 2 as its first two values.
'''
def find_8th_fib_starts_with_2_2():
    progression = new FibonacciProgression(2, 2)
    progression.print_progression(8)

'''
R-2.19 When using the ArithmeticProgression class of Section 2.4.2 with an increment of 128 and
a start of 0, how many calls to next can we make before we reach an integer of 2^63 or larger?

Answer: 2^ 63 // 128 + 1
'''

'''
R-2.20 What are some potential efficiency disadvantages of having very deep inheritance trees,
that is, a large set of classes, A, B, C, and so on, such that B extends A, C extends B,
D extends C, etc.?

Answer: super may be called many times over in a deep inheritance tree 
        when calling the constructor for the deepest class.
'''

'''
R-2.21 What are some potential efficiency disadvantages of having very shallow inheritance trees,
that is, a large set of classes, A, B, C, and so on, such that all of these classes
extend a single class, Z?

Answer: It lowers the efficiency of your developers and their ability to optimise the code.
        i.e. it can be less performant because it is harder to optimise.
'''

'''
R-2.22 The collections.Sequence abstract base class does not provide support for comparing
two sequences to each other. Modify our Sequence class from Code Fragment 2.14 to
include a definition for the __eq__ method, so that expression seq1 == seq2 will return True precisely
when the two sequences are element by element equivalent.

R-2.23 In similar spirit to the previous problem, augment the Sequence class with method __lt__,
to support lexicographic comparison seq1 < seq2.
'''
from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):
    def __eq__(self, other):
        if not isinstance(other, Sequence):
            raise TypeError('The other should also a Sequence to determine if equal')

        if len(self) != len(other):
            return False
        else:
            for k in range(len(self)):
                if self[k] != other[k]:
                    return False
            return True

    def __lt__(self, other):
        if not isinstance(other, Sequence):
            raise TypeError('The other should also a Sequence to determine if equal')

        for k in range(len(self)):
            try:
                if self[k] != other[k]:
                    return self[k] > other[k]
            except IndexError:
                return True
            
        return False

'''
C-2.24 Suppose you are on the design team for a new e-book reader. What are the primary classes and
methods that the Python software for your reader will need? You should include an inheritance
diagram for this code, but you do not need to write any actual code. Your software architecture
should at least include ways for customers to buy new books, view their list of purchased books,
and read their purchased books.

Answer: check C-2.24.pdf
'''

'''
C-2.26 The SequenceIterator class of Section 2.3.4 provides what is known as a forward iterator.
Implement a class named ReversedSequenceIterator that serves as a reverse iterator for any Python
sequence type. The first call to next should return the last element of the sequence, the second
call to next should return the second-to-last element, and so forth.
'''
class ReversedSequenceIterator:

    def __init__(self, sequence):
        self._seq = sequence
        self._k = len(sequence)

    def __next__(self):
        self._k -= 1
        if self._k > 0:
            return self._seq[self._k]
        else:
            raise StopIteration()

    def __iter__(self):
        return self

'''
C-2.27 In Section 2.3.5, we note that our version of the Range class has implicit support for
iteration, due to its explicit support of both __len__ and __getitem__. The class also receives
implicit support of the Boolean test, “k in r” for Range r. This test is evaluated based on
a forward iteration through the range, as evidenced by the relative quickness of the test
2 in Range(10000000) versus 9999999 in Range(10000000). Provide a more efficient implementation of
the contains method to determine whether a particular value lies within a given range.
The running time of your method should be independent of the length of the range.
'''
class Range:

    def __contains__(self, value):
        return self._start <= value < self._stop and (value - self._start) % step == 0

'''
C-2.28 The PredatoryCreditCard class of Section 2.4.1 provides a process_month method that models
the completion of a monthly cycle. Modify the class so that once a customer has made ten calls to
charge in the current month, each additional call to that function results in an additional $1 surcharge.

C-2.29 Modify the PredatoryCreditCard class from Section 2.4.1 so that a customer is assigned
a minimum monthly payment, as a percentage of the balance, and so that a late fee is assessed if
the customer does not subsequently pay that minimum amount before the next monthly cycle.
'''
class PredatoryCreditCard(CreditCard):
    '''An extension to CreditCard that compounds interest and fees.'''

    def __init__(self, customer, bank, acnt, limit, apr, mmpr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._mmpr = mmpr

        self._payment = 0
        self._charges = 0
        self._late_fee_assessed = False

    def pay(self, amount):
        self._payment += amount

    def charge(self, price):
        success = super().charge(price)

        self._charges += 1
        if (self._charges > 10)
            self._balance -= 1

        if not success:
            self._balance += 5
        return success

    def process_month(self):
        self._charges = 0

        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
        self._balance *= monthly_factor

        if self._balance * self._mmpr > self._payment:
            self._late_fee_assessed = True

'''
C-2.31 Write a Python class that extends the Progression class so that each value in the progression
is the absolute value of the difference between the previous two values. You should include
a constructor that accepts a pair of numbers as the first two values, using 2 and 200 as the defaults.
'''
class AbsoluteDifferenceProgression(Progression):

    def __init__(self, first = 2, second = 200):
        super().__init__(first)
        self._prev = second + first

    def _advance(self):
        self._prev, self._current = self._current, abs(self._prev - self.current)

'''
C-2.32 Write a Python class that extends the Progression class so that each value in the progression
is the square root of the previous value. (Note that you can no longer represent each value with
an integer.) Your constructor should accept an optional parameter specifying the start value, using
65,536 as a default.
'''
import math

class SqrtProgression(Progression):

    def __init__(self, start = 65536):
        super().__init__(float(start))

    def _advance(self):
        self._prev, self._current = self._current, math.sqrt(self._current)

'''
P-2.33 Write a Python program that inputs a polynomial in standard algebraic notation and outputs
the first derivative of that polynomial.
'''
import re

def main233():
    polynomial = input('Please input the polynomial: ')
    symbol = None
    parsed = []
    first_directive = []

    for raw in re.split('+|-', polynomial):
        term = raw.strip()

        if parsed == []:
            symbol = term[term.find('*') + 1:term.find('*') + 2]

        const = int(term[:term.find('*')])
        degree = int(term[term.find('**') + 2:]) if term.find('**') != -1 else 0
        parsed.append((const, degree))

    parsed = sorted(parsed, key = lambda t: t[1], reverse = True)

    for t in parsed:
        if t[1] != 0:
            first_directive.append((t[0] * t[1], t[1] - 1))

'''
P-2.34 Write a Python program that inputs a document and then outputs a barchart plot of
the frequencies of each alphabet character that appears in that document.
'''
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

def main234():
    document = input('Please input the document: ')
    frequencies = {}

    for c in document:
        if c.isalpha():
            if c in frequencies:
                frequencies[c] += 1
            else
                frequencies[c] = 1

    ordered = OrderedDict(sorted(frequencies.items()))

    alphabets = ordered.keys()
    y_pos = np.arange(len(alphabets))
    count = ordered.values()

    plt.bar(y_pos, count, align='center', alpha=0.5)
    plt.xticks(y_pos, alphabets)
    plt.ylabel('Frequencies')
    plt.title('Alphabet character that appears in that document')

    plt.show()

'''
P-2.35 Write a set of Python classes that can simulate an Internet application in which one party,
Alice, is periodically creating a set of packets that she wants to send to Bob. An Internet process
is continually checking if Alice has any packets to send, and if so, it delivers them to Bob's
computer, and Bob is periodically checking if his computer has a packet from Alice, and if so,
he reads and deletes it.
'''
class Alice:
    def __init__(self):
        self._packets = []

    def get_packets(self):
        return self._packets
    
    def send(self, packets):
        self._packets.append(packets)

class InternetProcess:
    def __init__(self, alice, bob):
        self._alice = alice
        self._bob = bob

    def process(self):
        while True:
            packets = self._alice.get_packets()
            if len(packets) > 0:
                self._bob.receive(packets)

class Bob:
    def __init__(self):
        self._packets = []

    def receive(self, packets):
        self._packets = packets
    
    def read(self):
        print(self._packets)
        self._packets.clear()
