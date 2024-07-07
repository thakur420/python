class Hash:
    def __init__(self,size) -> None:
        self.size = size
        self.table = [None] * size

    def _hash_function(self,key):
        return hash(key) % self.size

    def insert(self,key,value):
        hash = self._hash_function(key)
        # print(key,hash)
        if self.table[hash]:
            for i,(k, _) in enumerate(self.table[hash]):
                if k == key:
                    self.table[hash][i] = (key,value)
                    return
            self.table[hash].append((key,value))
        else:
            self.table[hash] = [(key,value)]

    def find(self,key):
        hash = self._hash_function(key)
        # print(key,hash)
        if self.table[hash]:
            for k,v in self.table[hash]:
                if k == key:
                    return v
        return None

    def delete(self,key):
        hash = self._hash_function(key)
        # print(key,hash)
        val = None
        if self.table[hash]: 
            for k,v in self.table[hash]:
                if k == key:
                    val = v
                    self.table[hash].remove((k,v))
        return val    
    
if __name__ == "__main__":
    h = Hash(13)
    h.insert(111,"rat")
    h.insert(11,"bat")
    h.insert(101,"cat")
    h.insert(93,"sat")
    h.insert(88,"fat")
    h.insert(111,"new_rat")
    print(h.table)
    print(h.find(79))
    print(h.find(93))
    print(h.find(111))
    # print(h.table)
    print(h.delete(15))
    print(h.delete(101))
    print(h.table)