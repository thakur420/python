import random
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self) -> None:
        self.root = None
    
    def inorder_traversal(self):
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            print(root.data,end=' ')
            inorder(root.right)
        inorder(self.root) 
        
    def insert_node(self,x):
        def insert(root,x):
            if root == None:
                new_node = Node(x)
                if self.root == None:
                    self.root = new_node
                return new_node
            if root.data > x :
                root.left = insert(root.left,x)
            else:
                root.right = insert(root.right,x)
            return root
        insert(self.root,x)

    def search_node(self,x):
        def search(root,x):
            if root == None:
                return False
            if root.data == x:
                return True
            if root.data > x:
                return search(root.left,x)
            return search(root.right,x)
        return search(self.root,x)
    
    def delete_node(self,x):
        def delete(root,x):
            pass
        delete(self.root,x)

if __name__ == "__main__":
    tree = Tree()
    n = random.randint(1,10)
    print(f"testing for {n} random array of input")
    for i in range(n):
        m = random.randint(1,25)
        arr = [random.randint(1,100) for _ in range(m)]
        for ele in arr:
            tree.insert_node(ele)
        tree.inorder_traversal()
        node = random.randint(1,100)
        print(f"\nNode {node} is present = {tree.search_node(node)}")


    