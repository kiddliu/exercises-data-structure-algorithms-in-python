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
'''
class CreditCard:
    
    def __init__(customer, bank, acnt, limit, balance = 0):
        """Create a new credit card instance.

        The default balance is zero.

        customer    the name of the customer (e.g., John Bowman)
        bank        the name of the bank (e.g., California Savings)
        acnt        the account identifier (e.g., 5391 0375 9387 5309)
        limit       credit limit (measured in dollars)
        balance     the initial balance of the account
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance

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
'''
class Vector:
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

    def __mul__(self, multiplier):
        if not isinstance(multiplier, (int, float, Vector)):
            raise TypeError('multiplier must be a number, or a Vector')

        result = Vector(len(self))

        if isinstance(multiplier, (int, float):
            for j in range(len(self)):
                result[j] = self[j] * multiplier
        else:
            for j in range(len(self)):
                result[j] = self[j] * multiplier[j]

        return result

    __rmul__ = __mul__
