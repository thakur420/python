class Graph:
    def __init__(self,size) -> None:
        self.matrix = [[0 for _ in range(size)] for _ in range(size)]

    def add_edge(self,src,dest):
        self.matrix[src][dest] = 1
        self.matrix[dest][src] = 1 # undirected graph

    def remove_edge(self,src,dest):
        self.matrix[src][dest] = 0
        self.matrix[dest][src] = 0 # undirected graph
    
    def print(self):
        print(self.matrix)
if __name__ == "__main__":
    graph = Graph(3)
    graph.add_edge(2,1)
    graph.add_edge(1,0)
    graph.print()