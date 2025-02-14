class CircularBuffer:
    def __init__(self, n):
        self.list = []
        self.max_length = n

    def add(self, item):
        self.list.append(item)
        if len(self.list) > self.max_length:
            self.list.pop(0)
    

    def __len__(self):
        return len(self.list)
    
    def __getitem__(self , index):
        return self.list[index]
