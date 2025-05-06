class Book:
    def __init__(self, title, isbn :str):
        if title is None or title == "":
            raise RuntimeError
        
        isbn_short = isbn.replace(" ", "").replace("-","")
        digits = [int(d) for d in isbn_short]
        total = 0
        for i in range(13):
            if i % 2 != 0:
                total += digits[i] * 3
            else:
                total += digits[i]
        if total % 10 != 0:
            raise RuntimeError
        self.__title = title  
        self.__isbn = isbn

    
    @property
    def title(self):
        return self.__title
    
    @property
    def isbn(self):
        return self.__isbn
    


book = Book("dedikkeeend","978-1779501127")