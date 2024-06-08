class my_range:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def __iter__(self):
        return my_range_iterator(self)
    
class my_range_iterator:
    def __init__(self,iterable_obj):
        self.iterable_obj = iterable_obj
        

    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            if self.iterable_obj.start >= self.iterable_obj.end:
                raise StopIteration
            current = self.iterable_obj.start
            self.iterable_obj.start += 1
            return current

for i in my_range(1,11):
    print(i)

