class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    
    def __add__(self, other):
        if not isinstance(other, Money):
            raise ValueError()
        
        if not self.currency == other.currency:
            raise(RuntimeError("Mismatched currencies"))
        return Money(self.amount + other.amount, self.currency)
    
    def __sub__(self, other):
        if not isinstance(other, Money):
            raise ValueError()
        
        if not self.currency == other.currency:
            raise(RuntimeError("Mismatched currencies"))

        return Money(self.amount - other.amount, self.currency)
    
    def __mul__(self, number):
        if not (isinstance(number, int) or isinstance(number, float)):
            raise ValueError()
        
        return Money(self.amount * number, self.currency)