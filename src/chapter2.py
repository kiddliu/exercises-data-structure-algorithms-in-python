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