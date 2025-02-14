class Queue:
    def __init__(self):
        self.list_of_people = []

    def add(self, item):
        self.list_of_people.append(item)
    
    def next(self):
        return self.list_of_people.pop(0)
    
    def is_empty(self):
        return self.list_of_people == []