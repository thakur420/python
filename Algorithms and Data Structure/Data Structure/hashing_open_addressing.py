import time
class Hash:
    def __init__(self,size) -> None:
        self.size = size
        self.table = [None] * size
        self._primes = self._find_next_two_prime(self.size)
        self.count = 0

    def _find_next_two_prime(self,start):
        return 101,103

    def _hash_function(self,key,prob_cnt=0):
        p1, p2 = self._primes
        hash_val = (hash(key)%p1 + (hash(key) + prob_cnt)%p2 * prob_cnt) % self.size
        return hash_val
    
    def _rehash(self):
        print("performing rehashing ....")
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0

        for item in old_table:
            if item is not None:
                self.insert(item[0],item[1])

    def insert(self,key,value):
        if self.count / self.size > 0.7:
            self._rehash()

        prob_cnt = 0
        while True:
            hash = self._hash_function(key,prob_cnt)
            if self.table[hash] is None:
                self.table[hash] = (key,value)
                self.count += 1
                break
            if self.table[hash][0] == key:
                self.table[hash] = (key,value)
                break
            prob_cnt += 1

    def find(self,key):
        prob_cnt = 0
        while True:
            hash = self._hash_function(key,prob_cnt)
            if self.table[hash] is None:
                return None
            if self.table[hash][0] == key:
                return self.table[hash][1]
            prob_cnt += 1

    def delete(self,key):
        prob_cnt = 0
        while True:
            hash = self._hash_function(key,prob_cnt)
            if self.table[hash] is None:
                return None
            if self.table[hash][0] == key:
                val = self.table[hash][1]
                self.table[hash] = None
                return val
            prob_cnt += 1

if __name__ == "__main__":
    h = Hash(13)
    h.insert(111,"rat")
    h.insert(1,"bat")
    h.insert(14,"cat")
    h.insert(27,"sat")
    h.insert(40,"collision")
    h.insert(88,"fat")
    h.insert(111,"new_rat")
    print(h.table)
    print(h.find(40))
    print(h.find(27))
    print(h.find(111))
    print(h.find(88))
    print(h.table)
    h.insert(21,"rome")
    print(h.table)
    h.insert(98,"tome")
    h.insert(8,"comb")
    h.insert(54,(1,2))
    h.insert(34,(6,8))
    h.insert(65,(5,7))
    h.insert(33,33)
    print(h.find(54))
    print(h.delete(15))
    print(h.delete(101))
    print(h.delete(98))
    print(h.delete(34))
    print(h.table)