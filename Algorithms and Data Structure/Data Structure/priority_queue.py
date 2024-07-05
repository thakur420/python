class PriorityQueue:
    def __init__(self) -> None:
        self.heap = []
        self.map = {}

    def empty(self):
        return len(self.heap) == 0
    
    def _swap(self,par_idx,ch_idx):
        par_key, ch_key = self.heap[par_idx][1], self.heap[ch_idx][1]
        self.heap[par_idx], self.heap[ch_idx] = self.heap[ch_idx], self.heap[par_idx]
        self.map[par_key], self.map[ch_key] = ch_idx, par_idx
    
    def _make_heap(self,ch_idx):
        while ch_idx > 0:
            par_idx = (ch_idx + 1) // 2 - 1
            if self.heap[par_idx][0] > self.heap[ch_idx][0]:
                self._swap(par_idx,ch_idx)
            ch_idx = par_idx

    def _heapify(self, i):
        smallest, n = i, len(self.heap)
        left_child = 2*i+1
        right_child = 2*i+2
        if left_child < n and self.heap[smallest] > self.heap[left_child]:
            smallest = left_child
        if right_child < n and self.heap[smallest] > self.heap[right_child]:
            smallest = right_child
        if i != smallest:
            self._swap(i,smallest)
            self._heapify(smallest) 

    def insert(self,key,priority):
        self.heap.append((priority,key))
        ch_idx = len(self.heap)-1
        self.map[key] = ch_idx
        self._make_heap(ch_idx) 

    def get(self):
        if self.empty():
            return
        n = len(self.heap)
        val = self.heap[0]
        self._swap(0,n-1)
        self.heap.pop()
        del self.map[val[1]]
        self._heapify(0)
        return val

    def decrease_key(self,key,priority):
        if key not in self.map:
            return
        key_idx = self.map[key]
        self.heap[key_idx] = (priority,key)
        self._make_heap(key_idx)

    def print(self):
        print(f"heap => {self.heap}")
        print(f"idx => {self.map}")

def take_user_input():
        user_input = input("Enter key and priority:")
        # print(user_input)
        key, priority = user_input.split()
        return int(key), int(priority)

if __name__ == "__main__":
    pq  = PriorityQueue()
    pq.insert(0,35)
    pq.insert(1,33)
    pq.insert(2,42)
    pq.insert(3,10)
    pq.insert(4,14)
    pq.insert(5,19)
    pq.insert(6,27)
    pq.insert(7,44)
    pq.insert(8,26)
    pq.insert(9,31)
    pq.print()
    while not pq.empty():
        key, new_priority = take_user_input()
        pq.decrease_key(key,new_priority)
        pq.print()
        print(pq.get())
        pq.print()
        key , priority = take_user_input()
        pq.insert(key,priority)
        pq.print()
