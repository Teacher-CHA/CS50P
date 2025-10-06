"""
Suppose that you’d like to implement a cookie jar in which to store cookies. In a file called jar.py, implement a class called Jar with these methods:
__init__ should initialize a cookie jar with the given capacity, which represents the maximum number of cookies that can fit in the cookie jar. If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.
__str__ should return a str with 🍪, where is the number of cookies in the cookie jar. For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though, deposit should instead raise a ValueError.
withdraw should remove n cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
capacity should return the cookie jar’s capacity.
size should return the number of cookies actually in the cookie jar, initially 0.
"""
class Jar:#jar中capacity和size是不能够直接改动的变量，size必须通过deposit和withdraw改动
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or int(capacity) < 0:
            raise ValueError
        else:
            self.capacity = capacity 
            self.size = 0 

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if not isinstance(n, int) or n + self.size > self.capacity or n < 0:
            raise ValueError
        else:
            self.size = n + self.size

    def withdraw(self, n):
        if not isinstance(n, int) or self.size - n < 0  or n < 0:
            raise ValueError
        else:
            self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if int(capacity) < 0:
            raise ValueError
        else:
            self._capacity = capacity 

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if int(size) < 0:
            raise ValueError
        else:
            self._size = size

jar = Jar(10)
jar.deposit(5)
jar.withdraw(2)
print(jar)