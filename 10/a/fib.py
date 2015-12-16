__author__ = 'gauth_000'
class Fib():
    def __init__(self, n):
        self.n=n
        self.a=0
        self.b=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.b>=self.n:
            raise StopIteration
        else:
            self.a, self.b=self.b, self.a+self.b
            return self.b
f=Fib(30)
print(list(f))