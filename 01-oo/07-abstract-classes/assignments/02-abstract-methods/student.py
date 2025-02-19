# Write your code here
from abc import ABC, abstractmethod


class A(ABC):
    def a(self):
        self.b()

    def e(self):
        self.c()
    
    @abstractmethod
    def c(self):
        pass

    @abstractmethod
    def b(self):
        pass

class B(A):
    def b(self):
        self.a()

    def c(self):
        self.e()


class C(B):
    def f(self):
        pass


class D(A):
    def b(self):
        self.f()
    
    @abstractmethod
    def f(self):
        pass


class E(D):
    def c(self):
        self.a()

    def f(self):
        self.e()

    def g(self):
        self.f()


class F:
    def a(self):
        self.b()
        self.f()
    
    def b(self):
        pass

    def f(self):
        pass
    


f = F()
print(f)