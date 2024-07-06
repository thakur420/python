class Node:
    def __init__(self,data) -> None:
        self.rank = 0
        self.data = data
        self.parent = data

class DisjointSet:
    def __init__(self) -> None:
        self.map = {}

    def makeset(self,u):
        self.map[u] = Node(u)

    def getset(self,u):
        return self.map[u]

    def findset(self,u):
        u = self.map[u]
        if u.parent == u.data:
            return u.parent
        u.parent = self.findset(u.parent)
        return u.parent
    
    def unionset(self,u, v):
        # print(f"par of {u} => ",end =' ')
        u = self.map[self.findset(u)]
        # print(u.parent)
        # print(f"par of {v} => ",end =' ') 
        v = self.map[self.findset(v)]
        # print(v.parent)
        if u.rank == v.rank:
            u.rank += 1
        if u.rank > v.rank:
            v.parent = u.data
        else:
            u.parent = v.data

if __name__ == "__main__":
    ds = DisjointSet()
    for i in [1,2,3,4,5,6,7]:
        ds.makeset(i)
    ds.unionset(1,2)
    ds.unionset(2,3)
    ds.unionset(4,5)
    ds.unionset(6,7)
    ds.unionset(5,6)
    ds.unionset(3,7)
    for i in [1,2,3,4,5,6,7]:
        print(f"par of {i} = > {ds.getset(i).parent}")
