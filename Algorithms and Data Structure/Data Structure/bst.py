import random
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self) -> None:
        self.root = None
    
    def inorder_traversal(self,nodes = []):
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            print(root.data, end=' ')
            nodes.append(root.data)
            inorder(root.right)
        inorder(self.root) 
    
    def preorder_traversal(self):
        def preorder(root):
            if root == None:
                return
            print(root.data, end=' ')
            preorder(root.left)
            preorder(root.right)
        preorder(self.root)
    
    def postorder_traversal(self):
        def postorder(root):
            if root == None:
                return
            postorder(root.left)
            postorder(root.right)
        postorder(self.root)

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
    
    def get_inorder_predecessor(self,root):
        if root == None:
            return None
        par = None
        while root.right != None:
            par = root
            root = root.right
        return par, root
    
    def delete_node(self,x):
        def delete_two_child_node(root):
            par, pre = self.get_inorder_predecessor(root.left)
            if par == None:
                root.left = pre.left
            else:
                par.right = pre.left
            root.data = pre.data

        def relink_node(root):
            next = root
            if root.left != None and root.right != None:
                delete_two_child_node(root)
                next = root
            elif root.left == None:
                next = root.right
            else:
                next = root.left
            return next
            

        def delete(root,x):
            if root == None:
                return None
            if root.data == x:
                return relink_node(root)
            if root.data > x :
                root.left = delete(root.left,x)
            else:
                root.right = delete(root.right,x)
            return root
        self.root = delete(self.root,x)

def node_order(nodes):
    n = len(nodes)
    for i in range(n-1):
        if nodes[i] > nodes[i+1]:
            return False
    return True
     
if __name__ == "__main__":
    tree = Tree()
    n = random.randint(1,10)
    # print(f"testing for {n} random array of input")
    for i in range(n):
        m = random.randint(1,25)
        arr = [random.randint(1,100) for _ in range(m)]
        # arr = [10, 5, 15, 2, 5, 13, 22, 1, 14]
        for ele in arr:
            tree.insert_node(ele)
        while tree.root != None:
            nodes = []
            tree.inorder_traversal(nodes)
            if node_order(nodes) == False:
                print("Nodes of tree are not in right order")
            print()
            tree.preorder_traversal()
            node = random.randint(1,100)
            print(f"\nNode {node} is present = {tree.search_node(node)}")
            val = input("\nEnter node val to delete:\n")
            tree.delete_node(int(val))
            