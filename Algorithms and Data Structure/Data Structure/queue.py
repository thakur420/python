class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.head = None

    def push(self,x):
        self.__append(x)
    
    def pop(self):
        return self.__del_beg()

    def empty(self):
        return self.head == None

    def peek(self):
        if self.empty():
            return None
        return self.head.data
    
    def __append(self,x):
        new_node = Node(x)
        if self.head == None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next != None:
                curr_node = curr_node.next
            curr_node.next = new_node

    def __del_beg(self):
        if self.head == None:
            return None
        first_node = self.head
        self.head = first_node.next
        val = first_node.data
        del first_node
        return val
    
if __name__ == "__main__":
    queue = Queue()
    queue.push(5)
    queue.push(4)
    print(queue.pop())
    print(queue.pop())
    queue.push(3)
    queue.push(2)
    queue.push(9)
    queue.push(1)
    queue.push(7)
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    queue.push(6)