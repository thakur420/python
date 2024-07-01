from queue import Queue

class Graph:
    def __init__(self,size) -> None:
        self.adj_list = [set() for _ in range(size)]
    
    def add_edge(self,src,dest):
        self.adj_list[src].add(dest)
        self.adj_list[dest].add(src) # undirected graph

    def bfs(self, src):
        queue = Queue()
        visited = set()
        queue.push(src)
        visited.add(src)
        while not queue.empty():
            curr = queue.pop()
            print(curr, end = ' ')
            for node in self.adj_list[curr]:
                if node not in visited:
                    queue.push(node)
                    visited.add(node)

    def dfs(self,src):
        stack = []
        visited = set()
        stack.append(src)
        visited.add(src)
        while len(stack) > 0:
            curr = stack.pop()
            print(curr, end = ' ')
            for node in self.adj_list[curr]:
                if node not in visited:
                    stack.append(node)
                    visited.add(node)

if __name__ == "__main__":
    g = Graph(5)
    edges = [(0, 1), (0,2), (1,3), (2,3), (2,4), (3,4)]
    for u, v in edges:
        g.add_edge(u, v)
    g.bfs(2)
    print()
    g.dfs(0)