class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        size = 0
        self.size = size

    def __str__(self):
        string = ""
        for _ in range(self.size):
            string = string + "🍪"
        return string

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,n):
        if int(n) < 0:
            raise ValueError
        self._capacity = n

    def deposit(self, n):
        self.size += n
        if self.size < 0:
            raise ValueError
        if self.size > self._capacity:
            raise ValueError
        return self.size

    def withdraw(self, n):
        self.size -= n
        if self.size < 0:
            raise ValueError
        if self.size > self._capacity:
            raise ValueError
        return self.size

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self,n):
        if n < 0:
            raise ValueError
        if n > self._capacity:
            raise ValueError
        self._size = n
        return self._size



def main():
    cookie_jar = Jar(capacity=12)
    cookie_jar.deposit(10)
    print(cookie_jar)
    cookie_jar.withdraw(5)
    print(cookie_jar)


if __name__ == "__main__":
    main()
